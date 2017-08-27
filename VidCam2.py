# Motion Detection Pi Camera 
# created on 16.07.2017 Tony Davis 

import RPi.GPIO as GPIO
from picamera import PiCamera
from time import sleep
import datetime
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.IN)

camera = PiCamera()
date = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")

# i = 0
print 'VidCam working'

while True:
    state = GPIO.input(11)
    if state == 0:
        sleep(0.5)
    elif state == 1:
        # i = i +1
        print 'motion detected'
        camera.start_recording('/home/pi/Camera/images/' + 'LR ' + date + ' .h264')
        sleep(10)
        camera.stop_recording()
        










