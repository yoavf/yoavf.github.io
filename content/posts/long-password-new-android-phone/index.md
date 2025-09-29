---
title: 'Tip: typing a long Google password into a new Android device'
slug: long-password-new-android-phone
author: Yoav
date: 2016-10-06T09:32:28+00:00
jabber_published:
  - 1475746350
email_notification:
  - 1475746352
publicize_twitter_user:
  - yoavf
categories:
  - android
tags:
  - adb
  - password
  - tip

---
I use a password manager and create very long passwords where possible, including for my Google account. The problem? when setting up a new Android phone, I can&#8217;t download the password manager app until I&#8217;ve logged into my Google account, which is nearly impossible without the password manager app.

The workaround? Enable USB debugging on the phone, and use [ADB][1] to enter the password:

```bash
./adb shell input text "LONG COMPLICATED PASSWORD"
```

Is it safe enough? Probably not. Use at your own risk 🙂

 [1]: https://developer.android.com/studio/command-line/adb.html