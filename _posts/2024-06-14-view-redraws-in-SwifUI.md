---
layout: blogpost
title: Property Updates and View Redraws in SwifUI
subtitle: ""
---

There are many things to discover and discuss as SwiftUI becomes more popular. These days I only write SwiftUI unless others are needed. So I find myself thinking about different topics in terms of how SwiftUI handles them under the hood. One of these topics was about SwiftUI's view updates when a published property is updated. 

Imagine you have a viewModel that conforms to ObservableObject, it has two published properties. Let's say you update these properties one after the other and both are used in the view. So far, so good. If you update both of these properties at the same time, they should be updated with two new sets of data. Then comes the question; does this mean that the view will be drawn twice and maybe even cause flickering? 

I have received different answers and explanations to this question. SwiftUI's evolving mechanism under the hood definitely has an impact on this. So whenever the willSet observer is called, it will call objectWillChange.send inside. The theory is that the view has a viewModel as an ObservedObject and it subscribes to the viewModel's objectWillChange publisher and redraws the view when an event occurs. Having published properties can also be interpreted as having a variable with objectWillChange.send inside its willSet property observer. From this perspective, it sounds like the view should be drawn twice. However, this is not the case. When SwiftUI needs to redraw views, it does not do so immediately upon receiving the event. The updates are batched and done together if there are multiple changes. We can think of this as having a defer statement in each function that updates the properties without the Published attribute. In the defer statement, objectWillSend is called once for all the properties and the view is updated. Therefore, if you change many properties in this function in the same thread, the view will only be redrawn once. Although I could not find any documentation related to this, I would say that this behavior is thread related. If you update multiple properties in the same thread, SwiftUI updates the view with all new values at once. 

We can prove this theory in several ways, one using the [**_princhanges()**]([https://medium.com/@musakokcen](https://developer.apple.com/documentation/swift-playgrounds/console-print-debugging#Understand-when-and-why-your-views-change)) approach, the other using the Instruments tool. Assigning random background colors for testing is also an option, but does not sound like a good practice to me unless you need specific things. Using instruments, you just need to select SwiftUI profiler and watch the count number in the details section for the view body after doing something that changes property values. 

As a result, it is not always easy to figure out how things work under the hood, and you have to use different approaches to make an inference with a proof. As these two approaches show, the view update events are collected and applied all at once whenever possible.

As a result, it is not always easy to figure out how things work under the hood, and you have to use different approaches to make an inference with a proof. As the two recommended approaches show, the view update events are collected and applied all at once whenever possible.
