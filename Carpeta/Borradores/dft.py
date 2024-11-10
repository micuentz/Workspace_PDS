# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 22:24:47 2024

@author: Tobias
"""

import numpy as np
import matplotlib.pylab as plt
import mydft

n = 1
fs = 1000
N = 1000

resp = N/fs

x = np.arange(0 , resp , 1/N)

xx = np.sin(2*np.pi*x*n)

y = mydft.myDFT(xx, 8, N)

plt.plot(xx,y)
plt.xlim(0,1)
plt.ylim(-1.05,1.05)