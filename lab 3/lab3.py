# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 18:15:37 2021

@author: Rosalyn
"""
# credit McMcall, Neil for original coding

##These are particularly required for .
from astropy.io import fits
import numpy as np

#part 1
hdul=fits.open('section3.3.41635115208.fits')
hdul1=fits.open('backgroundimage1635117384.fits')

imgdata = hdul[0].data
imgdata1=hdul1[0].data

#output the shape of the array (should be the number of pixels on the camera)
print(imgdata.shape)
print(imgdata1.shape)

#trimming images to full size: 2048x1536 section of the array is extracted
imgtrim=imgdata[0:2048,0:1536]
print(imgtrim)
# backgroud image
imgtrim1=imgdata1[0:2048,0:1536]
print(imgtrim1)

# each element is times with the gain where the gain recorded is 100%=1e/ADU
img=imgtrim*1
print(img)
imgbkgd=imgtrim1*1
print(imgbkgd)

#to substract two arrays, element by element
imgsub=img-imgbkgd
print(imgsub)

#to take the sum of all elements in an array.
print("total number of photons counted by the camera=",np.sum(imgsub))

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

#trimming images to full size: 2048x1536 section of the array is extracted
imgtrim=imgdata[0:2048,0:1536]
print(imgtrim)
# backgroud image
imgtrim1=imgdata1[0:2048,0:1536]
print(imgtrim1)

# each element is times with the gain where the gain recorded is 100%=1e/ADU
img=imgtrim*1
print(img)
imgbkgd=imgtrim1*1
print(imgbkgd)
# each element is divided by the quantum efficiency of 35%=0.35. 
img2=(img/0.35)
print(img2)
imgbkgd2=(imgbkgd/0.35)
print(imgbkgd2)

#to substract two arrays, element by element
imgsub=img2-imgbkgd2
print(imgsub)

#to take the sum of all elements in an array.
print("total number of photons striking the detector=",np.sum(imgsub))


