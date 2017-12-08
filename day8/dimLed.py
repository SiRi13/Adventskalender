#!/usr/bin/python3

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

LED = 4
UP = 8
DOWN = 7

GPIO.setup(LED, GPIO.OUT)
GPIO.setup(UP, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(DOWN, GPIO.IN, GPIO.PUD_DOWN)

pwm = GPIO.PWM(LED, 50) # init pwm with 100Hz
pwm_dc = 0 
pwm.start(pwm_dc)

try:
    while True:
        if GPIO.input(UP) == True and pwm_dc < 100:
            pwm_dc += 10
        
        if GPIO.input(DOWN) == True and pwm_dc > 0:
            pwm_dc -= 10

        pwm.ChangeDutyCycle(pwm_dc)

except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()
