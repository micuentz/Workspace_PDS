# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 19:29:53 2023

@author: tobias_guerrero
"""

from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
from pytc2.sistemas_lineales import plot_plantilla
import scipy.io as io
import warnings
warnings.filterwarnings('ignore')

coef = 3001
den_fir = 1.0

ripple = 0.5
atenuacion = 40

fs = 1000
nyq = 500
ws1 = 0.1
wp1 = 0.5
wp2 = 30.0
ws2 = 40.0

ws = np.array([ws1 , ws2])
wp = np.array([wp1 , wp2])

#### Diseño Filtro IIR ####

num , den = signal.iirdesign(wp , ws , ripple , atenuacion, ftype = "butter", output = 'ba', fs = fs)

sos = signal.iirdesign(wp , ws , ripple , atenuacion, ftype = "butter", output = 'sos', fs = fs)

###########################

#### Diseño Filtro FIR ####

frecs = [0.0 , ws1 , wp1 , wp2 , ws2 , nyq]
gains = [-atenuacion,-atenuacion,-ripple,-ripple,-atenuacion,-atenuacion]
gains = 10**(np.array(gains)/20)

taps = signal.firwin2(coef , frecs , gains , window = 'tukey' , fs = fs) # boxcar , cosine , tukey

#### Levanto la señal de ECG ####

mat_struct = io.loadmat('ecg.mat')
ecg_one_lead = mat_struct['ecg_lead']
ecg_one_lead = ecg_one_lead.flatten()
#ecg_one_lead = ecg_one_lead[10000:11000]
cant_muestras = len(ecg_one_lead)

fig_sz_x = 10
fig_sz_y = 7
fig_dpi = 100 # dpi

###########################

#### Aplico el filtro ####

regs_interes = ( 
        np.array([5, 5.2]) *60*fs, # minutos a muestras
        np.array([12, 12.4]) *60*fs, # minutos a muestras
        np.array([15, 15.2]) *60*fs, # minutos a muestras
        [4000, 5500], # muestras
        [10e3, 11e3], # muestras
)

ECG_fir = signal.lfilter(taps, den_fir, ecg_one_lead)
#ECG_f_iir = signal.sosfiltfilt(sos, ecg_one_lead)
ECG_f_iir = signal.sosfilt(sos, ecg_one_lead)

demora = int((coef - 1) / 2)

for ii in regs_interes:
    
    # intervalo limitado de 0 a cant_muestras
    zoom_region = np.arange(np.max([0, ii[0]]), np.min([cant_muestras, ii[1]]), dtype='uint')
    
    plt.figure(figsize=(fig_sz_x, fig_sz_y), dpi= fig_dpi, facecolor='w', edgecolor='k')
    #plt.plot(zoom_region, ECG_fir[zoom_region + demora], label='Filtro FIR', linewidth=2)
    plt.plot(zoom_region, ecg_one_lead[zoom_region], label='ECG', linewidth=2)
    plt.plot(zoom_region, ECG_f_iir[zoom_region], label='Filtro IIR')
    #plt.plot(zoom_region, ECG_f_butt[zoom_region + demora], label='Win')
    
    plt.title('ECG filtrado de ' + str(ii[0]) + ' a ' + str(ii[1]) )
    plt.ylabel('Adimensional')
    plt.xlabel('Muestras (#)')
    
    axes_hdl = plt.gca()
    axes_hdl.legend()
    axes_hdl.set_yticks(())
            
    plt.show()