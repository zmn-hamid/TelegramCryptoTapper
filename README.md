# Telegram Crypto Bot Auto Tapper

to be used in Telegram crypto minings apps that work by tapping.
originally made for TapSwap bot, but can be used with other bots as well I guess.

UPDATE: In this version everything is flawless and app will use ocr to find out when to tap and when to cooldown.
you can use the whenever you want

# How to use

- install python
- install scrcpy
- add adb to path (the folder of scrcpy)
- verify you can execute events
    `adb shell input keyevent A` (types "a")
- run the app

# Configuration

change it according to your situation
to test the tap location, run `adb shell input keyevent X Y` and replace X Y with your numbers
you can find the exact coordinate using "show pointer location" in developer options of your phone

You can calculate the cooldown time automatically using the given script but it's generally prefered that you 
calculate it yourself. either way, change it accordingly in config

# Copyright

**Free for personal usage**. Credit me for other usages: my name + the url to my github (or simply the word "github")