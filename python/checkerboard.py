from PIL import Image
import urllib
import subprocess
import os.path
import math
import sys

if not os.path.isfile('oxygen.png'):
  opener = urllib.urlretrieve('http://www.pythonchallenge.com/pc/def/oxygen.png','oxygen.png')

pixelDimension=10
gradient=True

if len(sys.argv) > 2:
  if(sys.argv[2].upper() == "TRUE" or sys.argv[2] == "1"):
    gradient = True
  else:
    gradient = False
if len(sys.argv) > 1:
  pixelDimension = int(sys.argv[1])

img = Image.new('RGB',(1000,1000))

if gradient:
  width, height = img.size
  middlePixel = (int(width/2/pixelDimension), int(height/2/pixelDimension))
  maxDistance = math.sqrt(middlePixel[0]**2. + middlePixel[1]**2)

def makeCheckerboard(img):
  pix = img.load()
  for row in range(img.size[1]):
    for clm in range(img.size[0]):
      pixelatedPixel = (int(clm/pixelDimension), int(row/pixelDimension))
      if ((pixelatedPixel[0]+pixelatedPixel[1]) % 2 == 0):
        if gradient:
          distance = math.sqrt((float(middlePixel[0])-pixelatedPixel[0])**2 + (float(middlePixel[1])-pixelatedPixel[1])**2)
          val = int(distance/maxDistance*255/2)
        else:
          val = 0
      else:
        val = 255
      pix[clm,row] = (val,val,val,255)

makeCheckerboard(img)
img.show()

#radialGradient(img)
#img.show()
