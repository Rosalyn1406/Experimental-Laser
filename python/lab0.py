# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 18:10:19 2021

@author: Rosalyn
"""

# import libraries
import csv 
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


# Import CSV Data
time=[]
voltage_raw=[]

with open("Data-Oscilloscope.csv","r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_count = 0
    for row in csv_reader:
        time.append(float(row[3]))
        voltage_raw.append(float(row[4]))
        print( "voltage:", row[4])
        
# plotting data 
plt.plot(time,voltage_raw,'r-')

# plotting error bars for exercise 1 
#voltage_error = 0.005
#plt.errorbar(time,voltage_raw,yerr=voltage_error,fmt='')

# trimming the data
trim_low_index = 2100
trim_high_index = 2500
voltage_trim = voltage_raw[trim_low_index:trim_high_index]
time_trim = time[trim_low_index:trim_high_index]


plt.xlabel('Time')
plt.ylabel('Voltage')
plt.title('Voltage vs Time')

# setting limit axis
plt.axis([0,0.1,0.04,0.13])

#Exercise 2 
# Gaussian Function 
#def gauss_function(x, a, x0, sigma):
    #return a*np.exp(-(x-x0)**2/(2*sigma**2))
#popt, pcov = curve_fit(gauss_function, time_trim, voltage_trim, p0 = [1, 0.4, 0.1])
#perr= np.sqrt(np.diag(pcov))
#plt.plot(time_trim, gauss_function(time_trim, *popt), label='fit')
#plt.plot(time_trim, voltage_trim,'b')

# Exercise 3 
# Lorentzian Function
def lorentz_function(x,a1,x1,sigma1):
    return a1*sigma1**2/(sigma1**2+(x-x1)**2)
popt, pcov = curve_fit(lorentz_function, time_trim, voltage_trim, p0 = [1, 0.09, 0.1])
perr= np.sqrt(np.diag(pcov))
plt.plot(time_trim, lorentz_function(time_trim, *popt), label='fit')
plt.plot(time_trim, voltage_trim,'g')

print(pcov)
print(perr)

#Parsing output from the last two line 
print("The variance for fit parameter a is:", pcov[[0],[0]])
print("The variance for fit parameter x0 is:", pcov[[1],[1]])
print("The variance for fit parameter sigma is:", pcov[[2],[2]])
print("The fit standard deviation of parameter a:", perr[0])
print("The fit standard deviation of parameter x0:", perr[1])
print("The fit standard deviation of parameter sigma:", perr[2])                                                         
                                                        
# improve padding of the graph 
plt.tight_layout()
plt.show()
