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
  #img.save('oxygen-gray.png')


# Create radial b/w gradient
def radialGradient(img):
  # Get image dimensions
  width,height=img.size
  pix = img.load()

  # Find midpoint to reference from
  midWidth  = width/2
  midHeight = height/2

  # Determine max distance for scaling
  maxDistance = math.sqrt( float(midWidth)**2 + float(midHeight)**2 )

  # Calculate and apply gradient at each pixel
  for clm in range(width):
    for row in range(height):
      dist = math.sqrt( (float(clm)-midWidth)**2 + (float(row)-midHeight)**2 )
      val = int(255-(dist/maxDistance*255.))
      pix[clm,row] = (val,val,val,255)

makeGray(img)
img.show()

#radialGradient(img)
#img.show()
