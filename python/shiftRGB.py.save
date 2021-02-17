#!/usr/bin/env python2

from PIL import Image
import urllib
import subprocess
import os.path
import math
import sys

pixelDimension = 10

if len(sys.argv) > 2:
  rShift = int(sys.argv[1])
  gShift = int(sys.argv[2])
  bShift = int(sys.argv[3])
else:
  print "Pass in r, g, b shift values as command line arguments."
  sys.exit()

img = Image.new('RGB',(1000,1000))

def makeCheckerboard(img):
  pix = img.load()
  for row in range(img.size[1]):
    for clm in range(img.size[0]):
      pixelatedPixel = (int(clm/pixelDimension), int(row/pixelDimension))
      if ((pixelatedPixel[0]+pixelatedPixel[1]) % 2 == 0):
          val = 0
      else:
        val = 255
      pix[clm,row] = (val,val,val)

def shiftRGB(img,rShift,gShift,bShift):
  pix = img.load()
  shifts = [rShift,gShift,bShift]
  for row in range(img.size[1]):
    for clm in range(img.size[0]):
      x = pix[clm,row]
      x = [x[i]+shifts[i] for i in range(len(x))]
      for i in x:
        i = min(i,255)
        i = max(0,i)
        pix[clm,row] = tuple(x)

makeCheckerboard(img)
shiftRGB(img,rShift,gShift,bShift)
img.show()

#radialGradient(img)
#img.show()
