# -*- coding: utf-8 -*-

# import RPi.GPIO as GPIO
import time

from flask import Flask, jsonify, render_template, request
app = Flask(__name__)

r1 = r2 = 0.0
g1 = g2 = 0.0
b1 = b2 = 0.0

@app.route('/_day16')
def day16():
    global r1, r2, g1, g2, b1, b2
    r1 = request.args.get('red1', 0, type=float)
    r2 = request.args.get('red2', 0, type=float)
    g1 = request.args.get('green1', 0, type=float)
    g2 = request.args.get('green2', 0, type=float)
    b1 = request.args.get('blue1', 0, type=float)
    b2 = request.args.get('blue2', 0, type=float)

    return jsonify(result="Values set to:\n{}, {},\n{}, {},\n{}, {}".format(r1, r2, g1, g2, b1, b2))

@app.route("/")
def index():
    return render_template('index.html')



if __name__ == '__main__':
    app.run()
