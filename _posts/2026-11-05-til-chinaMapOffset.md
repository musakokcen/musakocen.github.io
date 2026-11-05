---
layout: blogpost
tags: [til]
title: "GPS Coordinates Don't Line Up with Maps in China"
subtitle: ""
---
<p>A few days ago I got an email from a <a href="{{ '/heatiz/' | relative_url }}">Heatiz</a> player in China. He wrote that the pitch coordinates were shifted. The heatmap and the pitch outline sat on the map next to the pitch, not on it. I was surprised, because I had tested this part of the app many times. My confusion didn't last long, though. He also told me the cause. China doesn't use the GPS coordinate system I know.</p>

<p>So I looked into it. GPS, and HealthKit with it, gives coordinates in WGS-84, the standard system used almost everywhere. Chinese law doesn't allow maps in those coordinates. Map data for mainland China has to use GCJ-02, a system that shifts every point by a deliberately irregular offset, roughly 100 to 700 metres depending on where you are.</p>

<p>To see it myself, I built a preview that draws a match as a phone in China would see it and points the map at a stadium in Beijing. The problem was there straight away: the whole match landed significantly north and east of the grass, on top of buildings and roads.</p>


<p>As far as I know, there is no built-in solution that handles this for developers. MapKit expects WGS-84 coordinates and doesn't tell you which map it is showing. So I needed to convert the coordinates myself before they go into MapKit. The GCJ-02 formula is widely published, and most China-facing map code uses it. Everything the app stores stays in WGS-84, and a coordinate is converted only at the moment it goes into MapKit:</p>

```swift
let onMap = ChinaCoordinateTransform.wgs84ToGCJ02(trackPoint)
```

<p>A coordinate that comes back out of the map, like a pitch corner the player drags, is converted back. GCJ-02 has no exact inverse, so that direction repeats the shift and corrects its guess until it lands, which takes a few steps to get well under a millimetre.</p>

<p>The formula was the easy part. Deciding when to use it took more thought:</p>

<ul>
<li><strong>Only in mainland China.</strong> Hong Kong, Macau and Taiwan use the normal map. A pitch is judged by its centre, so its four corners move together even right on a border.</li>
<li><strong>Only when the phone gets the China map.</strong> That depends on where the phone is, not where the match was played. A player in China looking at a match from abroad sees the normal map, so nothing should move. With no API to ask, I use the device's time zone, since phones set it from the network.</li>
</ul>

<p>In short, GPS coordinates are not the same everywhere on a map. In mainland China, the map uses its own shifted system, and MapKit won't convert your coordinates for you. If your app draws its own data on a map, convert it before it goes in, keep what you store in WGS-84, and test with a location in China.</p>


Sources:
- *<a href="https://en.wikipedia.org/wiki/Restrictions_on_geographic_data_in_China" target="_blank" class="underline">Wikipedia: Restrictions on geographic data in China</a>*
- *<a href="https://developer.apple.com/forums/thread/797697" target="_blank" class="underline">Apple Developer Forums: thread 797697</a>*
- *<a href="https://github.com/googollee/eviltransform" target="_blank" class="underline">eviltransform: open-source WGS-84 / GCJ-02 conversion</a>*
