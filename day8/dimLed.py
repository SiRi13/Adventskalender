#!/usr/bin/python3

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

LED = 4
UP = 8
DOWN = 7

GPIO.setup(LED, GPIO.OUT)
GPIO.setup(UP, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(DOWN, GPIO.IN, GPIO.PUD_DOWN)

pwm = GPIO.PWM(LED, 500)
pwm_dc = 0 
pwm.start(pwm_dc)

try:
    while True:
        if GPIO.input(UP) == True and pwm_dc < 100:
            pwm_dc += 5 
            print("Increase pwm_dc by 5 to ", pwm_dc)
        
        if GPIO.input(DOWN) == True and pwm_dc > 0:
            pwm_dc -= 5 
            print("Decrease pwm_dc by 5 to ", pwm_dc)

        # avoid to fast in/decreasing of pwm_dc
        time.sleep(0.5)
        pwm.ChangeDutyCycle(pwm_dc)

except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()
