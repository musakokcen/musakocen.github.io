---
layout: blogpost
tags: [writes]
title: "How do we implement unit tests? — Unit test practices"
subtitle: ""
---

![Photo byRich TervetonUnsplash](/assets/2021-06-25/1_QScIQuXWdtL9OMQapxBt3w.jpg)

We started to write unit tests in PlusMinusOne last year. Since we added the first tests to our codebase, we learned a lot and improved & refactored our tests. There are several practices & cases that we were not very familiar with before we started to write tests.

To better introduce our practices, I would like to mention our app development and unit testing approach. We developed three projects from scratch for the time being, and we used VIPER architecture in these projects. It has advantages also for writing unit tests. We create mocks for view, interactor, and router. Then, we write tests for the presenter’s protocol methods.

We do not aim to increase our code coverage to %100, but rather we consider code coverage in terms of modules. We aim to write tests for each new module that we add to our codebase. We write tests for each protocol method in the presenter layer. Therefore, the tested module never becomes %100 covered.

Initially, we started to write tests for uncomplicated modules and applied some simple practices. Our setup and some tests looked like this;

## Handling Async Methods

![](/assets/2021-06-25/1__wU31XmlCJEu6pDr9TD19A.png)

We never use `XCTAssert`alone but usually use `XCTAssertFalse`, `XCTAssertTrue`, `XCTAssertEqual`, and `XCTAssertNil` instead. There is a small difference between these functions and XCTAssert. XCTAssert requires adding comparisons in parentheses, but others do not require that;

![](/assets/2021-06-25/1_Bim2_14y2nKzSNdaMTcHPg.png)

## Using Mock Data

Sometimes, we need to pass the data that we fetch from the network manager to call some methods. We do not test network operations but the functions that we handle network request output. Therefore, we need to use mock data. We create JSON files based on our backend documentation and do tests by using them. We created a helper function to load JSON files. It returns a completion.

![](/assets/2021-06-25/1_zNw7qexYAea_A8kLy3DQ5w.png)

## Unwrapping Optionals

We need to unwrap the data and ensure that the error is nil before we test our methods. We also write a separate test for the failure cases.

We handle optionals by using `XCTUnwrap`.

```
XCTAssertNil(error)let solution = try XCTUnwrap(entityDataResponse)
```

We check error case by `XCTAssertNil` but **we do not use;**

```
XCTAssertNotNil(entityDataResponse!)
```

If we check “entityDataResponse” variable with the method above, it will not only fail but also crash if the data is nil.

![](/assets/2021-06-25/1_L_52bUj3njZSEa19RW8ixw.png)

Therefore, we need to use “XCTUnwrap” to make sure we can unwrap the data or not. If it fails, “print” function is not called.

![](/assets/2021-06-25/1_odY8IzRFoR55kQv5SaMveA.png)

If try-catch is used in a method, it should be a **throwing** method. Thus, the test method finally looks like this;

![](/assets/2021-06-25/1_ReCjC0IDJ5l1Rz0zYCovFg.png)

## Different use cases of setup functions

Similar to the methods that take data in their parameters, we have some modules that we initialize with dependency injection. Initially, we were using a similar process in `override func setupWithError() throws`. It was similar to this;

![](/assets/2021-06-25/1_CHAdMqHjr6Rt_61CqrO0ww.png)

Later on, we noticed that this is an expensive way to handle mock data in setup because it is called ever-time before a new test is run, and it increases the total time of the tests performed. Then, we decided to load data in **override class func setUp()**. The difference between **setup** and **class setup** is that the former one is called before every new test function, the latter is called only once when you run tests. There is one more difference between setup() and class setup(); it is the use of async methods. **Expectation** cannot be used in class functions, instead, **DispatchSemaphore** can be used. Our refactored **setup**looked like this in the end;

![](/assets/2021-06-25/1_EjrkqVS_S1QXARbjPe1UTQ.png)

Finally, let’s have a look at how we write a test for this class. Usually, dynamic values are not used in tests. We use random values among an array to test the related method instead. It saves us from tests pass with wrong logic in the presenter because of unexpectedly matching values.

![](/assets/2021-06-25/1_wpFusofVScCJto9-UUvfzg.png)

You can access the source code over [Github](https://gist.github.com/musatrtr/85fca7d2c3f5b54aff820fb25444838c)

## Wrapping Up

I shared our unit testing practices. We are still learning and refactoring our tests. If you have any questions or suggestions, we encourage you to comment below.

To learn more about our development experiences, you can have look at our [medium page](https://medium.com/plus-minus-one). At [Plus Minus One](https://www.plusminusone.co/), we love to learn and share our experiences. We hope this article makes your life easier 🙏🏻

[Musa Kökçen - Turkey | Professional Profile | LinkedIn](https://www.linkedin.com/in/musakokcen/)
