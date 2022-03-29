import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.OUT)

LED = GPIO.PWM(4, 0)

LED.start()

pause_time = 0.5

try:
    while True:
        for i in range(0,101):
            LED.ChangeDutyCycle(i)
        for y in range(101,1):
            LED.ChangeDutyCycle(y)
except KeyboardInterrupt:
    LED.stop()
    GPIO.cleanup()