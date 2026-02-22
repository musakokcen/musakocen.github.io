---
layout: blogpost
tags: [writes]
title: "Configure Firebase Push Notification"
subtitle: ""
---

Push notifications is one of the most essential implementations for any mobile app project. It is simple but simple things can sometimes turn out to be a huge issue. We use different push notification services for our projects. However, as part of our [backendless webhook implementation](/2020/10/26/how-to-use-a-firebase-function-to-handle-incoming/), we used Firebase. Therefore, we wanted to explain how to configure Firebase push notification to your project.

Handling certificates is sometimes too confusing. Thanks to [M. Kerem Keskin](https://medium.com/u/c94ebcb80e52), we did not face any issue in this part. He managed the certificates for us and helped us for an easy learning process.

**Configure APNs Certificates**

- *If you have not yet created a Firebase project for your app, firstly, create a project, download GoogleService-Info.plist, and place it in your project as guided over Firebase.*

![image source](/assets/2020-10-26-configure-firebase-push-notification/1_zL6q32KAOrUEBwP5y12Kag.png)

**Step 1: Create a certificate signing request**

- Open “Keychain Access” → Certificate Assistant → Request a Certificate From a Certificate Authority → Enter email address → Check “Saved to disk” → Continue → Specify a location & click “Save”

![](/assets/2020-10-26-configure-firebase-push-notification/1_M8FJ_6z99IWBTJ1_52jM1Q.png)

![](/assets/2020-10-26-configure-firebase-push-notification/1_vLrVMaHiMd-e_O29CjzMRA.png)

Now, you have a certificate signing request in the location that you specified. We will use it to generate a development certificate.

**Step 2: Download development certificate**

- Go to [developer.apple.com](http://developer.apple.com) → Certificates, Identifiers & Profiles → Identifiers → “your app” → Push Notification → Create Certificate → Choose File (choose the development certificate) → Download

![Click on Certificates, Identifiers & Profiles](/assets/2020-10-26-configure-firebase-push-notification/1_OzexYz8xK8m0SCAnJOu8wQ.png)

![Select identifiers and then select the app that you want to add push notification](/assets/2020-10-26-configure-firebase-push-notification/1_RosLe2XLcS14l0oaVNT6zg.png)

![Click on configure/edit, then, create a certificate](/assets/2020-10-26-configure-firebase-push-notification/1_JNlG01dJTp66XLSXu5F1yQ.png)

You can create a certificate for both development and production if you have a separate debug mode. Creating both sandbox and production certificates will save you from trouble in the future.

**Step 3: export .p12 file**

- Double click the certificate that you downloaded
- Then, go to “Keychain Access” → select “my certificates” → find the certificate → right click → “export” → “save”

![](/assets/2020-10-26-configure-firebase-push-notification/1_fFXuOMwxrE-STrLLqI_-Eg.png)

Now, you have a certificate (a .p12 file). We will upload this to Firebase so that we can send push notifications via Firebase.

**Step 4: Upload certificate to Firebase**

- Open Firebase, and go to Project Settings → Cloud Messaging → APNS Certificates → upload the certificate

![Open Project Settings](/assets/2020-10-26-configure-firebase-push-notification/1_d4vCs5couns7Cm9l8IR1GQ.png)

![Select Cloud Messaging](/assets/2020-10-26-configure-firebase-push-notification/1_0uoB3rU5Z-OrqCJG9LBQkg.png)

![Upload your certificate/certificates below APNs Certificates](/assets/2020-10-26-configure-firebase-push-notification/1_CPHo0ErRAtjabBWeHpgG9g.png)

Now, we can send push notification via Firebase. Let’s integrate Firebase messaging into our app for sending push notification to a certain user.

## **Install Dependencies**

Open your Podfile and add the required pod;

```
pod 'Firebase/Messaging'
```

Then, open terminal, add your project’s location, and then run

```
pod install
```

> Note: You should register for remote notifications where it is suitable for your purpose.

> [https://firebase.google.com/docs/cloud-messaging/ios/client#register_for_remote_notifications](https://firebase.google.com/docs/cloud-messaging/ios/client#register_for_remote_notifications)

## **Get push notification token**

Let’s get the push token. We need to use fcmToken (Firebase Cloud Messaging Token) to send push notifications via Firebase Cloud Messaging.

Open **Xcode**, and in **AppDelegate** file;

```
import FirebaseMessaging
```

APNs token should be paired to “**fcmToken”**;

In Firebase Cloud Messaging, swizzling is open by default for pairing fcmToken. If you want to disable swizzling you can check this [link](https://firebase.google.com/docs/cloud-messaging/ios/client#method_swizzling_in).

In order to use **apns token** for other purposes (e.g. to be able to send push notifications also with another 3rd party service), we decided to disable swizzling. In that case, you should obtain deviceToken for pairing with **fcmToken** as below.

in AppDelegate;

![](/assets/2020-10-26-configure-firebase-push-notification/1_J0ZMuX4zWU2NGQUBfNOPOw.png)

in **didFinishLaunchingWithOptions** function;

```
Messaging.messaging().delegate = self
```

Then,

![](/assets/2020-10-26-configure-firebase-push-notification/1_f0AKREmRrL8bR4B5u3quBg.png)

Now, we have fcmToken for a specific user. If we want to send a push notification to him/her, we will use this token.

## Test Push Notification

By using the fcmToken, we can send test push notifications to a certain device as shown below.

![](/assets/2020-10-26-configure-firebase-push-notification/1*9-dtGLOEkZpmoiHXRAzemQ.png)

![](/assets/2020-10-26-configure-firebase-push-notification/1*H79IyfVQpexojjZ-Rc5vRA.png)

To learn more about our development experiences, you can have look at our [medium page](https://medium.com/plus-minus-one). At [Plus Minus One](https://www.plusminusone.co/), we love to learn and share our experiences. We hope this article makes your life easier 🙏🏻

[Musa Kökçen — Turkey | Professional Profile | LinkedIn](https://www.linkedin.com/in/musakokcen/)
