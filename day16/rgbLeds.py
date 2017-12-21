# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import threading
import time

from flask import Flask, jsonify, render_template, request
app = Flask(__name__)

RED1, GREEN1, BLUE1 = 5, 6, 7
RED2, GREEN2, BLUE2 = 8, 9, 10

r1, g1, b1 = 0.0, 0.0, 0.0
r1t, g1t, b1t = 0.0, 0.0, 0.0

r2, g2, b2 = 0.0, 0.0, 0.0
r2t, g2t, b2t = 0.0, 0.0, 0.0

@app.route('/_day16')
def day16():
    global r1, r2, g1, g2, b1, b2
    global r1t, g1t, b1t
    global r2t, g2t, b2t

    r1 = request.args.get('red1', 0, type=float)
    g1 = request.args.get('green1', 0, type=float)
    b1 = request.args.get('blue1', 0, type=float)
    r1t = request.args.get('red1time', 0, type=float)
    g1t = request.args.get('green1time', 0, type=float)
    b1t = request.args.get('blue1time', 0, type=float)

    r2 = request.args.get('red2', 0, type=float)
    g2 = request.args.get('green2', 0, type=float)
    b2 = request.args.get('blue2', 0, type=float)
    r2t = request.args.get('red2time', 0, type=float)
    g2t = request.args.get('green2time', 0, type=float)
    b2t = request.args.get('blue2time', 0, type=float)

    return jsonify(result=True)

@app.route("/")
def index():
    return render_template('index.html')

def gpio_thread(ledId):
    global r1, r2, g1, g2, b1, b2
    global r1t, r2t, g1t, g2t, b1t, b2t

    if ledId == RED1:
        GPIO.setup(RED1, GPIO.OUT)
        pwm_r1 = GPIO.PWM(RED1, 50)
        pwm_r1.start(r1)
        while True:
            if 0 < r1 < 100:
                pwm_r1.ChangeDutyCycle(r1)
            time.sleep(r1t)

        pwm_r1.stop()
    elif ledId == GREEN1:
        GPIO.setup(GREEN1, GPIO.OUT)
        pwm_g1 = GPIO.PWM(GREEN1, 50)
        pwm_g1.start(g1)
        while True:
            if 0 < g1 < 100:
                pwm_g1.ChangeDutyCycle(g1)
            time.sleep(g1t)
        pwm_g1.stop()
    elif ledId == BLUE1:
        GPIO.setup(BLUE1, GPIO.OUT)
        pwm_b1 = GPIO.PWM(BLUE1, 50)
        pwm_b1.start(b1)
        while True:
            if 0 < b1 < 100:
                pwm_b1.ChangeDutyCycle(b1)
            time.sleep(b1t)
        pwm_b1.stop()
    elif ledId == RED2:
        GPIO.setup(RED2, GPIO.OUT)
        pwm_r2 = GPIO.PWM(RED2, 50)
        pwm_r2.start(r2)
        while True:
            if 0 < r2 < 100:
                pwm_r2.ChangeDutyCycle(r2)
            time.sleep(r2t)
        pwm_r2.stop()
    elif ledId == GREEN2:
        GPIO.setup(GREEN2, GPIO.OUT)
        pwm_g2 = GPIO.PWM(GREEN2, 50)
        pwm_g2.start(g2)
        while True:
            if 0 < g2 < 100:
                pwm_g2.ChangeDutyCycle(g2)
            time.sleep(g2t)
        pwm_g2.stop()
    elif ledId == BLUE2:
        GPIO.setup(BLUE2, GPIO.OUT)
        pwm_b2 = GPIO.PWM(BLUE2, 50)
        pwm_b2.start(b2)
        while True:
            if 0 < b2 < 100:
                pwm_b2.ChangeDutyCycle(b2)
            time.sleep(b2t)
        pwm_b2.stop()


if __name__ == '__main__':
    app.run()

    GPIO.setmode(GPIO.BCM)
    threads = []
    for i in [RED1, GREEN1, BLUE1]:
        t = threading.Thread(target=gpio_thread, args=(i,))
        threads.append(t)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
