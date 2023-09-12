# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 10:35:44 2021

@author: Rosalyn
"""

import csv 
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit



frequency=[]
photodiode_signal=[]

with open("frequency.csv","r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_count = 0
    for row in csv_reader:
        frequency.append(float(row[10]))
        photodiode_signal.append(float(row[11]))
        
trim_low_index = 900
trim_high_index= 1500
frequency_trim = frequency[trim_low_index:trim_high_index]
photodiode_signal_trim = photodiode_signal[trim_low_index:trim_high_index]

def gauss_function(x,a,x0,sigma):
    return a*np.exp(-(x-x0)**2/(2*sigma**2))

popt, pcov = curve_fit(gauss_function, frequency_trim, photodiode_signal_trim, p0 = [1, 1,10])
perr=np.sqrt(np.diag(pcov))


plot1=plt.figure(1)
plt.plot(frequency_trim,gauss_function(frequency_trim,*popt),label='fit')
plt.plot(frequency,photodiode_signal, color='y') 
plt.xlabel('frequency(GHz)')
plt.ylabel('photodiode signal(mV)')   
plt.title('Photodiode signal vs frequency')
plt.legend(["fit","Centre peak"])
plt.show()

print(pcov)
print(perr)
print("\n fit 1 is: ", pcov[0,0], "\n fit 2 is: ", pcov[1,1], "\n fit 3 is: ", pcov[2,2])
print("\n sigma 1 is: ", perr[0], "\n sigma 2 is: ", perr[1], "\n sigma 3 is: ", perr[2])

# standard deviation of lock in laser
frequency =[]
signal=[]

with open("lock.csv") as csv_file:
    csv_reader = csv.reader(csv_file,delimiter= ',')
    line_count=0
    for row in csv_reader:
        frequency.append(float(row[7]))
        signal.append(float(row[9]))
        print("signal: ", row[9])

signal_trim = signal
frequency_trim = frequency

standard = np.std(signal_trim)

print(standard)


