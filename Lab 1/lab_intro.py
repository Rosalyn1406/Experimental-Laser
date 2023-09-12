# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 20:43:57 2021

@author: Rosalyn
"""

import csv 
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


# Import CSV Data
half_wave_angle1=[]
no_of_photons=[]
half_wave_angle2=[]
no_of_photons_oscilloscope=[]
half_wave_angle3=[]
no_of_photons_multimeter=[]
no_of_photons_oscilloscope1=[]

with open("Book5.csv","r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_count = 0
    for row in csv_reader:
        half_wave_angle1.append(float(row[0]))
        no_of_photons.append(float(row[1]))
        print( "no_of_photons:", row[1])
        
# plotting data 
plot1=plt.figure(1)
plt.plot(half_wave_angle1,no_of_photons)
plt.xlabel('half wave plate angle(deg)')
plt.ylabel('no of photon (1/s)')
plt.title('no of photon vs half wave plate angle')


with open("Book6.csv","r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_count = 0
    for row in csv_reader:
        half_wave_angle2.append(float(row[0]))
        no_of_photons_oscilloscope.append(float(row[1]))
        print( "no_of_photons_oscilloscope:", row[1])
 
plot2=plt.figure(2)
plt.plot(half_wave_angle2,no_of_photons_oscilloscope)
plt.xlabel('half wave plate angle(deg)')
plt.ylabel('no of photon (1/s)')
plt.title('no of photon vs half wave plate angle')


with open("Book7.csv","r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_count = 0
    for row in csv_reader:
        half_wave_angle3.append(float(row[0]))
        no_of_photons_multimeter.append(float(row[1]))
        no_of_photons_oscilloscope1.append(float(row[2]))
        print( "no_of_photons_multimeter:", row[1])
        print( "no_of_photons_oscilloscope1:", row[2])

plot3=plt.figure(3)
plt.plot(half_wave_angle3,no_of_photons_multimeter, color='b',linestyle='-', label='multimeter')
plt.plot(half_wave_angle3,no_of_photons_oscilloscope1, color='g', label='oscilloscope')
plt.legend(loc='lower right')


plt.xlabel('half wave plate angle(deg)')
plt.ylabel('no of photon (1/s)')
plt.title('no of photon vs half wave plate angle')
plt.show()
