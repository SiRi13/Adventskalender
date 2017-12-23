# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import threading
import time

from flask import Flask, jsonify, render_template, request
app = Flask(__name__)

RED1, GREEN1, BLUE1 = 7, 5, 6
RED2, GREEN2, BLUE2 = 10, 7, 8

r1, g1, b1 = 0, 0, 0
r1t, g1t, b1t = 0, 0, 0

r2, g2, b2 = 0, 0, 0
r2t, g2t, b2t = 0, 0, 0

@app.route('/day16/red1', methods=['POST'])
def red1():
    global r1, r1t

    r1 = request.form.get('red1', 0, type=int)
    r1t = request.form.get('red1time', 0, type=int)

    return jsonify(result='red1 set')

@app.route('/day16/red2', methods=['POST'])
def red2():
    global r2, r2t

    r2 = request.form.get('red2', 0, type=int)
    r2t = request.form.get('red2time', 0, type=int)

    return jsonify(result="red2 set")

@app.route('/day16/green1', methods=['POST'])
    global g1, g1t

    g1 = request.form.get('green1', 0, type=int)
    g1t = request.form.get('green1time', 0, type=int)

    return jsonify(result="green1 set")

@app.route('/day16/green2', methods=['POST'])
    global g2, g2t

    g2 = request.form.get('green2', 0, type=int)
    g2t = request.form.get('green2time', 0, type=int)
    
    return jsonify(result="green2 set")

@app.route('/day16/blue1', methods=['POST'])
    global b1, b1t

    b1 = request.form.get('blue1', 0, type=int)
    b1t = request.form.get('blue1time', 0, type=int)

    return jsonify(result="blue1 set")

@app.route('/day16/blue2', methods=['POST'])
def day16():
    global b2, b2t

    b2 = request.form.get('blue2', 0, type=int)
    b2t = request.form.get('blue2time', 0, type=int)

    return jsonify(result="blue2 set")

@app.route("/day16")
def index():
    GPIO.setmode(GPIO.BCM)
    threads = []
    for i in [RED1, GREEN1, BLUE1, RED2, GREEN2, BLUE2]:
        t = threading.Thread(target=gpio_thread, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    return render_template('index.html')

def gpio_thread(ledId):
    GPIO.setup(ledId, GPIO.OUT)
    pwm = GPIO.PWM(ledId, 50)
    
    if ledId == RED1:
        pwm.start(r1)
        while True:
            if 0 <= r1 <= 100:
                pwm.ChangeDutyCycle(r1)
            time.sleep(r1t)
        pwm.stop()

    elif ledId == GREEN1:
        pwm.start(g1)
        while True:
            if 0 < g1 < 100:
                pwm.ChangeDutyCycle(g1)
            time.sleep(g1t)
        pwm.stop()
        
    elif ledId == BLUE1:
        pwm.start(b1)
        while True:
            if 0 < b1 < 100:
                pwm.ChangeDutyCycle(b1)
            time.sleep(b1t)
        pwm.stop()
        
    elif ledId == RED2:
        pwm.start(r2)
        while True:
            if 0 < r2 < 100:
                pwm.ChangeDutyCycle(r2)
            time.sleep(r2t)
        pwm.stop()
        
    elif ledId == GREEN2:
        pwm.start(g2)
        while True:
            if 0 < g2 < 100:
                pwm.ChangeDutyCycle(g2)
            time.sleep(g2t)
        pwm.stop()
        
    elif ledId == BLUE2:
        pwm.start(b2)
        while True:
            if 0 < b2 < 100:
                pwm.ChangeDutyCycle(b2)
            time.sleep(b2t)
        pwm.stop()


if __name__ == '__main__':
    app.run()
