#!/usr/bin/python3

from gpiozero import LED
from time import sleep

led = LED(4)
while True:
	led.on()
	sleep(0.5)
	led.off()
	sleep(0.5)
