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

try:
    while True:
        while GPIO.input(CLAY) != 0:
            pass
        while GPIO.input(CLAY) == 0:
            GPIO.outpu(GREEN, 1)
            time.sleep(0.01)
            GPIO.outpu(GREEN, 0)
            time.sleep(0.01)
            GPIO.outpu(YELLOW, 1)
            time.sleep(0.01)
            GPIO.outpu(YELLOW, 0)
            time.sleep(0.01)
            GPIO.outpu(RED, 1)
            time.sleep(0.01)
            GPIO.outpu(RED, 0)
            time.sleep(0.01)
        
        randOut = random.randint(5, 7)
        GPIO.output(randOut, 1)

except KeyboardInterrupt:
    GPIO.cleanup()
