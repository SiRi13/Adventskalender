#!/usr/bin/python3

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

SERVO = 4
DOWN = 5
UP = 6

GPIO.setup(DOWN, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(UP, GPIO.IN, GPIO.PUD_DOWN)

pwm_dc = 7.5
pwm_freq = 50
GPIO.setup(SERVO, GPIO.OUT)
pwm = GPIO.PWM(SERVO, pwm_freq)

pwm.start(pwm_dc)

try:
    while True:
        if GPIO.input(UP) and pwm_dc < 12.5:
            pwm_dc += 2.5
            pwm.ChangeDutyCycle(pwm_dc)
            time.sleep(0.5)
            pwm.ChangeDutyCycle(0)

        if GPIO.input(DOWN) and pwm_dc > 2.5:
            pwm_dc -= 2.5
            pwm.ChangeDutyCycle(pwm_dc)
            time.sleep(0.5)
            pwm.ChangeDutyCycle(0)

except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()
