#librarys
import RPi.GPIO as GPIO
import time
import busio
import digitalio
import board
import adafruit_pcd8544
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

GPIO.setmode(GPIO.BCM)
GPIO.setup(12,GPIO.OUT) #in1 stappenmotor
GPIO.setup(16,GPIO.OUT) #in2 stappenmotor
GPIO.setup(20,GPIO.OUT) #in3 stappenmotor
GPIO.setup(21,GPIO.OUT) #in4 stappenmotor
GPIO.setup(14,GPIO.OUT) #relais voor de lamp aan te sturen
GPIO.setup(15,GPIO.OUT) #relais om het water bij te vullen
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP) #knop voor het licht
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP) #knop voor het water bij te vullen
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP) #knop voor stappenmotor links te laten draainen
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP) #knop voor stappenmotor rechts te laten draainen




try:
    while True:
        button1_state = GPIO.input(18)
        button2_state = GPIO.input(15)
        if button_state == False:
            GPIO.output(14, 1)
            time.sleep(0.2)
        else:
            GPIO.output(14, 0)
        if button2_state == False:
            GPIO.output(15,1)
        else:
            GPIO.output(15,0)
except:
    GPIO.cleanup()