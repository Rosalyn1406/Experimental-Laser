# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 12:46:28 2021

@author: Rosalyn
"""
# import libraries
import csv 
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

pixel=[] # red
pixel1=[] # green
pixel2=[] # blue
pixel3=[] # black
point=[]

with open("35cm.csv","r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_count = 0
    for row in csv_reader:
        point.append(float(row[0]))
        pixel.append(float(row[1]))
        pixel1.append(float(row[2]))
        pixel2.append(float(row[3]))
        pixel3.append(float(row[4]))
        print("point:",row[0])
        #print( "pixel:", row[1])
        #print( "pixe1l:", row[2])
        #print( "pixel2:", row[3])
        #print( "pixel3:", row[4])

plot3=plt.figure(3)       
plt.plot(pixel, color='r')       
plt.plot(pixel1, color='g')
plt.plot(pixel2, color='b')
plt.plot(pixel3, color='k')