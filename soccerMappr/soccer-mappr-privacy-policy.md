---
layout: landing
title: Soccer Mappr – Privacy Policy
permalink: /soccer-mappr/privacy/
---

# Privacy Policy

**Last Updated: {{ "now" | date: "%B %d, %Y" }}**

## Introduction

This Privacy Policy describes how Soccer Mappr ("the App") handles your information. The App consists of an iPhone app and an Apple Watch app that work together to record soccer matches and generate movement heatmaps.

**In short: Your health and location data stays in your Apple ecosystem. Soccer Mappr never sends your personal data to external servers.**

## Information We Access

Soccer Mappr accesses the following data to provide its core functionality:

### Apple Health Data

The App requests read access to Apple Health to retrieve:

- **Workout sessions** — soccer workouts recorded by the Apple Watch app
- **Workout routes** — GPS location data captured during each match, used to generate your heatmap
- **Heart rate** — recorded during the workout, shown in your match summary
- **Active calories burned** — recorded during the workout, shown in your match summary

This data is read from Apple Health on your device. It is not uploaded to any server operated by Soccer Mappr.

### Match Stats (User-Generated)

After each match, you may optionally log:

- Personal performance rating
- Goals and assists
- Positions played

This data is stored locally on your device using SwiftData and synced between your iPhone and Apple Watch via iCloud (CloudKit). It is not accessible to us or any third party.

### Location Data

GPS location is captured by your Apple Watch during a workout session and stored in Apple Health as a workout route. The App reads this route to render your heatmap. Location data is never transmitted to Soccer Mappr's servers — it remains within your device and iCloud account.

## How Data Is Used

All data accessed by Soccer Mappr is used solely to provide the app's features:

- Rendering your pitch heatmap
- Displaying match stats and health metrics in your history
- Syncing match records between your iPhone and Apple Watch

## Data Storage and Sync

- **Apple Health** stores your workout sessions and GPS routes on your device.
- **iCloud / CloudKit** syncs your match stats between your iPhone and Apple Watch. This data lives in your personal iCloud account and is governed by Apple's iCloud privacy terms.
- **No Soccer Mappr servers** receive, store, or process your personal data.

## Third-Party Services

Soccer Mappr does not integrate with any third-party analytics, advertising, tracking, or crash reporting services.

## Data Security

Because your data remains on your device and in your iCloud account, it is protected by Apple's device and iCloud security measures. We recommend:

- Keeping your device's operating system up to date
- Using device passcode or biometric authentication
- Enabling iCloud encryption where available

## Children's Privacy

The App does not knowingly collect personal information from children under the age of 13. The App is suitable for all ages.

## Your Rights and Data Control

Since Soccer Mappr does not collect or store your data on external servers, you have full control over your data at all times:

- **Revoke Health access**: go to iPhone Settings → Health → Data Access & Devices → Soccer Mappr
- **Delete match stats**: swipe to delete individual matches within the app, or delete the app to remove all SwiftData records
- **Remove iCloud data**: delete your iCloud data through iPhone Settings → [your name] → iCloud → Manage Account Storage
- **Delete workout data**: remove workouts directly in the Apple Health or Fitness apps

## Changes to This Privacy Policy

We may update this Privacy Policy from time to time. Changes will be reflected by updating the "Last Updated" date at the top of this page. We encourage you to review this page periodically.

## Contact Us

If you have any questions about this Privacy Policy, please contact us:

**Email:** [{{ site.email }}](mailto:{{ site.email }})

## Consent

By using the App, you consent to this Privacy Policy.

---

_This privacy policy is effective as of the date listed above and applies to the current version of Soccer Mappr._
