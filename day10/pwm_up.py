#!/usr/bin/python3

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

LED = 4

GPIO.setup(LED, GPIO.OUT)

pwm_dc = 0
pwm = GPIO.PWM(LED, 50)  # init PWM with 50Hz
pwm.start(pwm_dc)

while pwm_dc < 100:
    pwm_dc += 5
    pwm.ChangeDutyCycle(pwm_dc)
    time.sleep(0.1)

pwm.stop()
GPIO.cleanup()
