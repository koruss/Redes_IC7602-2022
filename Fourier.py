import winsound
import scipy.io.wavfile as waves 
import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack as fourier
from pandas.core.common import flatten

filename = "nonblocking.wav"
# print(filename)
# winsound.PlaySound(filename,winsound.SND_FILENAME)


# Fs,data = waves.read(filename)
# data= list(flatten(data))
# Audio_m = data[:len(data)]
# Largo = len(Audio_m)
# Ts= 0.001
# n = Ts*np.arange(0,Largo)



# fig,ax = plt.subplots()
# plt.plot(n,Audio_m)
# plt.xlabel('Tiempo')
# plt.ylabel('Audio')


# gk = fourier.fft(Audio_m) #Aplicamos Fourier sobre el vector donde guardamos el audio
# M_gk = abs(gk) #Sacamos el valor absoluto luego de aplicar Fourier
# M_gk = M_gk[0:Largo//2] #Tomamos la mitad porque son 2 iguales y solo nos interesa tomar una 

# F= (Fs/Largo)*np.arange(0,Largo//2)
# fig,bx= plt.subplots()
# plt.plot(F,M_gk)
# plt.xlabel('Frecuencia', fontsize='14')
# plt.ylabel('Amplitud FFT', fontsize='14')
# plt.show()


class Graphic(object):    
    def __init__(self):
        self.filename = "nonblocking.wav"
        self.openWav()
        self.data = list(flatten(self.data))
        self.audio_m = self.data[:len(self.data)]
        self.largo =  len(self.audio_m)
        self.fourierData = self.fourierArray
        
    def openWav(self):
        Fs,data = waves.read(filename)
        self.rate = Fs
        self.data = data
  
    def fourierArray(self):
        arrayFourier = fourier.fft(self.audio_m)     #Aplicamos Fourier sobre el vector donde guardamos el audio
        arrayFourier = abs(arrayFourier)        #Sacamos el valor absoluto luego de aplicar Fourier
        arrayFourier = arrayFourier[0:self.largo//100] #Tomamos la mitad porque son 2 iguales y solo nos interesa tomar una
        return arrayFourier

    def fourierArray2(self):
        return self.audio_m




