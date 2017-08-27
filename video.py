# test code for PiCamera
# this programe captures a 10 second video
# to view the video open the terminal and type omxplayer video.h26

from picamera import PiCamera
from time import sleep

camera = PiCamera()


camera.start_preview()

camera.start_recording('/home/pi/video.h264')
sleep (10)
camera.stop_recording()
    
camera.stop_preview()

