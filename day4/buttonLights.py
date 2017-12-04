#!/usr/bin/python3

import RPi.GPIO as GPIO
import time

GPIO.set_mode(GPIO.BCM)

GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(24, GPIO.IN, GPIO.PUD_DOWN)

try:
    while True:
        GPIO.output(17, 1)
        GPIO.output(18, 0)
        while not GPIO.input(24):
            time.sleep(0.2)
        GPIO.output(17, 0)
        GPIO.output(18, 1)
        while not GPIO.input(24):
            time.sleep(0.2)

except KeyboardInterrupt:
    GPIO.cleanup()
