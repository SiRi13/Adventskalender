#!/usr/bin/python3

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.OUT)
GPIO.output(4, 1)

for i in range(1, 6):# 5 seconds
	print("{} sec".format(i))
	time.sleep(1.0) 

GPIO.cleanup()
