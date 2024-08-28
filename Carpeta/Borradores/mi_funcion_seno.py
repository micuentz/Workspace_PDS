# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 21:34:21 2024

@author: Tobias
"""

import numpy as np

def mi_funcion( modo = "seno" , vmax = 1 , dc = 0 , ff = 1 , pf = 0 , nn = 1000 , fs = 1000 ):

    x = np.arange(0 , nn/fs , 1/nn)
    y = np.array(len(x))
    t = len(x)

    if modo == "seno":
        y = dc + vmax * np.sin(2*np.pi*ff*x + pf)
    elif modo == "cuadrada":
        for i in range(len(x)):
            if x[i] < 1/2*ff:
                y[i] = dc + vmax
            else:
                y[i] = 0
    
    return x , y