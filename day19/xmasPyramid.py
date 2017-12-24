import RPi.GPIO as GPIO
import time
import threading

RED = 5
YELLOW = 6
GREEN = 7
SERVO = 4

LEDs = [RED, YELLOW, GREEN]

GPIO.setmode(GPIO.BCM)

def led_thread():
    GPIO.setup(RED, GPIO.OUT)
    GPIO.setup(YELLOW, GPIO.OUT)
    GPIO.setup(GREEN, GPIO.OUT)

    while True:
        GPIO.output(RED, 0)
        GPIO.output(YELLOW, 0)
        GPIO.output(GREEN, 0)
        for pin in LEDs:
            pwm = GPIO.PWM(pin, 50)
            pwm.start(0)
            for dc in range(10, 100, 10):
                pwm.ChangeDutyCycle(dc)
                time.sleep(0.05)
            for dc in range(100, 10, -10):
                pwm.ChangeDutyCycle(dc)
                time.sleep(0.05)
            pwm.stop()


def servo_thread():
    GPIO.setup(SERVO, GPIO.OUT)
    pwm = GPIO.PWM(SERVO, 50)
    dc_step = 2.5
    pwm_dc = 0.0
    pwm.start(pwm_dc)

    while True:
        pwm.ChangeDutyCycle(pwm_dc)
        pwm_dc += dc_step
        if pwm_dc == 12.5 or pwm_dc == 2.5:
            a = -a
        time.sleep(0.2)
        pwm.ChangeDutyCycle(0.0)

    pwm.stop()


led_t = threading.Thread(target=led_thread)
servo_t = threading.Thread(target=servo_thread)
led_t.start()
servo_t.start()
