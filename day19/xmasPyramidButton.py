#!/usr/bin/python3

import RPi.GPIO as GPIO
import time

SERVO = 4

RED = 5
YELLOW = 6
GREEN = 7

BUTTON = 8

LED = [[RED, YELLOW, GREEN], [GREEN, YELLOW, RED]]

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(SERVO, GPIO.OUT)

pwm_dc = 2.5
delta = 2.5
pwm = GPIO.PWM(SERVO, 50)
pwm.start(pwm_dc)

for i in LED[0]:
    GPIO.setup(i, GPIO.OUT)

try:
    reverse = False
    while True:
        pwm.ChangeDutyCycle(pwm_dc)
        pwm_dc += delta
        if pwm_dc == 12.5 or pwm_dc == 2.5:
            position = -delta
        time.sleep(0.2)
        pwm.ChangeDutyCycle(0)
        
        for i in LED[reverse]:
            GPIO.setup(i, True)
            time.sleep(0.2)
            GPIO.setup(i, False)
            if GPIO.input(BUTTON) == True:
                x != x

except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()
