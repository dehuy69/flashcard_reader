# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (800, 600)
rawCapture = PiRGBArray(camera)

# allow the camera to warmup
time.sleep(0.1)

# grab an image from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr",
                                       use_video_port=True):
    image = frame.array
# display the image on screen and wait for a keypress
    cv2.imshow("Image", image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    rawCapture.truncate(0)
