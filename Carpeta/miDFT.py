# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 19:33:02 2024

@author: Tobias
"""

import numpy as np

def miDFT( x ):
    
    y = np.zeros(len(x),complex)
    
    for k in range(len(x)): 
        for i in range(len(x)): 
            y[k] += x[i] * np.exp(-2j * np.pi * k * i / len(x)) 
    
    y = np.divide(y,len(y)) 
    
    return y


def miDFT2( x ):
    
    n = np.arange(len(x))
    
    k = n.reshape((len(x),1))
    
    e = np.exp(-2j * np.pi * n * k/ len(x))
    
    y = np.dot(x , e)
    
    y = np.divide(y,len(y))
    
    return y