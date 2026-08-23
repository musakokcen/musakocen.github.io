---
layout: landing
title: Heatiz – Privacy Policy
permalink: /soccer-mappr/privacy/
---

# Privacy Policy

**Last Updated: {{ "now" | date: "%B %d, %Y" }}**

## Introduction

This Privacy Policy describes how Heatiz ("the App") handles your information. The App consists of an iPhone app and an Apple Watch app that work together to record soccer matches and generate movement heatmaps.

**In short: Your health and location data stays in your Apple ecosystem. Heatiz never sends your personal data to external servers.**

## Information We Access

Heatiz accesses the following data to provide its core functionality:

### Apple Health Data

The App requests read access to Apple Health to retrieve:

- **Workout sessions** — soccer workouts recorded by the Apple Watch app
- **Workout routes** — GPS location data captured during each match, used to generate your heatmap
- **Heart rate** — recorded during the workout, shown in your match summary
- **Heart rate variability (HRV)** — read from Apple Health to compute your daily Recovery Score
- **Resting heart rate** — read from Apple Health to compute your daily Recovery Score
- **Sleep analysis** — read from Apple Health to compute your daily Recovery Score
- **Active calories burned** — recorded during the workout, shown in your match summary and used in training load calculations

This data is read from Apple Health on your device. It is not uploaded to any server operated by Heatiz.

### Match Stats (User-Generated)

After each match, you may optionally log:

- Personal performance rating
- Goals and assists
- Positions played

This data is stored locally on your device using SwiftData and synced between your iPhone and Apple Watch via iCloud (CloudKit). It is not accessible to us or any third party.

### Location Data

GPS location is captured by your Apple Watch during a workout session and stored in Apple Health as a workout route. The App reads this route to render your heatmap and compute movement statistics. Location data is never transmitted to Heatiz's servers — it remains within your device and iCloud account.

## How Data Is Used

All data accessed by Heatiz is used solely to provide the app's features:

- Rendering your pitch heatmap
- Displaying match stats and health metrics in your history
- Computing movement statistics (distance, sprints, speed zones)
- Computing your daily Recovery Score from HRV, resting heart rate, sleep, and training load
- Syncing match records between your iPhone and Apple Watch

## Data Storage and Sync

- **Apple Health** stores your workout sessions and GPS routes on your device.
- **iCloud / CloudKit** syncs your match stats between your iPhone and Apple Watch. This data lives in your personal iCloud account and is governed by Apple's iCloud privacy terms.
- **No Heatiz servers** receive, store, or process your personal data.

## Weather

Heatiz uses Apple's WeatherKit framework to fetch historical weather conditions for completed matches. The request uses your match location and date; no personal identifier is included. WeatherKit requests are subject to Apple's own privacy policy.

## Diagnostic Data

Heatiz uses Apple's MetricKit framework to capture crash diagnostic reports on your device if the app crashes. This data is stored locally on your device only. It is never automatically transmitted anywhere. If you choose to share a crash report with us for support purposes, you do so manually through Settings → Diagnostics → Share Crash Report. You can clear all stored crash reports at any time from the same screen.

## Third-Party Services

Heatiz does not integrate with any third-party analytics, advertising, or tracking services. All frameworks used (HealthKit, CloudKit, WeatherKit, MetricKit) are provided by Apple.

## Data Security

Because your data remains on your device and in your iCloud account, it is protected by Apple's device and iCloud security measures. We recommend:

- Keeping your device's operating system up to date
- Using device passcode or biometric authentication
- Enabling iCloud encryption where available

## Children's Privacy

The App does not knowingly collect personal information from children under the age of 13. The App is suitable for all ages.

## Your Rights and Data Control

Since Heatiz does not collect or store your data on external servers, you have full control over your data at all times:

- **Revoke Health access**: go to iPhone Settings → Privacy & Security → Health → Heatiz
- **Delete match stats**: swipe to delete individual matches within the app, or delete the app to remove all local records
- **Remove iCloud data**: delete your iCloud data through iPhone Settings → [your name] → iCloud → Manage Account Storage
- **Delete workout data**: remove workouts directly in the Apple Health or Fitness apps
- **Clear crash reports**: go to Settings → Diagnostics → Clear Crash Reports within the app

## Changes to This Privacy Policy

We may update this Privacy Policy from time to time. Changes will be reflected by updating the "Last Updated" date at the top of this page. We encourage you to review this page periodically.

## Contact Us

If you have any questions about this Privacy Policy, please contact us:

**Email:** [support@heatiz.com](mailto:support@heatiz.com)

## Consent

By using the App, you consent to this Privacy Policy.

---

_This privacy policy is effective as of the date listed above and applies to the current version of Heatiz._
