import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.OUT)

LED = GPIO.PWM(4, 100)

LED.start(0)

pause_time = 0.5

try:
    while True:
        for i in range(0,101):
            LED.ChangeDutyCycle(i)
            time.sleep(pause_time)
        for y in range(101,1):
            LED.ChangeDutyCycle(y)
            time.sleep(pause_time)
except KeyboardInterrupt:
    LED.stop()
    GPIO.cleanup()