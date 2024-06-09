import os
import random
import re
import time
from datetime import datetime, timedelta

import click
import pytesseract
from PIL import Image

from config import (
    COOLDOWN_TAPS_LEFT,
    COOLDOWN_TIME,
    MAXIMUM_NUMBER_OF_TAPS,
    MAXIMUM_TIME_RUNNING,
    SCREENSHOT_PATH,
    TAP_WEIGHT,
    WHERE_TO_TAP,
)

END_AT = datetime.now() + timedelta(seconds=MAXIMUM_TIME_RUNNING)
MAX_CHUNK_SIZE = 500


def time_exceeded():
    return datetime.now() >= END_AT


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
    all_the_numbers = re.findall(r"\d+", ocr_text)[::-1]
    for idx, number in enumerate(all_the_numbers):
        if int(number) == MAXIMUM_NUMBER_OF_TAPS:
            return int(all_the_numbers[idx + 1])


def handled_remaining():
    for _ in range(5):
        remaining = find_remaining(ocr(take_screenshot(SCREENSHOT_PATH)))
        if remaining == None:
            time.sleep(1.5)
            continue
        else:
            return int(remaining)
    else:
        raise Exception("cant find remaining")


def smart_tap():
    while not time_exceeded():
        number_of_taps = int(handled_remaining() / TAP_WEIGHT)
        print(f"tapping at {datetime.now()}...")
        while True:
            # do tapping
            chunks = [MAX_CHUNK_SIZE] * (number_of_taps // MAX_CHUNK_SIZE) + (
                [number_of_taps % MAX_CHUNK_SIZE]
                if number_of_taps % MAX_CHUNK_SIZE
                else []
            )
            for chunk in chunks:
                do_a_set_of_tapping(chunk)
                if len(chunks) > 1:
                    time.sleep(random.uniform(8, 12))

            # check how much left
            remaining = handled_remaining()

            # check if less than 5 exit
            if remaining < COOLDOWN_TAPS_LEFT:
                break

            # calulate new tapping amount
            number_of_taps = int(remaining / TAP_WEIGHT)
        if time_exceeded():
            break

        # cooldown
        print(f"resting at {datetime.now()}...")
        time.sleep(COOLDOWN_TIME)


def just_tap():
    while True:
        do_tapping(WHERE_TO_TAP)


print("1. smart tap\n2. just tap (continuously with no feature)\n")
choice = click.prompt("choose", type=click.Choice(["1", "2"]))

if choice == "1":
    smart_tap()
else:
    just_tap()
