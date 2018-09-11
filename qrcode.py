from __future__ import print_function
import pyzbar.pyzbar as pyzbar
from picamera.array import PiRGBArray
from picamera import PiCamera
import numpy as np
import cv2
import time

# cap = cv2.VideoCapture()
camera = PiCamera()
priviouse = []
while(True):
  # ret, frame = cap.read()
  
  rawCapture = PiRGBArray(camera)
  camera.capture(rawCapture, format="bgr")
  frame = rawCapture.array
  cv2.imshow('frame',frame)
  decodedObjects = pyzbar.decode(frame)
  if decodedObjects != []:      
    for obj in decodedObjects:
      if obj.data != priviouse:
        print('Type : ', obj.type)
        print('Data : ', obj.data,'\n')
        priviouse = obj.data
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
