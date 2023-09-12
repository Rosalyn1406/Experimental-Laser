# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 08:12:46 2021

@author: Rosalyn
"""
import matplotlib.pyplot as plt
# plot of beam diameter as a function of position from the laser output.

position=[15,25,35,45,55,65,75,85,95,105]
beam_diameter=[883.5, 135.9,271.8,356.8,307.5,101.9,373.8,339.8,423.0,101.9]

plot1=plt.figure(1)
plt.plot(beam_diameter,position)
plt.xlabel('beam diameter(micrometer)')
plt.ylabel('position (cm)')
plt.title('beam diameter as a function of position')
plt.show()
