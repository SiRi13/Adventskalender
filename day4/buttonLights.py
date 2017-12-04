#!/usr/bin/python3

import RPi.GPIO as GPIO

GPIO.set_mode(GPIO.BCM)

GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(24, GPIO.IN, GPIO.PUD_DOWN)

while True:
    GPIO.output(17, 1)
    GPIO.output(18, 0)
    while not GPIO.input(24):
        # do nothing
    GPIO.output(17, 0)
    GPIO.output(18, 1)
    while not GPIO.input(24):
        # do nothing

GPIO.cleanup()
