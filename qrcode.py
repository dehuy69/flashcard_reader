import pyzbar.pyzbar as pyzbar
from picamera.array import PiRGBArray
from picamera import PiCamera
# import numpy as np
import time
import os

audio_list = ['1.wav','2.wav','3.wav','4.wav','5.wav','6.wav','7.wav','8.wav','9.wav'
              ,'10.wav','11.wav','12.wav','13.wav','14.wav','15.wav','16.wav','17.wav','18.wav'
              ,'19.wav','20.wav','21.wav','22.wav','23.wav','24.wav','25.wav','26.wav','27.wav'
              ,'28.wav','29.wav','30.wav','31.wav','32.wav','33.wav','34.wav','35.wav','36.wav'
              ,'37.wav','38.wav','39.wav','40.wav','41.wav','42.wav','43.wav','44.wav','45.wav'
              ,'46.wav','47.wav','48.wav','49.wav','50.wav','51.wav','52.wav','53.wav','54.wav'
              ,'55.wav','56.wav','57.wav','58.wav','59.wav','60.wav','61.wav','62.wav']

camera = PiCamera()
camera.resolution = (480, 320)
rawCapture = PiRGBArray(camera)
privious_data = []
privious_time = 0
camera.start_preview(fullscreen=False, window=(100,20,480,320))
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
          os.system("aplay ./audio/{0}".format(audio_list[int(obj.data)-1]))
          privious_data = obj.data
##          privious_time = time.time()
    rawCapture.truncate(0)
  except:
    camera.stop_preview()
    break
  
