# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 19:37:53 2024

@author: Tobias
"""
import matplotlib.pyplot as plt
import mifuncion
import miDFT
import numpy as np


N = 100
fs = 100
frec = 1

x , y = mifuncion.mifuncion("seno",1,0,frec,0,N,fs)

Y = miDFT.miDFT(y)

f = np.fft.fftfreq(N,1/fs) # Con ayuda de la función fftfreq, se obtiene el eje de frecuencias

plt.plot( x , y ) # Se grafica la función en el dominio del tiempo
plt.xlim(0,1)
plt.ylim(-2,2)
plt.title("Señal en el dominio del tiempo")

plt.figure()
plt.stem( f , np.abs(Y) )
plt.xlim(-5,5)
plt.ylim(-1,1)
plt.title("DFT calculada")

fft = np.fft.fft(y)
fft = np.divide(fft,len(fft))

plt.figure()
plt.stem( f, np.abs(fft) )
plt.xlim(-5,5)
plt.ylim(-1,1)
plt.title("FFT obtenida con Numpy")

# Y = miDFT.miDFT2(y)

# f = np.fft.fftfreq(N,1/fs) # Con ayuda de la función fftfreq, se obtiene el eje de frecuencias

# fft = np.fft.fft(y)
# fft = np.divide(fft,len(fft))

# plt.plot( x , y ) # Se grafica la función en el dominio del tiempo
# plt.xlim(0,1)
# plt.ylim(-2,2)
# plt.title("Señal en el dominio del tiempo")

# plt.figure()
# plt.stem( f , np.abs(Y) )
# plt.xlim(-5,5)
# plt.ylim(-1,1)
# plt.title("DFT calculada sin bucles")

# plt.figure()
# plt.stem( f, np.abs(fft) )
# plt.xlim(-5,5)
# plt.ylim(-1,1)
# plt.title("FFT obtenida con Numpy")

# frec = 2

# x , y1 = mifuncion("seno",1,0,frec,0,N,fs)

# y += y1

# Y = miDFT.miDFT2(y)

# fft = np.fft.fft(y)
# fft = np.divide(fft,len(fft))

# plt.plot( x , y ) # Se grafica la función en el dominio del tiempo
# plt.xlim(0,1)
# plt.ylim(-2,2)
# plt.title("Señal en el dominio del tiempo")

# plt.figure()
# plt.stem( f , np.abs(Y) )
# plt.xlim(-5,5)
# plt.ylim(-1,1)
# plt.title("DFT calculada")

# plt.figure()
# plt.stem( f, np.abs(fft) )
# plt.xlim(-5,5)
# plt.ylim(-1,1)
# plt.title("FFT obtenida con Numpy")

# frec = 1

# x , y = mifuncion("cuadrada",1,0,frec,0,N,fs)

# Y = miDFT.miDFT2(y)

# f = np.fft.fftfreq(N,1/fs) # Con ayuda de la función fftfreq, se obtiene el eje de frecuencias

# fft = np.fft.fft(y)
# fft = np.divide(fft,len(fft))

# plt.plot( x , y ) # Se grafica la función en el dominio del tiempo
# plt.xlim(0,1)
# plt.ylim(-2,2)
# plt.title("Señal en el dominio del tiempo")

# plt.figure()
# plt.stem( f , np.abs(Y) )
# plt.xlim(-10,10)
# plt.ylim(-1,1)
# plt.title("DFT calculada")

# plt.figure()
# plt.stem( f, np.abs(fft) )
# plt.xlim(-10,10)
# plt.ylim(-1,1)
# plt.title("FFT obtenida con Numpy")

# x , y = mifuncion("diente",1,0,frec,0,N,fs)

# Y = miDFT.miDFT2(y)

# f = np.fft.fftfreq(N,1/fs) # Con ayuda de la función fftfreq, se obtiene el eje de frecuencias

# fft = np.fft.fft(y)
# fft = np.divide(fft,len(fft))

# plt.plot( x , y ) # Se grafica la función en el dominio del tiempo
# plt.xlim(0,1)
# plt.ylim(-2,2)
# plt.title("Señal en el dominio del tiempo")

# plt.figure()
# plt.stem( f , np.abs(Y) )
# plt.xlim(-10,10)
# plt.ylim(-1,1)
# plt.title("DFT calculada")

# plt.figure()
# plt.stem( f, np.abs(fft) )
# plt.xlim(-10,10)
# plt.ylim(-1,1)
# plt.title("FFT obtenida con Numpy")

# x , y = mifuncion("triangular",1,0,frec,0,N,fs)

# Y = miDFT.miDFT2(y)

# f = np.fft.fftfreq(N,1/fs) # Con ayuda de la función fftfreq, se obtiene el eje de frecuencias

# fft = np.fft.fft(y)
# fft = np.divide(fft,len(fft))

# plt.plot( x , y ) # Se grafica la función en el dominio del tiempo
# plt.xlim(0,1)
# plt.ylim(-2,2)
# plt.title("Señal en el dominio del tiempo")

# plt.figure()
# plt.stem( f , np.abs(Y) )
# plt.xlim(-10,10)
# plt.ylim(-1,1)
# plt.title("DFT calculada")

# plt.figure()
# plt.stem( f, np.abs(fft) )
# plt.xlim(-10,10)
# plt.ylim(-1,1)
# plt.title("FFT obtenida con Numpy")

# r = np.random.random_sample(len(x))

# R = miDFT.miDFT2(r)

# f = np.fft.fftfreq(N,1/fs) # Con ayuda de la función fftfreq, se obtiene el eje de frecuencias

# fft = np.fft.fft(r)
# fft = np.divide(fft,len(fft))

# plt.plot( x , r ) # Se grafica la función en el dominio del tiempo
# plt.xlim(0,1)
# plt.ylim(-2,2)
# plt.title("Ruido en el dominio del tiempo")

# plt.figure()
# plt.stem( f , np.abs(R) )
# plt.xlim(-10,10)
# plt.ylim(-1,1)
# plt.title("DFT calculada")

# plt.figure()
# plt.stem( f, np.abs(fft) )
# plt.xlim(-10,10)
# plt.ylim(-1,1)
# plt.title("FFT obtenida con Numpy")