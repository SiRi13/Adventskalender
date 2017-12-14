#!/bin/usr/python3

import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BCM)

CLAY    = 4
GREEN   = 5
YELLOW  = 6
RED     = 7

GPIO.setup(CLAY, GPIO.IN)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(YELLOW, GPIO.OUT)
GPIO.setup(RED, GPIO.OUT)

GPIO.output(GREEN, 0)
GPIO.output(YELLOW, 0)
GPIO.output(RED, 0)

try:
    while True:
        while GPIO.input(CLAY) != 1:
            pass
        while GPIO.input(CLAY) != 0:
            GPIO.output(GREEN, 1)
            time.sleep(0.01)
            GPIO.output(GREEN, 0)
            time.sleep(0.01)
            GPIO.output(YELLOW, 1)
            time.sleep(0.01)
            GPIO.output(YELLOW, 0)
            time.sleep(0.01)
            GPIO.output(RED, 1)
            time.sleep(0.01)
            GPIO.output(RED, 0)
            time.sleep(0.01)
        
        randOut = random.randint(5, 7)
        GPIO.output(randOut, 1)

except KeyboardInterrupt:
    GPIO.cleanup()
