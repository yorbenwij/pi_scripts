import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

while True:
        GPIO.setup(24, GPIO.OUT)
        GPIO.setup(23, GPIO.OUT)
        GPIO.setup(14, GPIO.OUT)
        GPIO.setup(15, GPIO.OUT)

        GPIO.output(24, 1)
        GPIO.output(23, 1)
        GPIO.output(15, 1)
        GPIO.output(14, 1)
        time.sleep(0.1)
        GPIO.output(24, 0)
        GPIO.output(23, 0)
        GPIO.output(15, 0)
        GPIO.output(14, 0)
        time.sleep(0.1)