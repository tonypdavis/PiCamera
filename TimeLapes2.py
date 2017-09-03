# Time-Lapes Pi Camera 
# created on 29.08.2017 Tony Davis 


from picamera import PiCamera
from time import sleep
import datetime
import time

timer_a = time.time() # duration timer
camera = PiCamera()
camera.resolution = (1280, 720)
camera.sharpness = 0
camera.contrast = 0
camera.brightness = 50
camera.saturation = 0
camera.ISO = 0
camera.video_stabilization = False
camera.exposure_compensation = 0
camera.exposure_mode = 'auto'
camera.awb_mode = 'auto'
camera.image_effect = 'none'
camera.meter_mode = 'average'
#camera.colour_effect = 'None'
camera.rotation = 90
camera.contrast = 0


date = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")


#------------- change these values to set freuency and duration--------------------#

feq = 2  # interval between taking a picture (in seconds)
duration = 10 # How long the program will continue run (in seconds i.e two hours 7200)

#----------------------------------------------------------------------------------#



print 'working'

while True:

    date = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
    camera.capture('/home/pi/Camera/images/' + date + ' .jpg')
    
    sleep(feq) # time interval between images
    
    print('/home/pi/Camera/images/' + date + ' .jpg')
    
    if time.time() - timer_a > duration:  # quit the program when the duration has been reached
		quit()
		
        










