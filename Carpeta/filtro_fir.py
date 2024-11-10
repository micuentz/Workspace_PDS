# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 16:29:24 2023

@author: tobias_guerrero
"""

from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
from pytc2.sistemas_lineales import plot_plantilla
import scipy.io as io
import warnings
warnings.filterwarnings('ignore')

coef = 10001
den_fir = 1.0

ripple = 0.01
atenuacion = 40

fs = 1000
nyq = 500
ws1 = 0.1
wp1 = 0.5
wp2 = 30.0
ws2 = 40.0

ws = np.array([ws1 , ws2])
wp = np.array([wp1 , wp2])

frecs = [0.0 , ws1 , wp1 , wp2 , ws2 , nyq]
gains = [-atenuacion,-atenuacion,-ripple,-ripple,-atenuacion,-atenuacion]
gains = 10**(np.array(gains)/20)

taps = signal.firwin2(coef , frecs , gains , window = 'tukey' , fs = fs) # boxcar , cosine , tukey

w, h = signal.freqz(taps, den_fir, worN=10000)

ww = w / np.pi * nyq

phase = np.unwrap(np.angle(h))

gd = -np.diff(np.unwrap(np.angle(h)))/np.diff(ww)

t = np.arange(0 , 10 , 0.001)
imp = np.fft.ifft(h)

mat_struct = io.loadmat('ecg.mat')
ecg_one_lead = mat_struct['ecg_lead']
ecg_one_lead = ecg_one_lead.flatten()
cant_muestras = len(ecg_one_lead)


ECG_fir = signal.lfilter(taps, den_fir, ecg_one_lead)

modulo = plt.figure()
plt.title("Filtro")
plt.plot(ww , ECG_fir)
plt.axis([0,100,-50,5])
plot_plantilla(filter_type = 'bandpass' , fpass = wp , ripple = ripple , fstop = ws , attenuation = atenuacion, fs = fs)

#fase = plt.figure()
#plt.title("Fase")
#plt.plot(ww, phase)
#plt.show()

#retardo = plt.figure()
#plt.title("Retardo")
#plt.plot(ww[1:], gd)
#plt.axis([0,500,-4,0])
#plt.show()

#resp_impulso = plt.figure()
#plt.title("Respuesta al impulso")
#plt.plot(t,imp)
#plt.show()