import os
import re
import time

import pytesseract
from PIL import Image

from config import (
    COOLDOWN_TIME,
    MAXIMUM_NUMBER_OF_TAPS,
    WHERE_TO_TAP,
)


def do_tapping(tap_coordinate):
    os.system(f"adb shell input tap {tap_coordinate[0]} {tap_coordinate[1]}")


def do_a_set_of_tapping(number_of_taps: int):
    for _ in range(int(number_of_taps)):
        do_tapping(WHERE_TO_TAP)


def take_screenshot(screenshot_file: str):
    os.system(
        f"adb shell screencap /sdcard/{screenshot_file} && adb pull /sdcard/{screenshot_file}"
    )
    return screenshot_file


def ocr(image_path: str):
    image = Image.open(image_path)
    return pytesseract.image_to_string(image)


def find_remaining(ocr_text: str):
    """returns remaining and total"""
    all_the_numbers = re.findall(r"\d+", ocr_text)
    for idx, number in enumerate(all_the_numbers):
        if int(number) == MAXIMUM_NUMBER_OF_TAPS:
            return int(all_the_numbers[:idx][::-1][0])
