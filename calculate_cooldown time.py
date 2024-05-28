import time, os
from main import find_remaining, ocr, take_screenshot, do_tapping
from config import WHERE_TO_TAP, SCREENSHOT_PATH, MAXIMUM_NUMBER_OF_TAPS

print("if you can calculate it yourself, its better.")
print("anyways wait a little bit while i'm calculating (takes 10s)...")
for _ in range(int(100)):
    do_tapping(WHERE_TO_TAP)

SECOND_SCREENSHOT_PATH = "2" + SCREENSHOT_PATH

take_screenshot(SCREENSHOT_PATH)
time.sleep(10)
take_screenshot(SECOND_SCREENSHOT_PATH)
speed = (
    find_remaining(ocr(SECOND_SCREENSHOT_PATH))
    - find_remaining(ocr(SCREENSHOT_PATH)) / 10
)
print(f"cooldown time = {MAXIMUM_NUMBER_OF_TAPS / speed}")
print("copy this to config")
os.remove(SECOND_SCREENSHOT_PATH)
