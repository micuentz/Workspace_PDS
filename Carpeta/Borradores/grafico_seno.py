# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 21:39:22 2024

@author: Tobias
"""

from mi_funcion_seno import mi_funcion
import matplotlib.pyplot as plt

x , y = mi_funcion("cuadrada",1,0,1,0,1000,1000)

plt.plot(x,y)
plt.xlim(0,1)
plt.ylim(-10,10)