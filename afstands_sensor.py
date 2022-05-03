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
        GPIO.output(17,0)
        while GPIO.input(GPIO_ECHO)==0: 

            start_time = time.time() 

        while GPIO.input(GPIO_ECHO)==1: 

            Bounce_back_time = time.time() 

            pulse_duration = Bounce_back_time - start_time 

            distance = round(pulse_duration * 17150, 2) 

except KeyboardInterrupt:
    GPIO.cleanup()

