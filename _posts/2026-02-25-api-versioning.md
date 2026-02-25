---
layout: blogpost
tags: [writes]
title: "Designing for Version Uncertainty: API Versioning in Mobile Clients with On-Premise Servers"
subtitle: ""
---

In many software projects, different server solutions have been used: some products rely solely on a local database, others on cloud‑based databases, and some on on‑premise servers. Version management is relatively easier in the first case than the last, or more challenging in the last case. Consider a product that has been released after considerable effort. A few months or even a year later, new features have been added, the server version has been incremented, and a new release is ready for customers. However, not all customers want or are able to adopt these new features immediately. Some lack the capacity to upgrade, while others plan the transition for months in the future.

From the perspective of the mobile client owner, how would this situation be handled?

When you have a project that needs to support multiple versions, the client should handle this gracefully. This becomes even more important when the server is on-premise. In mobile apps, there is no synchronized update between server and client because users update the app through the App Store or Google Play whenever they want. So the client needs to figure things out during its first communication with the server. For this, you need a sustainable strategy.

## The Problem

There are a few things to keep in mind here:
- You don't know when (or if) users will update your app.
- Version detection is a runtime task. Mobile apps are installed from app stores, not from your server.
- As new versions are deployed, older ones must still be supported until they are explicitly dropped. This matters even more with on-premise servers, since supported versions can vary across deployments.
- The mobile client can only know which version the server supports after it talks to the server.

## Version Discovery: The Handshake Endpoint

If you don't already know the version information, which version do you use to ask for it? That's why you need a **versionless discovery endpoint**, in other words, a handshake endpoint you can call without knowing anything about the server's current version first.

```
GET /api/hello
// or
GET /api/discover

// Response:
{
  "supportedVersions": ["1.0", "2.0", "3.0"],
  "minimumVersion": "1.0",
  "recommendedVersion": "3.0",
  "deprecatedVersions": ["1.0"],
  "sunset": {
    "1.0": "2025-06-01"
  }
}
```

Based on this response, the client performs **version resolution**: it finds the intersection of what the server supports and what the client supports, then picks the highest common version. Note that this is not HTTP content negotiation (the mechanism driven by `Accept` / `Content-Type` headers). What happens here is a client-side decision. The client selects the best version both sides can speak.

> **Deprecation Signaling:** Including a `sunset` field in the discovery response to announce when deprecated versions will be removed is a good practice. The client can read this at startup and surface a warning to administrators before the cutoff arrives.

This handshake endpoint should be one of the most stable, backward-compatible contracts you ship. If it ever breaks, nothing else can work.

---

## Scattered Version Checks Problem

Different API versions will naturally have different endpoints, features, response schemas, and contracts. This is the biggest problem to solve. At first, the differences may look small or simple; a field renamed here, a new parameter there. This pushes you toward quick fixes with `if` statements. But it spreads over time, leads to several well-known code smells, and puts the codebase in a state that is hard to recover from.

Here's why this is problematic:
- Many features are already tested using the `if-else` approach, and reworking them introduces risk.
- Version checks cause version information to be scattered everywhere.
- Every API and method ends up needing version awareness, which makes testing harder and violates the Open/Closed Principle.

```swift
// ❌ DON'T DO THIS
class UserRepository {
    func getUser(id: String) async throws -> User {
        if negotiatedVersion >= ApiVersion(major: 2, minor: 0) {
            let response = try await http.get("/api/v2/users/\(id)")
            return try UserV2Dto(from: response).toDomain()
        } else {
            let response = try await http.get("/api/v1/users/\(id)")
            return try UserV1Dto(from: response).toDomain()
        }
    }
}
```

---

## Recommended Approach

The solution is built in two layers that work together: the **Strategy Pattern** defines what the implementations look like, and the **Factory Pattern** handles how the right one gets selected. One gives you the structure, the other gives you the selection mechanism.

### Version-Specific Implementations with Strategy Pattern

The Strategy Pattern requires three things: a common interface, interchangeable implementations behind it, and a context that delegates to whichever one was selected, without knowing which one it is. Here, the protocol is the interface, each versioned struct is an interchangeable strategy, and the repository is the context that simply calls through:

