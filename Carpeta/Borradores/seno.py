#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 18:13:23 2024

@author: alumno
"""

import numpy as np
import matplotlib.pylab as plt

# n = 1001 Alias en fase
# n = 999 Alias en contra fase
# n = 499 y 501 Simil AM en fase y contrafase
n = 1
fs = 1000
N = 1000
phi = 0 * np.pi
# phi = 0.5 * np.pi Muestrea en punto maximo cuando n = fs / 2 = 500

resp = N/fs

x = np.arange(0 , resp , 1/N)

y = np.sin(2*np.pi*x*n + phi)

plt.plot(x,y)
plt.xlim(0,1)
plt.ylim(-1.05,1.05)