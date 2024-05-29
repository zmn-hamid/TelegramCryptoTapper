# Telegram Crypto Bot Auto Tapper

To be used in Telegram crypto minings apps that work by tapping.
Originally made for TapSwap bot.

UPDATE: In this version everything is flawless and app will use ocr to find out when to tap and when to cooldown.
You can use the bot whenever you want. It has a minor anti-spam built-in function as well.

# How to use

- Install python
- Install scrcpy
- Add ADB to path (the folder of scrcpy)
- Verify you can execute events
    `adb shell input keyevent A` (types "a")
- Run the app `python app.py`

# Configuration

change it according to your situation
to test the tap location, run `adb shell input keyevent X Y` and replace X Y with your numbers
you can find the exact coordinate using "show pointer location" in developer options of your phone

# Copyright

**Free for personal usage**. Credit me for other usages: my name + the url to my github (or simply the word "github")