---
layout: blogpost
tags: [writes]
title: "Quiz Bürger: A Side‑Project Journey"
subtitle: "A minimalist app for the “Leben in Deutschland” test, built with SwiftUI, SwiftData, and Apple’s Translation Framework"
---

Last week I published the Quiz Bürger app. I had been working on it for some time as a side project. In this app, where I wrote the UI components in SwiftUI and used SwiftData for the database, my goal was to keep things as simple as possible, follow Apple’s Human Interface Guidelines, experiment with a few new frameworks, put what I already knew into practice, and build something useful for people.

<div class="image-container">
  <img src="/assets/img/lebenindeutschlandappicon.webp" alt="Quiz Bürger App" class="main-image" style="max-width: 256px;">
</div>
<p class="image-caption"><a href="https://apps.apple.com/us/app/quiz-b%C3%BCrger-lid-2026/id6758575798">Quiz Bürger App on Appstore</a></p>


### Why this specific topic?
There were two important reasons why I chose this topic as a side project. First, I personally needed something like this. Second, there were no high‑quality apps available for this topic. That gave me strong motivation to finish and publish the project.

Last year I took the “Leben in Deutschland” exam in Germany, also known as the Einbürgerungstest. This exam asks questions from a fixed question pool, and you pass if you answer more than half correctly. You can prepare for it on public transport, during short breaks, and similar situations. For that, I installed many apps. However, most of them used webviews, were full of ads, and had strange UI and UX. Because of this, my goal was to build a simple, distraction‑free, offline app that focused only on its purpose.

### My architecture and tech choices
By storing the questions inside the app, I made it fully offline. I made en effort to follow Apple’s design principles, used default components and symbols wherever I could. I used Apple’s Translation framework for translations, SwiftUI for UI development, and SwiftData for the database. In the end, I built a simple app that focuses on the goal.

### User flow and small settings
The app consists of a quiz page with all the questions, a page that lists the incorrectly answered questions, bookmarked questions page, and finally a test simulation page. The user must select their federal state because the questions are determined based on that. In addition, there are a few small settings. They include options like turning haptic feedback on or off, automatically removing a question from the “incorrect questions” list when it is answered correctly, and automatically moving to the next question after a question is answered correctly. These are simple options but can improve the user’s learning experience.

### Trying out Apple's Translation Framework
While working on this feature, I discovered Apple’s Translation framework. My goal was to let users translate the questions into the language of their choice. When I thought about how to translate the question screen, I noticed that the framework supports different features such as batch translation. Instead of translating one question and four answers in a loop, using this batch mechanism, provided by the framework, was more logical. Technically, this was easy to implement, but from a user‑experience perspective, every new question caused a new loading indicator to appear. This made batch translation impractical for me. After that, I considered pre‑translating questions and storing the translations in the database. That way, each question would be translated only once. I tried pre‑loading and translating every three questions, but if the user skipped questions quickly, this approach still caused problems and affected the experience. I also had to handle the case where the user changes their target language. In the end, I switched to user-driven translation idea. The exam is in German, and many people take it without learning any German yet. Instead of understanding the questions and learning the topic, they often just memorize the answers. Translating only the questions that the user struggles with feels like a more sensible solution in this context. 

### Localization with AI and “good enough”
For app localization (parts outside the questions), I used AI to help with translations. Because I couldn’t translate every language myself, this approach helped me a lot. When I look at the English, Turkish, and German localizations, I can’t say I’m completely happy with the translations, but the app is still improving, and I’m not in a position to do a better job right now. I also took this approach for the promotional text, app description, and similar content. In the next versions, I plan to spend more time refining these parts. With its current state, I felt the app was ready to be published because it already solves the main problem.

### App Store screenshots and design with Sketch
I prepared the App Store screenshots in Sketch. I wrote a snapshot test / script to capture all supported languages’ screenshots. Then, I used an online tool to place these screenshots inside phone frames. I imported them into Sketch, arranged them into one of the sizes accepted by the App Store, and finished the layout. I did this for each screen together with its visual promotional text and created a shared symbol. For other languages, I reused this symbol and only localized the images and text. Through this process, I made good progress in design and working with Sketch. I learned many shortcuts, practical solutions, and how to use the tools more effectively. I also learnt the concept of "symbols" during this work. 

### Launch
The first version of the app was published last week. I didn’t share it with anyone during this time, but the App Store statistics already show impressions (views on the App Store apps list) and downloads. I created issues on GitHub for the app’s missing features and I plan to update it as I complete them. I’ve even submitted the next version for review already.

----

Download the app: [Quiz Bürger App on the Appstore](https://apps.apple.com/us/app/quiz-b%C3%BCrger-lid-2026/id6758575798)