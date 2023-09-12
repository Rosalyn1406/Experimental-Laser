# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 06:36:08 2021

@author: Rosalyn
"""

import matplotlib.pyplot as plt

half_wave_angle1=[208,218,228,238,248,258,268,278,288,298,308,318]
no_of_photons=[10242019900000,10242019900000,10032378340000,10048731030000,10056907380000,10056907380000,
              10056907380000,10040554680000,10032378340000,10024201990000,10024201990000,10032378340000]
plt.plot(half_wave_angle1,no_of_photons)
plt.xlabel('half wave plate angle(deg)')
plt.ylabel('no of photon(1/s)')
plt.title('no of photon vs half wave plate angle')
plt.show()

# import libraries
import csv 
import numpy as np
import matplotlib.pyplot as plt

# Import CSV Data
half_wave_angle1=[]
no_of_photons=[]
half_wave_angle2=[]
no_of_photons_oscilloscope=[]
half_wave_angle3=[]
no_of_photons_multimeter=[]
no_of_photons_oscilloscope1=[]

with open("Book1.csv","r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_count = 0
    for row in csv_reader:
        half_wave_angle1.append(float(row[0]))
        no_of_photons.append(float(row[1]))
        print( "no_of_photons:", row[1])

# plotting data 
plt.plot(half_wave_angle1,no_of_photons)
plt.xlabel('half wave plate angle(deg)')
plt.ylabel('no of photon(1/s)')
plt.title('no of photon vs half wave angle')
plt.show()
        
with open("Book2.csv","r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_count = 0
    for row in csv_reader:
        half_wave_angle2.append(float(row[0]))
        no_of_photons_oscilloscope.append(float(row[1]))
        print( "no_of_photons:", row[1])

# plotting data 
plt.plot(half_wave_angle2,no_of_photons_oscilloscope)
plt.xlabel('half wave plate angle(deg)')
plt.ylabel('no of photon(1/s)')
plt.title('no of photon vs half wave angle')
plt.show()
    
with open("Book3.csv","r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_count = 0
    for row in csv_reader:
        half_wave_angle3.append(float(row[0]))
        no_of_photons_multimeter.append(float(row[1]))
        no_of_photonos_oscilloscope1.append(float(row[2]))
        print( "no_of_photons:", row[2])
        
# plotting data 
plt.plot(half_wave_angle2,no_of_photons_oscilloscope)
plt.xlabel('half wave plate angle(deg)')
plt.ylabel('no of photon(1/s)')
plt.title('no of photon vs half wave angle')
plt.legend(loc='lower right')
plt.show()