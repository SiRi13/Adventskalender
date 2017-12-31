#!/usr/bin/python3

import RPi.GPIO as GPIO
import time

RED = 5
YELLOW = 6
GREEN = 7

LED = [RED, YELLOW, GREEN]

CLAY1 = 8
CLAY2 = 9

GPIO.setmode(GPIO.BCM)
GPIO.setup(CLAY1, GPIO.IN)
GPIO.setup(CLAY2, GPIO.IN)

for l in LED:
    GPIO.setup(l, GPIO.OUT)

try:
    while True:
        while GPIO.input(CLAY1) == False:
            for l in LED:
                GPIO.output(l, True)
                time.sleep(0.1)
                GPIO.output(l, False)

        while GPIO.input(CLAY2) == False:
            for l in LED:
                GPIO.output(l, True)
            time.sleep(0.1)
            for l in LED:
                GPIO.output(l, False)
            time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()
