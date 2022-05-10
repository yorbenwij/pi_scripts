#librarys
import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setup(12,GPIO.OUT) #in1 stappenmotor
GPIO.setup(16,GPIO.OUT) #in2 stappenmotor
GPIO.setup(20,GPIO.OUT) #in3 stappenmotor
GPIO.setup(21,GPIO.OUT) #in4 stappenmotor
GPIO.setup(14,GPIO.OUT) #relais voor de lamp aan te sturen
GPIO.setup(15,GPIO.OUT) #relais om het water bij te vullen
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #knop voor het licht
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #knop voor het water bij te vullen
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #knop voor stappenmotor links te laten draainen
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #knop voor stappenmotor rechts te laten draainen


try:
    while True:
        if GPIO.input(18) == GPIO.HIGH: #deel voor het licht
            GPIO.output(14, 1)
        else:
            GPIO.output(14,0)
        if GPIO.input(23) == GPIO.HIGH: #deel voor het water bij te vullen
            GPIO.output(15, 1)
        else:
            GPIO.output(15,0)
        if GPIO.input(24) == GPIO.HIGH: #deel voor het licht
            GPIO.output(12, 1)
            GPIO.output(16, 0)
            GPIO.output(20, 0)
            GPIO.output(21, 0)
            time.sleep(0.5)
            GPIO.output(12, 0)
            GPIO.output(16, 1)
            GPIO.output(20, 0)
            GPIO.output(21, 0)
            time.sleep(0.5)
            GPIO.output(12, 0)
            GPIO.output(16, 0)
            GPIO.output(20, 1)
            GPIO.output(21, 0)
            time.sleep(0.5)
            GPIO.output(12, )
            GPIO.output(16, 0)
            GPIO.output(20, 0)
            GPIO.output(21, 1)
            time.sleep(0.5)
        else:
            GPIO.output(14,0)
            GPIO.output(14, 0)
            GPIO.output(14, 0)
            GPIO.output(14, 0)

except KeyboardInterrupt:
    GPIO.cleanup()