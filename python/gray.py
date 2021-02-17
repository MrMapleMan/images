from PIL import Image
import urllib
import subprocess
import os.path
import math

if not os.path.isfile('oxygen.png'):
  opener = urllib.urlretrieve('http://www.pythonchallenge.com/pc/def/oxygen.png','oxygen.png')

img = Image.open('oxygen.png')
#img = Image.new('RGB',(1000,1000))

def makeGray(img):
  pix = img.load()
  for row in range(img.size[1]):
    for clm in range(img.size[0]):
      pixel = pix[clm,row]
      val = int((float(pixel[0])+pixel[1]+pixel[2])/3)
      pix[clm,row] = (val,val,val,255)


makeGray(img)
img.save('oxygen-gray.png')
img.show()
