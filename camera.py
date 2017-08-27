# test code for PiCamera

from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.annotate_text = 'Hello World'

camera.start_preview()

for i in range (5):
    sleep(5)
    camera.capture('/home/pi/Documents/Python/PiCamera/Image/image%s.jpg' % i)
    
camera.stop_preview()

