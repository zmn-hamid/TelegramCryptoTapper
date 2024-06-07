from main import do_a_set_of_tapping, take_screenshot, ocr, find_remaining
from config import (
    SCREENSHOT_PATH,
    COOLDOWN_TIME,
    MAXIMUM_TIME_RUNNING,
    COOLDOWN_TAPS_LEFT,
    TAP_WEIGHT,
)
import time, random
from datetime import datetime, timedelta

END_AT = datetime.now() + timedelta(seconds=MAXIMUM_TIME_RUNNING)
MAX_CHUNK_SIZE = 500


def time_exceeded():
    return datetime.now() >= END_AT


def handled_remaining():
    for _ in range(3):
        remaining = int(find_remaining(ocr(take_screenshot(SCREENSHOT_PATH))))
        if remaining == None:
            time.sleep(1)
            continue
        else:
            return remaining
    else:
        raise Exception("cant find remaining")


# do tapping until finished
time_before_operation = time.time()
while not time_exceeded():
    for idx in range(3):
        number_of_taps = int(handled_remaining() / TAP_WEIGHT)
    print(f"tapping at {datetime.now()}...")
    while True:
        # do tapping
        chunks = [MAX_CHUNK_SIZE] * (number_of_taps // MAX_CHUNK_SIZE) + (
            [number_of_taps % MAX_CHUNK_SIZE] if number_of_taps % MAX_CHUNK_SIZE else []
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
