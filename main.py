!sudo apt install tesseract-ocr
!apt install libtesseract-dev
!pip install Pillow
!pip install pytesseract

import cv2
import pytesseract

dir = 'your_video.mp4'  # directory of video
path = '\images_path'   # path to save images
sec = 0
frame_rate = 0.5       #it will capture image in each 0.5 second

def getFrame(sec,dir,path,count):
    vidcap = cv2.VideoCapture(dir)
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
        cv2.imwrite(str(path)+"/image"+str(count)+".jpg", image)     # save frame as JPG file to path
    return hasFrames
    
def make_images(dir,path,sec,frame_rate):
  count=1
  success = getFrame(sec,count)
  while success:
      count = count + 1
      sec = sec + frameRate
      sec = round(sec, 2)
      success = getFrame(sec,dir,path,count)
      #print(count)
