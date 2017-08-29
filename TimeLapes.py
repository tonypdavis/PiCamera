# Time-Lapes Pi Camera 
# created on 29.08.2017 Tony Davis 


from picamera import PiCamera
from time import sleep
import datetime
import time

timer_a = time.time() # duration timer
camera = PiCamera()
date = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")


#------------- change these values to set freuency and duration--------------------#

feq = 30  # interval between taking a picture (in seconds)
duration = 120 # How long the program will continue run (in seconds i.e two hours 7200)

#----------------------------------------------------------------------------------#



print 'working'

while True:

    date = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
    camera.capture('/home/pi/Camera/images/' + date + ' .jpg')
    
    sleep(feq) # time interval between images
    
    print('/home/pi/Camera/images/' + date + ' .jpg')
    
    if time.time() - timer_a > duration:  # quit the program when the duration has been reached
		quit()
        