```swift
protocol UserApi {
    func getUser(id: String) async throws -> User
}

struct UserApiV1: UserApi {
    func getUser(id: String) async throws -> User {
        let response = try await http.get("/api/v1/users/\(id)")
        return try UserV1Dto(from: response).toDomain()
    }
}

struct UserApiV2: UserApi {
    func getUser(id: String) async throws -> User {
        let response = try await http.get("/api/v2/users/\(id)")
        return try UserV2Dto(from: response).toDomain()
    }
}
```

The repository receives whichever strategy was selected and calls it without any awareness of which version it is talking to. The version decision happens elsewhere, exactly once.

### Centralized Version Resolution with Factory Pattern

A factory centralizes the version resolution decision. The rest of the codebase simply asks for an implementation and it never inspects the version itself:

```swift
class ApiFactory {
    private let versionNegotiation: VersionNegotiation
    private var registry: [ObjectIdentifier: [AnyApiRegistration]] = [:]

    func resolve<T>(_ type: T.Type) throws -> T {
        let version = versionNegotiation.version

        guard let registrations = registry[ObjectIdentifier(T.self)] else {
            throw ApiFactoryError.notRegistered(String(describing: T.self))
        }

        let sorted = registrations.sorted { $0.minVersion > $1.minVersion }

        for registration in sorted {
            if registration.appliesTo(version) {
                return registration.factory() as! T
            }
        }

        throw ApiFactoryError.unsupportedVersion(version, String(describing: T.self))
    }
}
```

> resolve sorts the registrations by version, highest first, before iterating, so the first match is always the highest applicable version. The caller's list order does not matter.

This solution works well when different API versions are not in use simultaneously — meaning after version resolution, all requests go to the same server version for the duration of the session.

---

## Alignment with SOLID Principles

These approaches make it possible to support multiple versions cleanly:

**Single Responsibility:** Version detection, storing the negotiated version, and selecting the right implementation are each a separate unit with one job.

**Open/Closed:** Adding support for a new server version means registering a new implementation. Existing code is not touched:

```swift
func registerApis() {
    // Adding v3 requires no changes to UserRepository or any caller
    register(UserApi.self, [
        ApiRegistration(factory: { UserApiV3() }, minVersion: ApiVersion(3, 0)),
        ApiRegistration(factory: { UserApiV2() }, minVersion: ApiVersion(2, 0)),
        ApiRegistration(factory: { UserApiV1() }, maxVersion: ApiVersion(2, 0, exclusive: true)),
        //                                         ^-- everything below v2.0
        //                                         (using 1.9 would exclude v1.10+ under semver)
    ])
}
```

**Dependency Inversion:** Repositories depend on the protocol, not on any concrete implementation. No matter which version was resolved at runtime, the concrete type behind the protocol can be swapped without the repository knowing:

```swift
// UserRepository never imports UserApiV1 or UserApiV2.
// It only knows UserApi. The factory handles the rest.
class UserRepository {
    private let api: any UserApi

    init(api: any UserApi) {
        self.api = api
    }
}
```

---

Once you have clean, isolated implementations, a new question emerges: what do you do when v2 is 90% identical to v1?

## DRY: Inheritance vs. Composition

Not every new version involves 100% changes. A new endpoint may be added while everything else stays the same. In that case, the v2 implementation can inherit from v1 and only override what changed:

```swift
// Inheritance approach
class UserApiV2: UserApiV1 {
    override func getUser(id: String) async throws -> User {
        // Only the changed endpoint is overridden
        let response = try await http.get("/api/v2/users/\(id)")
        return try UserV2Dto(from: response).toDomain()
    }
    // getUserPreferences() is inherited from v1 — stays the same
}
```

However, this introduces the **Fragile Base Class** problem. A patch or bug fix in `UserApiV1` can unintentionally affect `UserApiV2` in unexpected ways. What makes this particularly risky is that version-specific implementations tend to diverge silently over time and you may not discover the breakage until a customer on a specific server version reports it.

