# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 21:40:48 2021

@author: Rosalyn
"""

import csv 
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

frequency=[]
photodiode_signal=[]


with open("Book1.csv","r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_count = 0
    for row in csv_reader:
        frequency.append(float(row[14]))
        # print( "time:", row[1])
        photodiode_signal.append(float(row[15]))
        # print( "photodiode signal:", row[2])


plot1=plt.figure(1) 
plt.plot(frequency,photodiode_signal,'y-')
# plt.plot(time1,photodiode_signal1,'b-')
plt.xlabel('frequency(Hz)')
plt.ylabel('Photodiode signal(V)')
plt.title('Photodiode signal vs Frequency Rb-87')
plt.show()

frequency1=[]
photodiode_signal1=[]

with open("Book2.csv","r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_count = 0
    for row in csv_reader:
        frequency1.append(float(row[10]))
        # print( "time:", row[1])
        photodiode_signal1.append(float(row[8]))
        # print( "photodiode signal:", row[2])

plot2=plt.figure(2) 
plt.plot(frequency1,photodiode_signal1,'y-')
plt.xlabel('frequency(Hz)')
plt.ylabel('Photodiode signal(V)')
plt.title('Photodiode signal vs Frequency Rb-85')
plt.show()

frequency2=[]
photodiode_signal2=[]

with open("Book3.csv","r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_count = 0
    for row in csv_reader:
        frequency2.append(float(row[10]))
        # print( "time:", row[1])
        photodiode_signal2.append(float(row[8]))
        # print( "photodiode signal:", row[2])

plot3=plt.figure(3) 
plt.plot(frequency2,photodiode_signal2,'y-')
plt.xlabel('frequency(Hz)')
plt.ylabel('Photodiode signal(V)')
plt.title('Photodiode signal vs Frequency Rb-85 F=3')
plt.show()

frequency3=[]
photodiode_signal3=[]

with open("Book4.csv","r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_count = 0
    for row in csv_reader:
        frequency3.append(float(row[10]))
        # print( "time:", row[1])
        photodiode_signal3.append(float(row[8]))
        # print( "photodiode signal:", row[2])

plot4=plt.figure(4) 
plt.plot(frequency3,photodiode_signal3,'y-')
plt.xlabel('frequency(Hz)')
plt.ylabel('Photodiode signal(V)')
plt.title('Photodiode signal vs Frequency Rb-87 F=2')
plt.show()

# plot with x-axis in seconds

# time=[]
# photodiode_signal=[]


# with open("Book1.csv","r") as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=",")
#     line_count = 0
#     for row in csv_reader:
#         time.append(float(row[1]))
#         # print( "time:", row[1])
#         photodiode_signal.append(float(row[15]))
#         # print( "photodiode signal:", row[2])


# plot5=plt.figure(5) 
# plt.plot(time,photodiode_signal,'b-')
# plt.xlabel('time(s)')
# plt.ylabel('Photodiode signal(V)')
# plt.title('Photodiode signal vs time Rb-87')
# plt.show()

# time1=[]
# photodiode_signal1=[]


# with open("Book2.csv","r") as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=",")
#     line_count = 0
#     for row in csv_reader:
#         time1.append(float(row[1]))
#         # print( "time:", row[1])
#         photodiode_signal1.append(float(row[8]))
#         # print( "photodiode signal:", row[2])


# plot6=plt.figure(6) 
# plt.plot(time1,photodiode_signal1,'b-')
# plt.xlabel('time(s)')
# plt.ylabel('Photodiode signal(V)')
# plt.title('Photodiode signal vs time Rb-85')
# plt.show()

# # time2=[]
# # photodiode_signal2=[]


# # with open("Book3.csv","r") as csv_file:
# #     csv_reader = csv.reader(csv_file, delimiter=",")
# #     line_count = 0
# #     for row in csv_reader:
# #         time2.append(float(row[1]))
# #         # print( "time:", row[1])
# #         photodiode_signal2.append(float(row[8]))
# #         # print( "photodiode signal:", row[2])


# # plot7=plt.figure(7) 
# # plt.plot(time2,photodiode_signal2,'b-')
# # plt.xlabel('time(s)')
# # plt.ylabel('Photodiode signal(V)')
# # plt.title('Photodiode signal vs time Rb-85 F=3')
# # plt.show()

# # time3=[]
# # photodiode_signal3=[]


# # with open("Book4.csv","r") as csv_file:
# #     csv_reader = csv.reader(csv_file, delimiter=",")
# #     line_count = 0
# #     for row in csv_reader:
# #         time3.append(float(row[1]))
# #         # print( "time:", row[1])
# #         photodiode_signal3.append(float(row[8]))
# #         # print( "photodiode signal:", row[2])


# # plot8=plt.figure(8) 
# # plt.plot(time3,photodiode_signal3,'b-')
# # plt.xlabel('time(s)')
# # plt.ylabel('Photodiode signal(V)')
# # plt.title('Photodiode signal vs time Rb-87 F=2')
# # plt.show()