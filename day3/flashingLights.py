#!/usr/bin/python3

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

for i in range(10):
    GPIO.output(17, 1)
    GPIO.output(18, 0)
    time.sleep(0.5)
    GPIO.output(17, 0)
    GPIO.output(18, 1)
    time.sleep(0.5)

GPIO.cleanup()
