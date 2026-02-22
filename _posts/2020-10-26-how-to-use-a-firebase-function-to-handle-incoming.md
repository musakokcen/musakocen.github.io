---
layout: blogpost
tags: [writes]
title: "How to use a Firebase Function to handle incoming Webhook"
subtitle: ""
---

![](/assets/2020-10-26-how-to-use-a-firebase-function-to-handle-incoming/1*0JU88ckN5gaGcBqz8LFvXw.png)

In this article, we will explain how to create a **Firebase function** and use it as a **callback** **url**. This function will serve as a backend service, when it is triggered, it will interpret incoming **post data**andaccordingly will send a push notification to a specific user.

### **Prerequisite**:

- Firebase Push Notification service should be configured for your project. (If you need help with this subject you can have a look at [this article](/2020/10/26/configure-firebase-push-notification/))
- Firebase Realtime Database should be configured for your project.
- Upgrading our Firebase app to Blaze plan

In order to use Firebase Functions, Google tells us that we have to upgrade our account to **Blaze** **plan**. **Cloud Functions** and **Realtime Database** are free until you reach a certain usage limits. You can see pricing [here](https://firebase.google.com/pricing). The limits look too much to exceed but it is a bit tricky. On August 17, 2020, Google changed Container registry pricing. So you may pay some tiny amount. **(e.g. $0.026)**

![https://firebase.google.com/support/faq#expandable-10](/assets/2020-10-26-how-to-use-a-firebase-function-to-handle-incoming/1*5AmtZle1TiZUvVUefDtiaQ.png)

You can check related Stack Overflow links below.

[Is Function Cloud in Firebase Free or Not (Cloud Functions deployment requires the pay-as-you-go…](https://stackoverflow.com/questions/62824043/is-function-cloud-in-firebase-free-or-not-cloud-functions-deployment-requires-t)

[Firebase storage artifacts](https://stackoverflow.com/questions/63578581/firebase-storage-artifacts)

### **Case:**

We use a third party API for our business. It sends a webhook to inform us about result of the operation. The webhook includes a multiform data. We parse **operation ID**and **success info** from the JSON in it, then, send a push notification to the owner of the operation.

There are three main issues here;

- Storing **operation ID** and the owner’s **push token**
- Receiving webhook
- Parsing webhook and sending push notification

### **Story:**

Let’s say the user presses a button and the app makes an API call. At that moment, the **operation ID** is saved together with the user’s **push token** in order to find the owner of the operation ID that we receive in the webhook.

## **Get Started**

We store the **operation ID** and **push token***, in the completion of the API call.

*You can access **fcmToken** in AppDelegate

![#Swift](/assets/2020-10-26-how-to-use-a-firebase-function-to-handle-incoming/1*4zEHIe43Sjby6BYAsDXFkQ.png)

We saved the **operation ID** and the user’s **push token** to the database, under “**TransferData**” object.

## **Create Cloud Function**

We first need to enable Functions in our Firebase project.

```
Firebase -> Functions -> Get Started
```

![](/assets/2020-10-26-how-to-use-a-firebase-function-to-handle-incoming/1*7Gaxwi3pxsFYlkHoHc3qvA.png)

We open **Terminal** and specify the location that we want to install Node.js (functions are written in Node.js).

```
// example: cd Desktop/MyFunctions
```

```
npm install -g firebase-tools
```

![](/assets/2020-10-26-how-to-use-a-firebase-function-to-handle-incoming/1*EQKuF7FWevTJEmW09ePfcA.png)

If this is the first time that you install Node.js , probably you will get some errors. If so, proceed to[**this page**](https://docs.npmjs.com/resolving-eacces-permissions-errors-when-installing-packages-globally)**.**

![](/assets/2020-10-26-how-to-use-a-firebase-function-to-handle-incoming/1*qmqVOS8VR6yQJaf61HHYVQ.png)

Follow the instructions and make sure you successfully complete this step.

Still in **terminal**, run;

```
firebase init
```

If you face any issue in this step, try this command;

```
curl -sL  https://firebase.tools | bash
```

Then,

```
firebase init
```

The API that we use sends webhook with a multiform data. Therefore, we also need to install Busboy. This library parses multiform data.

```
npm install busboy
```

> **here is a small tip on .gitignore**

> We did not want to have separate projects for our app and functions. Therefore, we created functions folder in our app’s folder. So that, we can access it when we clone or pull the project. However, the default .gitignore file in the functions is not enough in this case. We added node_modules folder (which is created by firebase) to the main .**gitignore file**as**functions/node_modules**

![](/assets/2020-10-26-how-to-use-a-firebase-function-to-handle-incoming/1*-_skfxFnBz5SNRq0lpVBUA.png)

![](/assets/2020-10-26-how-to-use-a-firebase-function-to-handle-incoming/1*n82zm73TnrWJNHqo0yyk8A.png)

## Let’s start developing our function — in Index.js

Now, everything is ready. We only need to write our functions and deploy them to Firebase. The functions are written in **Index.js** file. We open this file. (You can either use JavaScript or TypeScript, we chose JavaScript)

- Let’s first import **busboy**. On the top of the file;

```
const Busboy = require('busboy');
```

Let’s give a name to our function. This name will be also included in the url. You should give a proper name if it is going to be a public url.

- Change the default name after “export”;

```
export.dataTransferResult
```

- The function is now named “**dataTransferResult**”. We want it to be triggered when we receive a webhook. Therefore, we write;

![](/assets/2020-10-26-how-to-use-a-firebase-function-to-handle-incoming/1*TfbatvHqmQFYsr2eokG38w.png)

When we deploy this function to Firebase, it will have a url. We will assign it as our callback url. The API will send webhook and this function will be triggered on request.

We receive multiform data, so that we need to parse it;

```
const busboy = new Busboy({ headers: request.headers });
```

Then, we look for the field that we need and parse it;

![](/assets/2020-10-26-how-to-use-a-firebase-function-to-handle-incoming/1*ZxHVq7z88jiEiW0OE2Nr9A.png)

Once a webhook is sent, **dataTransferResult** function is called. Then, we parse the data and get the **ID** and the **success info**. Now, we need to find the user who sent this data and send him/her a push notification with the result.

We get the ID for the operation in the webhook. We need to find that ID in the database and then find the push token that the ID is belong to.

![](/assets/2020-10-26-how-to-use-a-firebase-function-to-handle-incoming/1*5X4a9WZKCPxIBuxB2E_gwA.png)

We stored the push token as a key under “**TransferData/id**”. Above code gives us a snapshot for a specific ID. We will parse that snapshot and get the push token.

![](/assets/2020-10-26-how-to-use-a-firebase-function-to-handle-incoming/1*wbBtJzVqyq5HctgtjC2EyQ.png)

We parsed the snapshot and got the token. Let’s send a push notification to the user with that token;

![](/assets/2020-10-26-how-to-use-a-firebase-function-to-handle-incoming/1_-PJLqpXk0fGUPVD1VRY5tw.png)

Final look should be like this;

![](/assets/2020-10-26-how-to-use-a-firebase-function-to-handle-incoming/1_Cf0HKN4qcLo9T1sVYhy0eQ.png)

If everything is fine so far, save the file, open terminal, and deploy it to Firebase;

```
firebase deploy
```

If you have multiple projects in Firebase, you can switch between them and deploy each one by using the project id, which is found under Firebase -> Project Overview -> Project Settings.

```
firebase use <project_id>firebase deploy
```

That’s all.

From now on when the API is called in the app, it will send a webhook to the given url, which means that it will trigger the firebase function. After that, our firebase function will send a push notification to the user about the result of the operation.

To learn more about our development experiences, you can have look at our [medium page](https://medium.com/plus-minus-one). At [Plus Minus One](https://www.plusminusone.co/), we love to learn and share our experiences. We hope this article makes your life easier 🙏🏻

[Musa Kökçen — Turkey | Professional Profile | LinkedIn](https://www.linkedin.com/in/musakokcen/)
