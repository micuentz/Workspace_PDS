# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 19:35:18 2024

@author: Tobias
"""

import matplotlib.pyplot as plt
import mifuncion
import numpy as np

modo = "seno"
vmax = 1
dc = 0
frec = 1
fase = 0 # En radianes
muestras = 1000
fs = 1000

x , y = mifuncion.mifuncion( modo , vmax , dc , frec , fase , muestras , fs )

# Gráficos
plt.plot(x,y)
plt.xlim(-0.1,1.1)
plt.ylim(-(vmax*1.1+dc),vmax*1.1+dc)

# dc = 1
# fase = np.pi

# x , y = mifuncion( modo , vmax , dc , frec , fase , muestras , fs )

# # Gráficos
# plt.plot(x,y)
# plt.xlim(-0.1,1.1)
# plt.ylim(-(vmax*1.1)+dc,vmax*1.1+dc)

# modo = "cuadrada"

# # Devuelvo el valor medio y la fase inicial a sus valores originales
# dc = 0
# fase = 0

# x , y = mifuncion( modo , vmax , dc , frec , fase , muestras , fs )

# # Gráficos
# plt.plot(x,y)
# plt.xlim(-0.1,1.1)
# plt.ylim(-(vmax*1.1)+dc,vmax*1.1+dc)

# muestras = 2000

# x , y = mifuncion( modo , vmax , dc , frec , fase , muestras , fs )

# # Gráficos
# plt.plot(x,y)
# plt.xlim(-0.1,2.1)
# plt.ylim(-(vmax*1.1)+dc,vmax*1.1+dc)

# modo = "diente"
# muestras = 1000

# x , y = mifuncion( modo , vmax , dc , frec , fase , muestras , fs )

# # Gráficos
# plt.plot(x,y)
# plt.xlim(-0.1,1.1)
# plt.ylim(-(vmax*1.1)+dc,vmax*1.1+dc)

# modo = "diente"
# muestras = 1000

# x , y = mifuncion( modo , vmax , dc , frec , fase , muestras , fs )

# # Gráficos
# plt.plot(x,y)
# plt.xlim(-0.1,1.1)
# plt.ylim(-(vmax*1.1)+dc,vmax*1.1+dc)

# modo = "triangular"
# frec = 1

# x , y = mifuncion( modo , vmax , dc , frec , fase , muestras , fs )

# # Gráficos
# plt.plot(x,y)
# plt.xlim(-0.1,1.1)
# plt.ylim(-(vmax*1.1)+dc,vmax*1.1+dc)

# fs = 5

# x , y = mifuncion( modo , vmax , dc , frec , fase , muestras , fs )

# # Gráficos
# plt.plot(x,y)
# plt.xlim(-0.1,1.1)
# plt.ylim(-(vmax*1.1)+dc,vmax*1.1+dc)