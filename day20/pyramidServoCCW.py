#!/usr/bin/python3

import RPi.GPIO as GPIO
import time

SERVO = 4
pwm_dc = 12.5

GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO, GPIO.OUT)
pwm = GPIO.PWM(SERVO, 50)

pwm.start(pwm_dc)
time.sleep(0.5)
pwm.ChangeDutyCycle(0)
pwm.stop()
GPIO.cleanup()
