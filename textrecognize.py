# import cv2
import pytesseract
# from PIL import Image
from picamera.array import PiRGBArray
from picamera import PiCamera

camera = PiCamera()
# camera.resolution = (480, 320)
rawCapture = PiRGBArray(camera)
camera.start_preview(fullscreen=False, window=(100,20,480,320))
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
  try:
    frame = rawCapture.array
    text = pytesseract.image_to_string(frame)
    print(text)
  rawCapture.truncate(0)
  except:
    camera.stop_preview()
    break

def recognizetext(im=None, im_path=None):
  if im_path != None:
    image = Image.open(im_path)
    # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # filename = "{}.png".format(os.getpid())
    # cv2.imwrite(filename, image)
    text = pytesseract.image_to_string(image)
    print(text)
  else:
    text = pytesseract.image_to_string(im)
    print(text)

# if __name__=="__main__":
#   recognizetext(im_path='textimage.png')