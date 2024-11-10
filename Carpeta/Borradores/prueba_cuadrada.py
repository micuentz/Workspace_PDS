# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 22:16:59 2024

@author: Tobias
"""
import numpy as np
import matplotlib.pyplot as plt

modo = "diente"
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
elif modo == "diente":
    for i in range(int(nn/fs)):    
        y = dc + vmax*x

plt.plot(x,y)
plt.xlim(0,2)
plt.ylim(-1,1)