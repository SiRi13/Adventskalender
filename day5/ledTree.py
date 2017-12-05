#!/usr/bin/python3

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

RED1 = 17
GREEN1 = 18
RED2 = 19

PUSHBUTTON = 24

# set pins as output
GPIO.setup(RED1, GPIO.OUT)
GPIO.setup(GREEN1, GPIO.OUT)
GPIO.setup(RED2, GPIO.OUT)

# set pin 24 as input with pull down resistor
GPIO.setup(PUSHBUTTON, GPIO.IN, GPIO.PUD_DOWN)

try:
    while True:
        if GPIO.input(PUSHBUTTON) == True:
            GPIO.output(RED1, 1)
            GPIO.output(GREEN1, 0)
            GPIO.output(RED2, 1)
        else:
            GPIO.output(RED1, 0)
            GPIO.output(GREEN1, 1)
            GPIO.output(RED2, 0)

except KeyboardInterrupt:
    GPIO.cleanup()
