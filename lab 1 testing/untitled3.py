# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 07:09:03 2021

@author: Rosalyn
"""
import numpy as np
import matplotlib.pyplot as plt
#plt.style.use('seaborn')

half_wave_angle3=[58,68,78,88,98,108,118,128,138,148,158,168]
no_of_photons_multimeter=[36880000000.0,45870000000.0,46770000000.0,43170000000.0,
                         31480000000.0,23380000000.0,17990000000.0,18890000000.0,
                         26080000000.0,35980000000.0,44070000000.0,45870000000.0]
no_of_photons_oscilloscope1=[113300000000.0,120500000000.0,123200000000.0,113300000000.0,
                             100700000000.0,95340000000.0,92640000000.0,90840000000.0,
                             96240000000.0,118700000000.0,121400000000.0,123300000000.0]

plt.plot(half_wave_angle3,no_of_photons_multimeter, color='b',linestyle='-', label='multimeter')
plt.plot(half_wave_angle3,no_of_photons_oscilloscope1, color='g', label='oscilloscope')
plt.xlabel('half wave plate angle(deg)')
plt.ylabel('no of photon(1/s)')
plt.title('no of photon vs half wave angle')
plt.legend(loc='lower right')
plt.show()