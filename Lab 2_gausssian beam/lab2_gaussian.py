# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 12:14:43 2021

@author: Rosalyn
"""

# import libraries
import csv 
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# plot of beam diameter as a function of position from the laser output.

position=[15,25,35,45,55,65,75,85,95,105]
beam_diameter=[883.5,135.9,271.8,356.8,307.5,101.9,373.8,339.8,423.0,101.9]

plot1=plt.figure(1)
plt.plot(position,beam_diameter)
plt.xlabel('position(cm)')
plt.ylabel('beam diameter')
plt.title('beam diameter as a function of position')

# improve padding of the graph 
plt.tight_layout()
plt.show()


pixel=[] # red
pixel1=[] # green
pixel2=[] # blue
pixel3=[] # black
point=[]


# 25cm 
with open("25cm.csv","r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_count = 0
    for row in csv_reader:
        point.append(float(row[0]))
        pixel.append(float(row[1]))
        pixel1.append(float(row[2]))
        pixel2.append(float(row[3]))
        pixel3.append(float(row[4]))
        #print("point:",row[0])
        #print( "pixel:", row[1])
        #print( "pixe1l:", row[2])
        #print( "pixel2:", row[3])
        #print( "pixel3:", row[4])

trim_low_index=200
trim_high_index=800
pixel_trim=pixel3[trim_low_index:trim_high_index]
point_trim=point[trim_low_index:trim_high_index]

plot2=plt.figure(2)       
plt.plot(pixel, color='r')       
plt.plot(pixel1, color='g')
plt.plot(pixel2, color='b')
plt.plot(pixel3, color='k')
plt.plot(point_trim,pixel_trim,'y')

plt.xlabel('point')
plt.ylabel('pixel')
plt.title('pixel number vs point(25cm)')

# Gaussian Function 
def gauss_function(x, a, x0, sigma):
    return a*np.exp(-(x-x0)**2/(2*sigma**2))

popt, pcov = curve_fit(gauss_function,point_trim, pixel_trim, p0 = [1, 450, 300])
perr= np.sqrt(np.diag(pcov))
   
plt.plot(point_trim,gauss_function(point_trim, *popt), label='fit')


#print(pcov)
#print(perr)

#35cm

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
        #print("point:",row[0])
        #print( "pixel:", row[1])
        #print( "pixe1l:", row[2])
        #print( "pixel2:", row[3])
        #print( "pixel3:", row[4])

trim35_low_index=250
trim35_high_index=600
pixel35_trim=pixel3[trim35_low_index:trim35_high_index]
point_trim=point[trim35_low_index:trim35_high_index]

plot3=plt.figure(3)       
plt.plot(pixel, color='r')       
plt.plot(pixel1, color='g')
plt.plot(pixel2, color='b')
plt.plot(pixel3, color='k')
plt.plot(point_trim,pixel35_trim,'y')

plt.xlabel('point')
plt.ylabel('pixel')
plt.title('pixel number vs point(35cm)')

# Gaussian Function 
def gauss_function(x, a, x0, sigma):
    return a*np.exp(-(x-x0)**2/(2*sigma**2))

popt, pcov = curve_fit(gauss_function,point_trim, pixel35_trim, p0 = [1, 500, 175])
perr= np.sqrt(np.diag(pcov))
   
plt.plot(point_trim,gauss_function(point_trim, *popt), label='fit')
print(pcov)
print(perr)

# 45cm

pixel=[] # red
pixel1=[] # green
pixel2=[] # blue
pixel3=[] # black
point=[]

with open("45cm.csv","r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_count = 0
    for row in csv_reader:
        point.append(float(row[0]))
        pixel.append(float(row[1]))
        pixel1.append(float(row[2]))
        pixel2.append(float(row[3]))
        pixel3.append(float(row[4]))
        #print("point:",row[0])
        #print( "pixel:", row[1])
        #print( "pixe1l:", row[2])
        #print( "pixel2:", row[3])
        #print( "pixel3:", row[4])

trim45_low_index=400
trim45_high_index=1200
pixel45_trim=pixel3[trim45_low_index:trim45_high_index]
point_trim=point[trim45_low_index:trim45_high_index]

plot4=plt.figure(4)       
plt.plot(pixel, color='r')       
plt.plot(pixel1, color='g')
plt.plot(pixel2, color='b')
plt.plot(pixel3, color='k')
plt.plot(point_trim,pixel45_trim,'y')

plt.xlabel('point')
plt.ylabel('pixel')
plt.title('pixel number vs point (45cm)')

# Gaussian Function 
def gauss_function(x, a, x0, sigma):
    return a*np.exp(-(x-x0)**2/(2*sigma**2))

popt, pcov = curve_fit(gauss_function,point_trim, pixel45_trim, p0 = [1, 700, 400])
perr= np.sqrt(np.diag(pcov))
   
plt.plot(point_trim,gauss_function(point_trim, *popt), label='fit')
print(pcov)
print(perr)

#55cm

pixel=[] # red
pixel1=[] # green
pixel2=[] # blue
pixel3=[] # black
point=[]

with open("55cm.csv","r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_count = 0
    for row in csv_reader:
        point.append(float(row[0]))
        pixel.append(float(row[1]))
        pixel1.append(float(row[2]))
        pixel2.append(float(row[3]))
        pixel3.append(float(row[4]))
        #print("point:",row[0])
        #print( "pixel:", row[1])
        #print( "pixe1l:", row[2])
        #print( "pixel2:", row[3])
        #print( "pixel3:", row[4])
        
trim55_low_index=480
trim55_high_index=980
pixel55_trim=pixel3[trim55_low_index:trim55_high_index]
point_trim=point[trim55_low_index:trim55_high_index]

plot5=plt.figure(5)       
plt.plot(pixel, color='r')       
plt.plot(pixel1, color='g')
plt.plot(pixel2, color='b')
plt.plot(pixel3, color='k')
plt.plot(point_trim,pixel55_trim,'y')

plt.xlabel('point')
plt.ylabel('pixel')
plt.title('pixel number vs point(55cm)')

# Gaussian Function 
def gauss_function(x, a, x0, sigma):
    return a*np.exp(-(x-x0)**2/(2*sigma**2))

popt, pcov = curve_fit(gauss_function,point_trim, pixel55_trim, p0 = [1, 700, 250])
perr= np.sqrt(np.diag(pcov))
   
plt.plot(point_trim,gauss_function(point_trim, *popt), label='fit')
print(pcov)
print(perr)

#65cm

pixel=[] # red
pixel1=[] # green
pixel2=[] # blue
pixel3=[] # black
point=[]

with open("65cm.csv","r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_count = 0
    for row in csv_reader:
        point.append(float(row[0]))
        pixel.append(float(row[1]))
        pixel1.append(float(row[2]))
        pixel2.append(float(row[3]))
        pixel3.append(float(row[4]))
        #print("point:",row[0])
        #print( "pixel:", row[1])
        #print( "pixe1l:", row[2])
        #print( "pixel2:", row[3])
        #print( "pixel3:", row[4])
        
trim65_low_index=590
trim65_high_index=1030
pixel65_trim=pixel3[trim65_low_index:trim65_high_index]
point_trim=point[trim65_low_index:trim65_high_index]

plot6=plt.figure(6)       
plt.plot(pixel, color='r')       
plt.plot(pixel1, color='g')
plt.plot(pixel2, color='b')
plt.plot(pixel3, color='k')
plt.plot(point_trim,pixel65_trim,'y')

plt.xlabel('point')
plt.ylabel('pixel')
plt.title('pixel number vs point(65cm)')

# Gaussian Function 
def gauss_function(x, a, x0, sigma):
    return a*np.exp(-(x-x0)**2/(2*sigma**2))

popt, pcov = curve_fit(gauss_function,point_trim, pixel65_trim, p0 = [1, 700, 240])
perr= np.sqrt(np.diag(pcov))
   
plt.plot(point_trim,gauss_function(point_trim, *popt), label='fit')#print(pcov)
print(pcov)
print(perr)

#75cm

pixel=[] # red
pixel1=[] # green
pixel2=[] # blue
pixel3=[] # black
point=[]

with open("75cm.csv","r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_count = 0
    for row in csv_reader:
        point.append(float(row[0]))
        pixel.append(float(row[1]))
        pixel1.append(float(row[2]))
        pixel2.append(float(row[3]))
        pixel3.append(float(row[4]))
        #print("point:",row[0])
        #print( "pixel:", row[1])
        #print( "pixe1l:", row[2])
        #print( "pixel2:", row[3])
        #print( "pixel3:", row[4])
        
trim75_low_index=300
trim75_high_index=1000
pixel75_trim=pixel3[trim75_low_index:trim75_high_index]
point_trim=point[trim75_low_index:trim75_high_index]

plot7=plt.figure(7)       
plt.plot(pixel, color='r')       
plt.plot(pixel1, color='g')
plt.plot(pixel2, color='b')
plt.plot(pixel3, color='k')
plt.plot(point_trim,pixel75_trim,'y')

plt.xlabel('point')
plt.ylabel('pixel')
plt.title('pixel number vs point(75cm)')

# Gaussian Function 
def gauss_function(x, a, x0, sigma):
    return a*np.exp(-(x-x0)**2/(2*sigma**2))

popt, pcov = curve_fit(gauss_function,point_trim, pixel75_trim, p0 = [1, 610, 350])
perr= np.sqrt(np.diag(pcov))
   
plt.plot(point_trim,gauss_function(point_trim, *popt), label='fit')#print(pcov)
print(pcov)
print(perr)

# 85cm

pixel=[] # red
pixel1=[] # green
pixel2=[] # blue
pixel3=[] # black
point=[]

with open("85cm.csv","r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_count = 0
    for row in csv_reader:
        point.append(float(row[0]))
        pixel.append(float(row[1]))
        pixel1.append(float(row[2]))
        pixel2.append(float(row[3]))
        pixel3.append(float(row[4]))
        #print("point:",row[0])
        #print( "pixel:", row[1])
        #print( "pixe1l:", row[2])
        #print( "pixel2:", row[3])
        #print( "pixel3:", row[4])
        
trim85_low_index=0
trim85_high_index=1000
pixel85_trim=pixel3[trim85_low_index:trim85_high_index]
point_trim=point[trim85_low_index:trim85_high_index]

plot8=plt.figure(8)       
plt.plot(pixel, color='r')       
plt.plot(pixel1, color='g')
plt.plot(pixel2, color='b')
plt.plot(pixel3, color='k')
plt.plot(point_trim,pixel85_trim,'y')

plt.xlabel('point')
plt.ylabel('pixel')
plt.title('pixel number vs point(85cm)')

# Gaussian Function 
def gauss_function(x, a, x0, sigma):
    return a*np.exp(-(x-x0)**2/(2*sigma**2))

popt, pcov = curve_fit(gauss_function,point_trim, pixel85_trim, p0 = [1, 500, 500])
perr= np.sqrt(np.diag(pcov))
   
plt.plot(point_trim,gauss_function(point_trim, *popt), label='fit')
print(pcov)
print(perr)

# 95cm 

pixel=[] # red
pixel1=[] # green
pixel2=[] # blue
pixel3=[] # black
point=[]

with open("95cm.csv","r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_count = 0
    for row in csv_reader:
        point.append(float(row[0]))
        pixel.append(float(row[1]))
        pixel1.append(float(row[2]))
        pixel2.append(float(row[3]))
        pixel3.append(float(row[4]))
        #print("point:",row[0])
        #print( "pixel:", row[1])
        #print( "pixe1l:", row[2])
        #print( "pixel2:", row[3])
        #print( "pixel3:", row[4])

trim95_low_index=200
trim95_high_index=1000
pixel95_trim=pixel3[trim95_low_index:trim95_high_index]
point_trim=point[trim95_low_index:trim95_high_index]

plot9=plt.figure(9)       
plt.plot(pixel, color='r')       
plt.plot(pixel1, color='g')
plt.plot(pixel2, color='b')
plt.plot(pixel3, color='k')
plt.plot(point_trim,pixel95_trim,'y')

plt.xlabel('point')
plt.ylabel('pixel')
plt.title('pixel number vs point(95cm)')

# Gaussian Function 
def gauss_function(x, a, x0, sigma):
    return a*np.exp(-(x-x0)**2/(2*sigma**2))

popt, pcov = curve_fit(gauss_function,point_trim, pixel95_trim, p0 = [1, 600, 400])
perr= np.sqrt(np.diag(pcov))
   
plt.plot(point_trim,gauss_function(point_trim, *popt), label='fit')
print(pcov)
print(perr)

#105cm

pixel=[] # red
pixel1=[] # green
pixel2=[] # blue
pixel3=[] # black
point=[]

with open("105cm.csv","r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_count = 0
    for row in csv_reader:
        point.append(float(row[0]))
        pixel.append(float(row[1]))
        pixel1.append(float(row[2]))
        pixel2.append(float(row[3]))
        pixel3.append(float(row[4]))
        #print("point:",row[0])
        #print( "pixel:", row[1])
        #print( "pixe1l:", row[2])
        #print( "pixel2:", row[3])
        #print( "pixel3:", row[4])
        
trim105_low_index=200
trim105_high_index=1000
pixel105_trim=pixel3[trim105_low_index:trim105_high_index]
point_trim=point[trim105_low_index:trim105_high_index]


plot10=plt.figure(10)       
plt.plot(pixel, color='r')       
plt.plot(pixel1, color='g')
plt.plot(pixel2, color='b')
plt.plot(pixel3, color='k')
plt.plot(point_trim,pixel105_trim,'y')

plt.xlabel('point')
plt.ylabel('pixel')
plt.title('pixel number vs point(105cm)')

# Gaussian Function 
def gauss_function(x, a, x0, sigma):
    return a*np.exp(-(x-x0)**2/(2*sigma**2))

popt, pcov = curve_fit(gauss_function,point_trim, pixel95_trim, p0 = [1, 600, 400])
perr= np.sqrt(np.diag(pcov))
   
plt.plot(point_trim,gauss_function(point_trim, *popt), label='fit')
print(pcov)
print(perr)

# 15cm

pixel=[] # red
pixel1=[] # green
pixel2=[] # blue
pixel3=[] # black
point=[]

with open("15cm.csv","r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_count = 0
    for row in csv_reader:
        point.append(float(row[0]))
        pixel.append(float(row[1]))
        pixel1.append(float(row[2]))
        pixel2.append(float(row[3]))
        pixel3.append(float(row[4]))
        #print("point:",row[0])
        #print( "pixel:", row[1])
        #print( "pixe1l:", row[2])
        #print( "pixel2:", row[3])
        #print( "pixel3:", row[4])

trim15_low_index=200
trim15_high_index=1000
pixel15_trim=pixel3[trim15_low_index:trim15_high_index]
point_trim=point[trim15_low_index:trim15_high_index]

plot11=plt.figure(11)       
plt.plot(pixel, color='r')       
plt.plot(pixel1, color='g')
plt.plot(pixel2, color='b')
plt.plot(pixel3, color='k')
plt.plot(point_trim,pixel15_trim,'y')

plt.xlabel('point')
plt.ylabel('pixel')
plt.title('pixel number vs point(15cm)')

# Gaussian Function 
def gauss_function(x, a, x0, sigma):
    return a*np.exp(-(x-x0)**2/(2*sigma**2))

popt, pcov = curve_fit(gauss_function,point_trim, pixel95_trim, p0 = [1, 400, 400])
perr= np.sqrt(np.diag(pcov))
   
plt.plot(point_trim,gauss_function(point_trim, *popt), label='fit')
print(pcov)
print(perr)

#laser focusing
#lens 1

pixel=[] # red
pixel1=[] # green
pixel2=[] # blue
pixel3=[] # black
point=[]

with open("lens 1(89cm).csv","r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_count = 0
    for row in csv_reader:
        point.append(float(row[0]))
        pixel.append(float(row[1]))
        pixel1.append(float(row[2]))
        pixel2.append(float(row[3]))
        pixel3.append(float(row[4]))
        #print("point:",row[0])
        #print( "pixel:", row[1])
        #print( "pixe1l:", row[2])
        #print( "pixel2:", row[3])
        #print( "pixel3:", row[4])
        
trim_lens1_low_index=540
trim_lens1_high_index=1000
pixel_lens1_trim=pixel3[trim_lens1_low_index:trim_lens1_high_index]
point_trim=point[trim_lens1_low_index:trim_lens1_high_index]
        
plot12=plt.figure(12)       
plt.plot(pixel, color='r')       
plt.plot(pixel1, color='g')
plt.plot(pixel2, color='b')
plt.plot(pixel3, color='k')
plt.plot(point_trim,pixel_lens1_trim,'y')

plt.xlabel('point')
plt.ylabel('pixel')
plt.title('pixel number vs point(lens 1)')

# Gaussian Function 
def gauss_function(x, a, x0, sigma):
    return a*np.exp(-(x-x0)**2/(2*sigma**2))

popt, pcov = curve_fit(gauss_function,point_trim, pixel_lens1_trim, p0 = [1, 630, 230])
perr= np.sqrt(np.diag(pcov))
   
plt.plot(point_trim,gauss_function(point_trim, *popt), label='fit')
print(pcov)
print(perr)

# lens 2

pixel=[] # red
pixel1=[] # green
pixel2=[] # blue
pixel3=[] # black
point=[]

with open("len 2(82.5cm).csv","r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_count = 0
    for row in csv_reader:
        point.append(float(row[0]))
        pixel.append(float(row[1]))
        pixel1.append(float(row[2]))
        pixel2.append(float(row[3]))
        pixel3.append(float(row[4]))
        #print("point:",row[0])
        #print( "pixel:", row[1])
        #print( "pixe1l:", row[2])
        #print( "pixel2:", row[3])
        #print( "pixel3:", row[4])
        
trim_lens2_low_index=400
trim_lens2_high_index=1200
pixel_lens2_trim=pixel3[trim_lens2_low_index:trim_lens2_high_index]
point_trim=point[trim_lens2_low_index:trim_lens2_high_index]
        
plot13=plt.figure(13)       
plt.plot(pixel, color='r')       
plt.plot(pixel1, color='g')
plt.plot(pixel2, color='b')
plt.plot(pixel3, color='k')
plt.plot(point_trim,pixel_lens2_trim,'y')

plt.xlabel('point')
plt.ylabel('pixel')
plt.title('pixel number vs point(lens 2)')

# Gaussian Function 
def gauss_function(x, a, x0, sigma):
    return a*np.exp(-(x-x0)**2/(2*sigma**2))

popt, pcov = curve_fit(gauss_function,point_trim, pixel_lens2_trim, p0 = [1, 800, 400])
perr= np.sqrt(np.diag(pcov))
   
plt.plot(point_trim,gauss_function(point_trim, *popt), label='fit')
print(pcov)
print(perr)

# lens 3

pixel=[] # red
pixel1=[] # green
pixel2=[] # blue
pixel3=[] # black
point=[]

with open("lens 3(75cm).csv","r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_count = 0
    for row in csv_reader:
        point.append(float(row[0]))
        pixel.append(float(row[1]))
        pixel1.append(float(row[2]))
        pixel2.append(float(row[3]))
        pixel3.append(float(row[4]))
        #print("point:",row[0])
        #print( "pixel:", row[1])
        #print( "pixe1l:", row[2])
        #print( "pixel2:", row[3])
        #print( "pixel3:", row[4])
        
trim_lens3_low_index=400
trim_lens3_high_index=1200
pixel_lens3_trim=pixel3[trim_lens3_low_index:trim_lens3_high_index]
point_trim=point[trim_lens3_low_index:trim_lens3_high_index]
        
plot14=plt.figure(14)       
plt.plot(pixel, color='r')       
plt.plot(pixel1, color='g')
plt.plot(pixel2, color='b')
plt.plot(pixel3, color='k')
plt.plot(point_trim,pixel_lens3_trim,'y')

plt.xlabel('point')
plt.ylabel('pixel')
plt.title('pixel number vs point(lens 3)')

# Gaussian Function 
def gauss_function(x, a, x0, sigma):
    return a*np.exp(-(x-x0)**2/(2*sigma**2))

popt, pcov = curve_fit(gauss_function,point_trim, pixel_lens2_trim, p0 = [1, 800, 400])
perr= np.sqrt(np.diag(pcov))
   
plt.plot(point_trim,gauss_function(point_trim, *popt), label='fit')
print(pcov)
print(perr)

# before  beam expander 

pixel=[] # red
pixel1=[] # green
pixel2=[] # blue
pixel3=[] # black
point=[]

with open("before beam expander.csv","r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_count = 0
    for row in csv_reader:
        point.append(float(row[0]))
        pixel.append(float(row[1]))
        pixel1.append(float(row[2]))
        pixel2.append(float(row[3]))
        pixel3.append(float(row[4]))
        #print("point:",row[0])
        #print( "pixel:", row[1])
        #print( "pixe1l:", row[2])
        #print( "pixel2:", row[3])
        #print( "pixel3:", row[4])
        
trim_before_low_index=390
trim_before_high_index=820
pixel_before_trim=pixel3[trim_before_low_index:trim_before_high_index]
point_trim=point[trim_before_low_index:trim_before_high_index]

plot15=plt.figure(15)       
plt.plot(pixel, color='r')       
plt.plot(pixel1, color='g')
plt.plot(pixel2, color='b')
plt.plot(pixel3, color='k')
plt.plot(point_trim,pixel_before_trim,'y')

plt.xlabel('point')
plt.ylabel('pixel')
plt.title('pixel number vs point(before beam expander)')

# Gaussian Function 
def gauss_function(x, a, x0, sigma):
    return a*np.exp(-(x-x0)**2/(2*sigma**2))

popt, pcov = curve_fit(gauss_function,point_trim, pixel_before_trim, p0 = [1, 600, 215])
perr= np.sqrt(np.diag(pcov))
   
plt.plot(point_trim,gauss_function(point_trim, *popt), label='fit')
print(pcov)
print(perr)

# after beam expander 

pixel=[] # red
pixel1=[] # green
pixel2=[] # blue
pixel3=[] # black
point=[]

with open("beam expander.csv","r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_count = 0
    for row in csv_reader:
        point.append(float(row[0]))
        pixel.append(float(row[1]))
        pixel1.append(float(row[2]))
        pixel2.append(float(row[3]))
        pixel3.append(float(row[4]))
        #print("point:",row[0])
        #print( "pixel:", row[1])
        #print( "pixe1l:", row[2])
        #print( "pixel2:", row[3])
        #print( "pixel3:", row[4])

trim_after_low_index=200
trim_after_high_index=1100
pixel_after_trim=pixel3[trim_after_low_index:trim_after_high_index]
point_trim=point[trim_after_low_index:trim_after_high_index]

plot16=plt.figure(16)       
plt.plot(pixel, color='r')       
plt.plot(pixel1, color='g')
plt.plot(pixel2, color='b')
plt.plot(pixel3, color='k')
plt.plot(point_trim,pixel_after_trim,'y')

plt.xlabel('point')
plt.ylabel('pixel')
plt.title('pixel number vs point(after beam expander)')

# Gaussian Function 
def gauss_function(x, a, x0, sigma):
    return a*np.exp(-(x-x0)**2/(2*sigma**2))

popt, pcov = curve_fit(gauss_function,point_trim, pixel_after_trim, p0 = [1, 780, 450])
perr= np.sqrt(np.diag(pcov))
   
plt.plot(point_trim,gauss_function(point_trim, *popt), label='fit')
print(pcov)
print(perr)