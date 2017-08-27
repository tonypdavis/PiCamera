# Motion Detection Pi Camera 
# created on 16.07.2016 

import RPi.GPIO as GPIO
import time
from picamera import PiCamera

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.IN)

camera = PiCamera()

i = 0

while True:
    i = i +1
    state = GPIO.input(7)
    if state == 0:
        print 'all quite'
        time.sleep(0.5)
    elif state == 1:
        print 'motion detected'
        camera.capture('/home/pi/Documents/Python/PiCamera/Image/image%s.jpg' % i)
        










