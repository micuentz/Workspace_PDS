# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 22:33:40 2024

@author: Tobias
"""

import numpy as np
import matplotlib.pyplot as plt

modo = "cuadrada"
vmax = 1
dc = 0
ff = 1
pf = 0
nn = 2000
fs = 1000

x = np.arange(0 , nn/fs , 1/nn)

y = np.arange(0 , nn/fs , 1/nn)

if modo == "seno":
    y = dc + vmax * np.sin(2*np.pi*ff*x + pf)
elif modo == "cuadrada":
    for i in range(nn):
        if x[i] < 1/2*ff:
            y[i] = dc + vmax
        else:
            y[i] = dc
    #elif modo == "triangular":
    
plt.plot(x,y)
plt.xlim(0,2)
plt.ylim(-2,2)