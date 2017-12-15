#!/usr/bin/python3

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GREEN   = 5
BLUE    = 6
RED     = 7

GPIO.setup(GREEN, GPIO.OUT) 
GPIO.setup(BLUE, GPIO.OUT) 
GPIO.setup(RED, GPIO.OUT) 

GPIO.output(GREEN, 1)
GPIO.output(BLUE, 0)
GPIO.output(RED, 0)

try:
    while True:
        GPIO.output(RED, 1)
        time.sleep(0.2)
        GPIO.output(GREEN, 0)
        time.sleep(0.2)
        GPIO.output(BLUE, 1)
        time.sleep(0.2)
        GPIO.output(RED, 0)
        time.sleep(0.2)
        GPIO.output(GREEN, 1)
        time.sleep(0.2)
        GPIO.output(BLUE, 0)
        time.sleep(0.2)

except KeyboardInterrupt:
    GPIO.cleanup()
