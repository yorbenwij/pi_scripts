from turtle import delay
import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
try:
    while True:
        GPIO.output(4,1)
        time.sleep(0.5)
        GPIO.output(17,1)
        time.sleep(0.5)
        GPIO.output(27,1)
        time.sleep(0.5)
        GPIO.output(22,1)
        time.sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()