# Purpose

to be used in Telegram crypto minings apps that work with tapping.
originally made for TapSwap bot, but can be used with other bots as well I guess.
this tutorial needs programming knowledge

# How to use

1. install scrcpy
2. add adb to path (the folder of scrcpy)
3. verify you can execute events
    `adb shell input keyevent A` (types "a")
    if failed, check scrcpy's faq
    one of the solutions: allow security debugging then restart
4. run the app

# Configuration

change it according to your situation
to test where it taps, run `adb shell input keyevent X Y` and replace X Y with those numbers
you can find the exact coordinate using "show pointer location" in developer options of your phone

# Copyright

**Free for personal usage**. Credit me for other usages: my name + the url to my github (or simply the word "github")