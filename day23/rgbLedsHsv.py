#!/usr/bin/python3

import RPi.GPIO as GPIO
import time
import colorsys

LED1 = [17, 27, 22]
LED2 = [10, 9, 11]
LED3 = [5, 6, 13]

pwm_dc1 = [0, 0, 0]
pwm_dc2 = [0, 0, 0]
pwm_dc3 = [0, 0, 0]

GPIO.setmode(GPIO.BCM)

for i in range(3):
    GPIO.setup(LED1[i], GPIO.OUT)
    GPIO.setup(LED2[i], GPIO.OUT)
    GPIO.setup(LED3[i], GPIO.OUT)

for i in range(3):
    pwm_dc1[i] = GPIO.PWM(LED1[i], 50)
    pwm_dc1[i].start(0)
    pwm_dc2[i] = GPIO.PWM(LED2[i], 50)
    pwm_dc2[i].start(0)
    pwm_dc3[i] = GPIO.PWM(LED3[i], 50)
    pwm_dc3[i].start(0)

try:
    while True:
        for i in range(100):
            h = i
            rgb1 = colorsys.hsv_to_rgb(h/100, 1, 1)
            h += 20
            if h > 100:
                h -= 100
            rgb2 = colorsys.hsv_to_rgb(h/100, 1, 1)
            h += 40
            if h > 100:
                h -= 100
            rgb3 = colorsys.hls_to_rgb(h/100, 1, 1)

            for j in range(3):
                pwm_dc1[j].ChangeDutyCycle(rgb1[j])
                pwm_dc2[j].ChangeDutyCycle(rgb2[j])
                pwm_dc3[j].ChangeDutyCycle(rgb3[j])

            time.sleep(0.1)

except KeyboardInterrupt:
    for i in range(3):
        pwm_dc1[i].stop()
        pwm_dc2[i].stop()
        pwm_dc3[i].stop()
    GPIO.cleanup()
