#!/usr/bin/python3

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

SERVO = 4
GPIO.setup(SERVO, GPIO.OUT)

PWM_FREQ = 50.0
pwm = GPIO.PWM(SERVO, PWM_FREQ)

pwm_dc = 12.5
pwm.start(pwm_dc)

time.sleep(0.5)
pwm.ChangeDutyCycle(0.0)
pwm.stop()
GPIO.cleanup()
