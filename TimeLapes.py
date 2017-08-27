# Time-Lapes Pi Camera 
# created on 27.07.2017 Tony Davis 

import RPi.GPIO as GPIO
from picamera import PiCamera
from time import sleep
import datetime
import time


camera = PiCamera()
date = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")


print 'working'

while True:

    date = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
    camera.capture('/home/pi/Camera/images/' + 'Ki ' + date + ' .jpg')
    
    sleep(60) # use this value to set the time interval between images
    
    print('/home/pi/Camera/images/' + 'Ki ' + date + ' .jpg')
        










