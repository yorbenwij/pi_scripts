#librarys
from operator import truediv
import RPi.GPIO as GPIO
import time


#set pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(7,GPIO.OUT) #trigger pin
GPIO.setup(5,GPIO.IN) #echo pin

try:
    while True:
        GPIO.output(7,1)
        time.sleep(0.00001)
        GPIO.output(7,0)
        while GPIO.input(5)==0: 

            start_time = time.time() 

        while GPIO.input(5)==1: 

            Bounce_back_time = time.time() 

            pulse_duration = Bounce_back_time - start_time 

            distance = round(pulse_duration * 0.0340 /2, 2)
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()

