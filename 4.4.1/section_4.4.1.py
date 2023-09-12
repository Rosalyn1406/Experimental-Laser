# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 14:04:30 2021

@author: Rosalyn
"""

#Anyhwere there are  ... you should put some code or lines of code

#1. import the useful packages. 
import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as cnst

#2. User defined parameters
R = 0.90 #power reflected from mirrors
D = 50.0 #separation distance in mm
lo= 780     #nm  starting wavelength of 780nm for analysis
dl= 0.00001       #nm  
steps = 1000    # the number of wavelengths to consider
nreflect = 100  #number of reflections in etalon
#pi=3.14159265359 


#3. Compute r and t parameters from R
T=1-R
r=np.sqrt(R)
t=np.sqrt(T)

#4. Prepare array for results.
result = [0.0]*steps
freq = [0.0]*steps

for i in range(steps):
    Esum=0.0
    for j in range(nreflect):
        Esum = Esum + (t**2)*r**(2*j)*np.cos( (1 + 2*j)*D*1e-3 / ((lo + i*dl)*1e-9)*2*cnst.pi)
        result[i]=Esum**2
        freq[i]= (cnst.c/(lo*1e-9)-cnst.c/ ((lo + i*dl)*1e-9) )/1e9

plt.plot(freq,result)
plt.xlabel('frequency(hertz)')
plt.ylabel('Intensity(Watts)')
plt.title('Intensity vs frequency')
plt.show()