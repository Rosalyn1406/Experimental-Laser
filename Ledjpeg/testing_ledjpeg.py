# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 15:48:11 2021

@author: Rosalyn
"""

##These are particularly required for .
import numpy as np
from PIL import Image

#import an image in Python. The convert('L') converts to grayscale
#image must be a .jpg. If you have .bmp, you should use another program to 
#convert to .jpg. I used MS Paint -> Save as. Perhaps possible within Python 
#if needed.
img=Image.open("ledjpeg.jpg").convert('L')


#convert the image to 2D array
imgdata = np.asarray(img)

#output the shape of the array (should be the number of pixels on the camera)
print(imgdata.shape)

#for instructive purposes only, a small 10x10 section of the array is extracted
#imgtrim=imgdata[1000:1010,750:760]
#print(imgtrim)

#for instructive purposes only, a constrant value is subtracted off each array
#element. In reality, you will import a second image as the background image.
#imgbkgd=np.subtract(imgtrim,5)
#print(imgbkgd)

#to substract two arrays, element by element
#imgsub=np.subtract(imgtrim,imgbkgd)
#print(imgsub)

#to take the sum of all elements in an array.
#print(np.sum(imgsub))


# part 2
from astropy.io import fits
import numpy as np
#from PIL import Image

hdul=fits.open('section3.3.41635115208.fits')
hdul1=fits.open('backgroundimage1635117384.fits')

imgdata = hdul[0].data
imgdata1=hdul1[0].data

#output the shape of the array (should be the number of pixels on the camera)
print(imgdata.shape)
print(imgdata1.shape)

#a 2048x1536 section of the array is extracted
imgtrim=imgdata[0:2048,0:1536]
print(imgtrim)
# backgroud image
imgtrim1=imgdata1[0:2048,0:1536]
print(imgtrim1)

#for instructive purposes only, a constrant value is subtracted off each array
#element. In reality, you will import a second image as the background image.

# each element is divided by the quantum efficiency of 35%
img=imgtrim/0.35
print(img)
imgbkgd=imgtrim1/0.35
print(imgbkgd)

#to substract two arrays, element by element
imgsub=imgtrim-imgbkgd
print(imgsub)

#to take the sum of all elements in an array.
print("total number of photons striking the detector=",np.sum(imgsub))