A safer alternative is **composition**: inject the previous version's implementation as a dependency rather than inheriting from it. The tradeoff is more boilerplate, but the dependency relationship is explicit and the fragility is low:

```swift
// Composition approach
struct UserApiV2: UserApi {
    private let v1: any UserApi // fallback for unchanged endpoints

    func getUser(id: String) async throws -> User {
        let response = try await http.get("/api/v2/users/\(id)")
        return try UserV2Dto(from: response).toDomain()
    }

    func getUserPreferences(id: String) async throws -> UserPreferences {
        // Explicitly delegates to v1 — the dependency is visible
        return try await v1.getUserPreferences(id: id)
    }
}
```

Even though the system looks good in theory, in practice you need to detect code smells and iterate on the solution to make it fit your project.

## Detecting Code Smells

**Shotgun Surgery:** If changing version information requires modifications in many files, there is a dependency that shouldn't exist. Version knowledge should be confined to the factory and the registration setup — nowhere else.

**Primitive Obsession:** Using version strings throughout the codebase leads to subtle mistakes. A value object adds type safety and makes comparisons reliable:

```swift
// ❌ Primitive obsession
if version == "2.0" { ... }

// ✅ Value object
struct ApiVersion: Comparable, CustomStringConvertible {
    let major: Int
    let minor: Int

    static func < (lhs: ApiVersion, rhs: ApiVersion) -> Bool {
        if lhs.major != rhs.major { return lhs.major < rhs.major }
        return lhs.minor < rhs.minor
    }

    var description: String { "\(major).\(minor)" }
}
```

**Feature Envy:** If callers are repeatedly asking about the negotiated version to decide what to do, that logic belongs in the factory, not in the caller. The factory's contract is simple: ask for a type, get the right implementation back. The caller should never care which version is behind it.

---

## Edge Cases to Think About

Some scenarios that are easy to overlook but important to handle explicitly:

- **What if the server doesn't return a handshake response?** Fall back to a cached version from the last successful session, or fail with a clear, human-readable error. Never silently fall back to a hardcoded version.
- **What if there's no common version between server and client?** Surface a specific error telling the user the minimum required server version, rather than a generic failure.
- **What if the user logs out and connects to a different server?** Each server connection must carry its own negotiated version. Never share version state globally across different server contexts.
- **What if the server version changes between app sessions?** Re-run the handshake at each session start. Don't assume the cached version is still valid.
- **What if the server gets updated while the app is running?** Define a policy, either complete the session against the known version and re-negotiate on next launch, or listen for a server-sent signal to re-negotiate mid-session.

## Testing Strategy

Every layer of this implementation should be tested independently and together.

**Unit tests** verify that the factory returns the correct implementation for a given version, including boundary versions and edge cases. Registration logic and version comparison should be covered exhaustively here since this code is the foundation everything else rests on.

**Contract tests** verify that a given API version implementation still behaves as the server expects, consider request shape, response parsing, and error handling. In a mobile context, this typically means testing each versioned implementation against recorded or mocked server responses, so that a response schema change on the server side is caught before it reaches production.

**Integration tests** verify that the client works end-to-end against different server versions, covering the full flow from handshake to version resolution to calling the correct endpoints. These tests run against real or simulated server instances and are a must-have requirement, unit tests alone cannot catch the failure modes that only surface when the full stack is exercised together.

---

## Conclusion

API versioning on the client side requires careful architectural thinking and thorough planning upfront. The cost of not doing this is real: version checks scattered across the codebase, tests that are difficult to maintain, and bugs that only surface for customers on a specific server version which are the hardest kind to reproduce and the most damaging to trust.

But the architecture described here pays off most visibly at the end of a version's life. When the time comes to drop v1 support, the work is almost trivial: remove the `UserApiV1` registration and update the minimum version floor. No `if` statements to hunt down, no repository logic to untangle, no risk of accidentally breaking v2 while removing v1 specific code. The version simply stops existing in the codebase as cleanly as it was added. That is the real measure of a well-designed versioning strategy, how little it costs to let one go.