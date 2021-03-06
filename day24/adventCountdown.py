#!/usr/bin/python3

import RPi.GPIO as GPIO
import time
import subprocess

GPIO.setmode(GPIO.BCM)

SERVO = 4

GPIO.setup(SERVO, GPIO.OUT)
pwm = GPIO.PWM(SERVO, 50)
pwm.start(0)

localDate = time.localtime()
month = localDate.tm_mon
pwm_dc = (month / 12 * 10) + 2.5
pwm.ChangeDutyCycle(pwm_dc)
time.sleep(0.5)
pwm.ChangeDutyCycle(0)

if month < 4:
    subprocess.Popen(["omxplayer", "-o", "hdmi", "assets/lied1.mp3"])
elif month < 7:
    subprocess.Popen(["omxplayer", "-o", "hdmi", "assets/lied2.mp3"])
elif month < 10:
    subprocess.Popen(["omxplayer", "-o", "hdmi", "assets/lied3.mp3"])
elif month < 12:
    subprocess.Popen(["omxplayer", "-o", "hdmi", "assets/lied4.mp3"])
else:
    subprocess.Popen(["omxplayer", "-o", "hdmi", "assets/lied5.mp3"])

pwm.stop()
GPIO.cleanup()
