---
layout: work
title: Career
permalink: /experience/
---

Seven years of building Apple-platform products, from a large-scale super app to apps I shipped on my own. The full CV is available on request via [LinkedIn](https://www.linkedin.com/in/musakokcen/) or [email](mailto:{{ site.email }}).

---

## Software Engineer

**C4B Com for Business** | _Munich, Germany_ | _July 2024 – Present_

Native iOS, macOS and Android (Flutter) clients for XPhone NextGen, a unified communications platform that business customers run on their own servers.

- **Native meetings:** Designed and delivered the native meeting experience end to end: WebRTC audio and video, two-way screen sharing, Picture-in-Picture, on-device background effects and moderation. It reached verified feature parity with the web client and shipped on schedule.
- **Three-day prototype:** Used Claude Code to map company-specific APIs and business rules into a working meeting prototype in three days, work that would have taken weeks by hand, while I built the UI in parallel.
- **API versioning:** Designed a framework that lets one app build serve customers on different server versions, through version negotiation, capability interfaces and graceful feature degradation. Annotation-driven code generation turned onboarding a new server version into a single annotated class. Write-ups: [API versioning]({% post_url 2026-02-25-api-versioning %}), [@Injectable annotations]({% post_url 2026-02-17-injectable-annotations %}).
- **iOS depth in Flutter:** Brought iOS expertise into the Flutter codebase, fixed platform-specific issues that cut iOS-only QA reports, and removed every UI creation warning.
- **Beyond my own tickets:** Drive bug triage and cross-team root-cause analysis and review pull requests. Automated tests and TestFlight and Google Play deployment with Fastlane.

---

## Software Engineer

**CHECK24** | _Munich, Germany_ | _November 2022 – July 2024_

Bank account module in CHECK24's large-scale iOS super app.

- **SwiftUI module:** Built and maintained the module in SwiftUI and refactored legacy UIKit along the way, which stabilized UI tests and reduced layout bugs.
- **Architecture decision:** Made the case for SwiftUI in architecture reviews with evidence and an incremental migration plan. The module became the team's reference for SwiftUI adoption.
- **Requirements first:** Clarified requirements and edge cases with product and backend before building, which meant fewer post-release issues and support tickets.

---

## Software Engineer

**Plus Minus One** | _Istanbul, Turkey_ | _July 2020 – October 2022_

A small product team building B2C iOS apps from the first plan to App Store release.

- **Math AI** (formerly Math Hero; 27K+ App Store reviews, 4.7 rating, 10M+ problems solved): set up the base project and built screen and camera recording with ReplayKit, a photo and video editing pipeline, LaTeX input, OCR and live chat.
- **Reliability under pressure:** Kept crash-free sessions above 99.7% with bi-weekly releases by investing early in modular architecture and performance, even when the pressure was to ship fast.
- **EasyFax, Call Recorder, EasyScanner:** Migrated the apps from Objective-C to Swift, redesigned the UI, added in-app purchases and set up CI on Bitrise.
- **Planty**, featured by Apple on the App Store: built a light meter from device sensors and a custom keyboard extension.
- **Team:** Mentored junior developers and ran code reviews.

---

## Software Engineer

**Pineal Creative Technologies / Live View Sports** | _Istanbul, Turkey_ | _October 2019 – July 2020_

LVStudio, an iOS and iPadOS app for learning sports skills from video.

- **Stability:** Brought the crash rate below 0.3% by tracking down and fixing crash-prone areas.
- **Architecture:** Refactored modules from MVC to VIPER to make them testable.
- **Video:** Built resumable background downloads and video caching.

---

## Independent Products

Apps I design, build and ship on my own. More on the [Projects](/projects/) page.

- **[Heatiz](/heatiz/)**, a soccer tracker for iPhone and Apple Watch. Built with SwiftUI, watchOS, HealthKit, Core Location and CloudKit, from product definition to App Store release and post-launch updates. [Why I built it]({% post_url 2026-10-24-whyIBuiltHeatiz %}).
- **[Quiz Bürger](/einbuergerungstest/)**, an offline prep app for the German naturalization test. [The story]({% post_url 2026-02-16-releasingQuizBurger %}).
- **[World Cup Diaries](https://github.com/musakokcen/WWDCWorldCup2026)**, a SwiftUI diary app built with Xcode 27's agentic features that publishes to this blog. [The story]({% post_url 2026-06-20-building-world-cup-diaries-with-xcode-intelligence %}).
