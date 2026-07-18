---
layout: blogpost
tags: [til]
title: "watchOS Location Authorization Is Arbitrated by the iPhone"
subtitle: ""
---
<p>While working on the watch side of <a href="{{ '/soccer-mappr/' | relative_url }}">Soccer Mappr</a>, I hit a permission bug that made no sense at first: every time I opened the app, the location permission prompt appeared again. I would tap "Allow", the session would work fine, and then the next launch would ask all over again as if I had never answered.</p>

<p>The setup looked correct. The watch app uses <code>CLLocationManager</code> so I had added <code>NSLocationWhenInUseUsageDescription</code> to the Watch target's Info.plist. That's where the code runs, so that's where the key belongs. Or so I thought. Checking the authorization status confirmed the weird part: it came back as <code>.notDetermined</code> on every new session, even right after the user had granted access.</p>

<p>It turns out that on watchOS, location authorization isn't owned by the watch at all. It's arbitrated by the paired iPhone. When you grant location access on the watch, the system needs to record that grant on the iPhone side and it can only do that if the iOS companion target declares the same usage description keys. Without them, the system has nowhere to persist the answer, so the grant silently evaporates and <code>.notDetermined</code> comes back on the next launch.</p>

<p>The fix was to add the same <code>NSLocationWhenInUseUsageDescription</code> key to the iOS companion target's Info.plist. Even though the companion app never directly calls <code>CLLocationManager</code>. Once the keys exist on both sides, the grant persists across sessions and the prompt shows up only once, as it should.</p>

<p>The counterintuitive lesson: the target that runs the location code is not necessarily the target that owns the permission. On watchOS, the iPhone is the source of truth, so the usage description keys have to live in both places.</p>

Source: *<a href="https://developer.apple.com/forums/thread/696692" target="_blank" class="underline">Apple Developer Forums: How to properly ask for location permissions in WatchOS 8</a>*
