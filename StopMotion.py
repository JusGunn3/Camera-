from picamera import PiCamera
from gpiozero import Button
camera = PiCamera()
button = Button(2)
camera.start_preview()
button.wait_for_press()
camera.capture('/home/pi/Desktop/image.jpg')
camera.stop_preview()
