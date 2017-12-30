#!/usr/bin/python3

import RPi.GPIO as GPIO
import time

RED = 5
YELLOW = 6
GREEN = 7
LED = [RED, YELLOW, GREEN]

GPIO.setmode(GPIO.BCM)

for l in LED:
    GPIO.setup(l, GPIO.OUT)

for i in range(3):
    for l in LED:
        GPIO.output(l, True)
    time.sleep(0.2)
    for l in LED:
        GPIO.output(l, False)
    time.sleep(0.2)

GPIO.cleanup()
