import os, time, random
from config import (
    WHERE_TO_TAP,
    REST_BETWEEN_EACH_TAP,
    MAXIMUM_NUMBER_OF_TAPS,
    COOLDOWN_TIME,
    KEEP_SCREEN_ON,
    WHERE_TO_TAP_FOR_WAKING,
    REST_BETWEEN_EACH_WAKE_TAP,
)

TAP_PER_COOLDOWN = MAXIMUM_NUMBER_OF_TAPS / COOLDOWN_TIME
# used for calulating how much taps are available after a set of tapping


def do_tapping(tap_coordinate):
    os.system(f"adb shell input tap {tap_coordinate[0]} {tap_coordinate[1]}")


def do_a_set_of_tapping(number_of_taps: int):
    for _ in range(int(number_of_taps)):
        do_tapping(WHERE_TO_TAP)
        time.sleep(random.uniform(*REST_BETWEEN_EACH_TAP))


counter = 0
while True:
    counter += 1
    print(f"tapping #{counter}...")
    time_before_tapping = time.time()
    number_of_taps_needed = MAXIMUM_NUMBER_OF_TAPS
    while True:
        do_a_set_of_tapping(number_of_taps_needed)
        number_of_taps_refilled = (time.time() - time_before_tapping) * TAP_PER_COOLDOWN
        if number_of_taps_refilled < 5:
            # just cooldown man
            break
        number_of_taps_needed = number_of_taps_refilled

    print("resting...")
    if not KEEP_SCREEN_ON:
        REST_BETWEEN_EACH_TAP = COOLDOWN_TIME  # so it would end before the second rest
    total_time_sleeped = 0
    while True:
        # sleep
        time.sleep(REST_BETWEEN_EACH_WAKE_TAP)
        total_time_sleeped += REST_BETWEEN_EACH_WAKE_TAP
        if total_time_sleeped >= COOLDOWN_TIME:
            break

        # wake up
        do_tapping(WHERE_TO_TAP_FOR_WAKING)
