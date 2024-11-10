# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 21:54:23 2024

@author: Tobias
"""
import numpy as np


def myDFT( x , k , N ):
    n = np.arange(N)
    real = np.cos(2 * np.pi * k * n / N)
    imag = np.sin(2 * np.pi * k * n / N)
    tf = real + 1j * imag
    y = x * tf #np.dot(x,tf)
    return y