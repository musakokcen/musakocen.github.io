---
layout: blogpost
tags: [writes]
title: Understanding @Injectable, @Singleton, and @LazySingleton in Flutter
subtitle: ""
---

I was recently deep into debugging a dependency issue when I found myself in a situation where I needed to understand dependency injection annotations more deeply. They are more or less self-descriptive, but when you need to orchestrate the order of initialization, reusing, and disposing, things start to get complicated. Therefore, I want to break down these concepts and express my understanding.

`@Injectable`, `@Singleton`, and `@LazySingleton` are `injectable` library annotations built on top of the `GetIt` library. `GetIt` makes it easy to access dependencies across your app, you define them, register them, and then access them anywhere. However, the "register" step can become overwhelming over time. That's where the `injectable` library comes in. When a class is annotated with a dependency annotation, it gets registered automatically through the `build_runner` code generator.

Without `injectable`:

```dart
final getIt = GetIt.instance;
void setup() {
  getIt.registerFactory<ApiService>(() => ApiService(getIt<HttpClient>()));
  getIt.registerSingleton<AuthManager>(AuthManager(getIt<TokenStorage>()));
  getIt.registerLazySingleton<UserRepository>(() => UserRepository(getIt<ApiService>()));
}
```

`GetIt` provides three core registration methods: `registerFactory`, `registerSingleton`, and `registerLazySingleton`. `injectable` is a code generator that writes those calls for you based on annotations. The three annotations map 1:1 to these three `GetIt` methods. Without `GetIt`, `injectable` has no purpose. Without `injectable`, `GetIt` still works but requires manual wiring.

As your app grows, maintaining manual registrations becomes painful. Forgotten registrations cause runtime crashes, constructor changes break registration code, and dependency ordering becomes a puzzle. `injectable` eliminates all of that by reading your constructors, resolving the dependency graph, and generating the registration code for you.

### `@Injectable` — Factory Registration

Every time you request an instance from GetIt, it creates a **new instance**. Each call to `getIt<MyService>()` gives you a new object.

```dart
@injectable
class HomePageCubit extends Cubit<HomePageState> {
  HomePageCubit(HomePageRepository repo) : super(HomePageInitial());
}
```

Under the hood, this generates `gh.factory<HomePageCubit>(...)`. The object lives only as long as whatever holds a reference to it.

### `@Singleton` — Classic Singleton

Registers the class as a singleton that is **created immediately** when `configureDependencies()` runs at app startup. One instance, shared across the entire app, alive from the start.

```dart
@singleton
class ApplicationService with WidgetsBindingObserver {
  ApplicationService(TokenStorage storage) {
    // starts listening to auth changes immediately
  }
}
```

This is used when the object needs to be alive and ready from the moment the app launches, listening to streams, initializing connections, or providing a foundation that other services depend on during startup. If you're using `@preResolve` for async singletons, the initialization timing works differently.

### `@LazySingleton` — Lazy Singleton

Same as `@Singleton` in that only **one instance** ever exists, but it's created **lazily**, constructed only the **first time** someone requests it via `getIt<MyService>()`.

```dart
@lazySingleton
class ImagePreviewClass {
  // only created when someone actually needs to preview an image
}
```

If nothing ever requests this service, it's never created at all. This saves startup time and memory.

---

## Challenges: Lifecycle Management

The annotations look clean in isolation. The challenges emerge when your app has authentication flows, stream subscriptions, and services with different lifespans.

### Singletons Survive Logout

When your user logs out, session expires, or anything else, **singletons and lazy singletons don't get destroyed.** They stay in GetIt, holding references, with stream subscriptions still active. If a repository is subscribed to User A's data stream and User A logs out, that subscription doesn't stop on its own, you have to stop it explicitly. Alternatively, **GetIt scopes** let you push a scope on login and pop it on logout, disposing everything in that scope automatically.

### Factories Don't Know About Their Own Death

`@Injectable` classes are created fresh each time and **GetIt doesn't track them after creation.** Disposing is your responsibility. If a cubit holds a stream subscription and the user navigates away, that subscription keeps running unless you cancel it. `BlocProvider` handles this for you, but if you're resolving cubits manually via `getIt<T>()`, you must call `close()` yourself.


## `cancel()` vs `close()` — They're Not the Same

This is not about dependency management, but streams are everywhere, and handling them correctly impacts the lifespan of the classes. And this is where a subtle but painful mistake hides.

`cancel()` is called on a `StreamSubscription`, you stop listening, but the stream itself stays alive. `close()` is called on a `StreamController`, it shuts the entire stream down for everyone.

Why does this matter? Because **singletons survive logout**. If you `close()` a controller on logout, the next login cycle tries to add events to a dead controller and throws a `StateError`. You almost never want to close a controller on a singleton during logout, only cancel the subscription.

- **Logout** — `cancel()` subscriptions, keep controllers open. The object lives on.
- **App shutdown** via `@disposeMethod` — `cancel()` and `close()` everything. Truly done.
- **`@Injectable` on widget dispose** — `cancel()` and `close()` everything. A new instance will be created next time anyway.

## Final Thoughts

The annotations themselves are simple. The hard part is managing what happens between a session's start and end for objects that outlive that boundary, and what happens on screen exit for objects that don't manage their own cleanup. Singletons don't know about session's lifecycle. Factories don't know about their own death. You need to bridge both gaps explicitly, either through an orchestrator pattern, where a `@singleton` calls reset methods on every service on auth changes, or through GetIt scopes that align with your auth boundaries.

Get the lifecycle management right, and dependency injection in Flutter becomes a pleasure. Get it wrong, and you'll spend hours debugging stale streams, closed controllers, and phantom subscriptions.