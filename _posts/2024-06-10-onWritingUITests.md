---
layout: blogpost
title: My first impressions of writing UI Tests
subtitle: ""
---

Writing my first UITest gave me mixed feelings about its nature. So I wanted to share my first impressions. It is likely that there will be new things, maybe some cons will be removed or different opinions on some pros will get later, I think the beginning is worth saying something.

The first thing was about its difference from unit testing. While we sometimes mock classes to write unit tests, use flags, and thus take advantage of having access to internal operations, UI testing is not like that. The main purpose is to automate UI testing and get unbiased results. UI testing performs the same actions as a customer who does not have access to internal operations.

Writing UI tests is simple in many ways; you define a user journey, launch the application and watch it happen as defined. Another advantage is that once you have UI tests, you do not have to manually test every new feature. It also helps you to see weaknesses in your UI and also lack of access to some elements in the view. There can be difficult actions to write UI tests, but some of them can be solved by adding accessibility identifiers. 

Writing ui tests has a slightly higher learning curve than unit tests. You need to know how to find an element, scroll, tap, type, and so on. You need to keep a reference handy to learn this. However, there is one nice thing that helps a lot when you start writing ui tests; xcode's code generation. You can write a ui test function and by clicking the record button, Xcode will copy whatever you do in the simulator. This is a perfect way to start writing UI tests. But then you need to optimise the generated test function, treat it like a cheat book and clean up the code. The second thing is that this feature can easily be disconnected from the simulator and some events cannot be recorded. This is a headache if you only rely on Xcode's UI recording test feature. However, it is a good place to start when developing. It is useful to keep in mind that recording failures sometimes point to problems in UI development.

Running UI tests takes a long time. So I would not write UI tests for everything. Imagine running the app from Xcode for every user journey and repeating it. Unbearable. Also, network requests may be slower at the time the tests are running or the async task is running. This will cause your ui tests to fail unless you handle it with `waitForExistence(timeout: TimeInterval)`. This may end the wait in milliseconds if the async task finishes sooner than that, but if somehow, let's say, the network is slow, each method will wait for the response within the timeout.

Understanding the behaviour of the UI test is not easy. If you want to tap somewhere and use the .tap() method, then you need to check whether the element's .isHittable property. The bad thing is that the value can change depending on the iOS version. However, you have no idea why this version is not hittable for a particular element, while it is for newer versions. A common confusion is between the .exist and .isHittable properties. The former indicates that the view exists in the view hierarchy, but not that it is visible to the user. `isHittable` property shows whether the element is tappable or not. If the view's `isHittable` property returns false, but you are sure it is there and can be, you can select the coordinate of the element with `coordinate(withNormalisedOffset` and tap on it. This will not fail even if there is nothing there. 

There are also environmental difficulties, such as using the keyboard. If you are actively using the simulator and have previously typed something on the physical keyboard, the simulator keyboard is dismissed. This causes a problem when you type in the UI tests. Because the keyboard is hidden until you toggle it, your test will fail.

Finally, writing UI tests is fun until you cannot figure out how to do something you want to do :) the rest is up to your search skills. It is useful to check that your UI responds to user actions as expected, helps you find out if there is anything wrong, and also removes the developer's bias. Although there is a bit of a learning curve at first, it is then very straightforward. Xcode's test recording feature is also very helpful in this regard. On the other hand, it is slow, much slower than unit testing if you are used to it. There are also some stability issues. Sometimes the connection to the simulator is lost while testing or recording a test. Writing UI tests for everything may not be good idea. You should find a good balance between your resources and the views you want to test.