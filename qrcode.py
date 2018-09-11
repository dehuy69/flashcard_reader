import pyzbar.pyzbar as pyzbar
from picamera.array import PiRGBArray
from picamera import PiCamera
import numpy as np
import time
camera = PiCamera()
camera.resolution = (800, 600)
rawCapture = PiRGBArray(camera)
privious_data = []
privious_time = 0
camera.start_preview(fullscreen=False, window=(100,20,800,600))
for frame in camera.capture_continuous(rawCapture, format="bgr",
                                      use_video_port=True):
  try:
    frame = rawCapture.array
    decodedObjects = pyzbar.decode(frame)
    if decodedObjects != []:
      wait_time = time.time() - privious_time
      for obj in decodedObjects:
        if obj.data != privious_data or wait_time > 5:
          print('Type : ', obj.type)
          print('Data : ', obj.data,'\n')
          privious_data = obj.data
          privious_time = time.time()
    rawCapture.truncate(0)
  except:
    camera.stop_preview()
    break
  
