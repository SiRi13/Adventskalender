#!/usr/bin/python

from gpiozero import LED
from time import sleep

red = LED(17)
green = LED(18)

green.on()
red.off()

while True:
    green.on()
    red.off()
    sleep(0.5)
    green.off()
    red.on()
    sleep(0.5)
