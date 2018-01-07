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

pwm_dc = 5
delta = 2
pwm = GPIO.PWM(SERVO, 50)
pwm.start(pwm_dc)

for i in LED[0]:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, False)

try:
    reverse = False
    while True:
        pwm.ChangeDutyCycle(pwm_dc)
        pwm_dc += delta
        if pwm_dc >= 9 or pwm_dc <= 5:
            delta *= -1 
        time.sleep(0.2)
        pwm.ChangeDutyCycle(0)
        
        for i in LED[reverse]:
            GPIO.output(i, True)
            time.sleep(0.2)
            GPIO.output(i, False)
            if GPIO.input(BUTTON) == True:
                reverse = not reverse

except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()
