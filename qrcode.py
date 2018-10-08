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
          if obj.data == '1':
              os.system("aplay ./audio/{0}".format(audio_list[0]))
          elif obj.data == '2':
              os.system("aplay ./audio/{0}".format(audio_list[1]))
          elif obj.data == '3':
              os.system("aplay ./audio/{0}".format(audio_list[2]))
          elif obj.data == '4':
              os.system("aplay ./audio/{0}".format(audio_list[3]))
          elif obj.data == '5':
              os.system("aplay ./audio/{0}".format(audio_list[4]))
          elif obj.data == '6':
              os.system("aplay ./audio/{0}".format(audio_list[5]))
          elif obj.data == '7':
              os.system("aplay ./audio/{0}".format(audio_list[6]))
          elif obj.data == '8':
              os.system("aplay ./audio/{0}".format(audio_list[7]))
          elif obj.data == '9':
              os.system("aplay ./audio/{0}".format(audio_list[8]))
          elif obj.data == '10':
              os.system("aplay ./audio/{0}".format(audio_list[9]))
          elif obj.data == '11':
              os.system("aplay ./audio/{0}".format(audio_list[10]))
          elif obj.data == '12':
              os.system("aplay ./audio/{0}".format(audio_list[11]))
          elif obj.data == '13':
              os.system("aplay ./audio/{0}".format(audio_list[12]))
          elif obj.data == '14':
              os.system("aplay ./audio/{0}".format(audio_list[13]))
          elif obj.data == '15':
              os.system("aplay ./audio/{0}".format(audio_list[14]))
          elif obj.data == '16':
              os.system("aplay ./audio/{0}".format(audio_list[15]))
          elif obj.data == '17':
              os.system("aplay ./audio/{0}".format(audio_list[16]))
          elif obj.data == '18':
              os.system("aplay ./audio/{0}".format(audio_list[17]))
          elif obj.data == '19':
              os.system("aplay ./audio/{0}".format(audio_list[18]))
          elif obj.data == '20':
              os.system("aplay ./audio/{0}".format(audio_list[19]))
          elif obj.data == '21':
              os.system("aplay ./audio/{0}".format(audio_list[20]))
          elif obj.data == '22':
              os.system("aplay ./audio/{0}".format(audio_list[21]))
          elif obj.data == '23':
              os.system("aplay ./audio/{0}".format(audio_list[22]))
          elif obj.data == '24':
              os.system("aplay ./audio/{0}".format(audio_list[23]))
          elif obj.data == '25':
              os.system("aplay ./audio/{0}".format(audio_list[24]))
          elif obj.data == '26':
              os.system("aplay ./audio/{0}".format(audio_list[25]))
          elif obj.data == '27':
              os.system("aplay ./audio/{0}".format(audio_list[26]))
          elif obj.data == '28':
              os.system("aplay ./audio/{0}".format(audio_list[27]))
          elif obj.data == '29':
              os.system("aplay ./audio/{0}".format(audio_list[28]))
          elif obj.data == '30':
              os.system("aplay ./audio/{0}".format(audio_list[29]))
          elif obj.data == '31':
              os.system("aplay ./audio/{0}".format(audio_list[30]))
          elif obj.data == '32':
              os.system("aplay ./audio/{0}".format(audio_list[31]))
          elif obj.data == '33':
              os.system("aplay ./audio/{0}".format(audio_list[32]))
          elif obj.data == '34':
              os.system("aplay ./audio/{0}".format(audio_list[33]))
          elif obj.data == '35':
              os.system("aplay ./audio/{0}".format(audio_list[34]))
          elif obj.data == '36':
              os.system("aplay ./audio/{0}".format(audio_list[35]))
          elif obj.data == '37':
              os.system("aplay ./audio/{0}".format(audio_list[36]))
          elif obj.data == '38':
              os.system("aplay ./audio/{0}".format(audio_list[37]))
          elif obj.data == '39':
              os.system("aplay ./audio/{0}".format(audio_list[38]))
          elif obj.data == '40':
              os.system("aplay ./audio/{0}".format(audio_list[39]))
          elif obj.data == '41':
              os.system("aplay ./audio/{0}".format(audio_list[40]))
          elif obj.data == '42':
              os.system("aplay ./audio/{0}".format(audio_list[41]))
          elif obj.data == '43':
              os.system("aplay ./audio/{0}".format(audio_list[42]))
          elif obj.data == '44':
              os.system("aplay ./audio/{0}".format(audio_list[43]))
          elif obj.data == '45':
              os.system("aplay ./audio/{0}".format(audio_list[44]))
          elif obj.data == '46':
              os.system("aplay ./audio/{0}".format(audio_list[45]))
          elif obj.data == '47':
              os.system("aplay ./audio/{0}".format(audio_list[46]))
          elif obj.data == '48':
              os.system("aplay ./audio/{0}".format(audio_list[47]))
          elif obj.data == '49':
              os.system("aplay ./audio/{0}".format(audio_list[48]))
          elif obj.data == '50':
              os.system("aplay ./audio/{0}".format(audio_list[49]))
          elif obj.data == '51':
              os.system("aplay ./audio/{0}".format(audio_list[50]))
          elif obj.data == '52':
              os.system("aplay ./audio/{0}".format(audio_list[51]))
          elif obj.data == '53':
              os.system("aplay ./audio/{0}".format(audio_list[52]))
          elif obj.data == '54':
              os.system("aplay ./audio/{0}".format(audio_list[53]))
          elif obj.data == '55':
              os.system("aplay ./audio/{0}".format(audio_list[54]))
          elif obj.data == '56':
              os.system("aplay ./audio/{0}".format(audio_list[55]))
          elif obj.data == '57':
              os.system("aplay ./audio/{0}".format(audio_list[56]))
          elif obj.data == '58':
              os.system("aplay ./audio/{0}".format(audio_list[57]))
          elif obj.data == '59':
              os.system("aplay ./audio/{0}".format(audio_list[58]))
          elif obj.data == '60':
              os.system("aplay ./audio/{0}".format(audio_list[59]))
          elif obj.data == '61':
              os.system("aplay ./audio/{0}".format(audio_list[60]))
          elif obj.data == '62':
              os.system("aplay ./audio/{0}".format(audio_list[61]))
          privious_data = obj.data
##          privious_time = time.time()
    rawCapture.truncate(0)
  except:
    camera.stop_preview()
    break
  
