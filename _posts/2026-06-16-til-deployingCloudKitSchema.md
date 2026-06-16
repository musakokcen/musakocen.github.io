---
layout: blogpost
tags: [til]
title: "Deploying CloudKit Schema to Production"
subtitle: ""
---
<p>I’ve been working on my side project <a href="{{ '/soccer-mappr/' | relative_url }}">Soccer Mappr</a>  and managed to tailor the main features to the level that I can present to people. There is still a lot to add and improve, however, the starting idea has been reached. I've done many tests, recorded real games over many weeks, and all were consistent and looked like I desired. Until I faced a problem with syncing data to the cloud in a production build.</p>

<p>When I released the TestFlight version and installed from there to both my iPhone and Apple Watch, I saw that the manual entries were not syncing to the cloud. It was an interesting pain point initially because I thought I broke something while changing schemas, adding migrations during development.</p>

<p>The problem is about CloudKit's two environments: my records lived in the Development environment, while TestFlight runs in the Production environment. These are not the schemes in Xcode but the environments in the <a href="https://icloud.developer.apple.com/dashboard" target="_blank" class="underline">CloudKit dashboard</a>. I was always using the app that I installed from Xcode. I did my changes and ran on my devices. Later, when I deployed to TestFlight, I hadn't noticed they weren't syncing properly because I kept quickly reinstalling from Xcode for some reason.</p>

<p>But the deeper reason is the one that actually matters. In the Development environment, CloudKit auto-creates record types and fields for you the first time you save them. That's why it always "just worked" while I developed. Production does not do this. Apple's <a href="https://developer.apple.com/library/archive/documentation/General/Conceptual/iCloudDesignGuide/DesigningforCloudKit/DesigningforCloudKit.html" target="_blank" class="underline">Designing for CloudKit</a> guide spells it out: "your app can save records. Or you can add fields to records that aren't in the schema and then CloudKit creates the corresponding record types and fields for you. This feature is not available in the production environment." So when Production had no schema matching my data model, CloudKit silently rejected every write. That's why even new entries made on TestFlight, on both devices, never synced to each other. There was nothing on the server to accept them.</p>

<p>The solution was simple. Well, it can become complicated over time, but initially simple. You go to the CloudKit dashboard and deploy the schema to Production. That's it. Then everything works as expected.</p> 

<p>One thing to keep in mind so this doesn't happen again: this is not a one-time setup. Every time you change your SwiftData model, you have to redeploy the schema to Production before shipping the build that uses it, otherwise Production sync silently breaks all over again.</p>

<p>And there is one more thing that can make things complicated in the future: once a schema is deployed to Production you cannot remove keys or change a field's type. You can only add new keys. So plan your model changes accordingly.</p>

Source: *<a href="https://developer.apple.com/library/archive/documentation/General/Conceptual/iCloudDesignGuide/DesigningforCloudKit/DesigningforCloudKit.html" target="_blank" class="underline">Apple Developer Documentation: Designing for CloudKit</a>* 
