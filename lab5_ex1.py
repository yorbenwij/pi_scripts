import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.bcm)

try:
    while True:
        GPIO.setup(24, GPIO.OUT)
        GPIO.output(24, 1)
        time.sleep(0.5)
        GPIO.output(24, 1)
        time.sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()

