import winsound
import scipy.io.wavfile as waves 
import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack as fourier
from pandas.core.common import flatten



class Graphic(object):    
    def __init__(self):
        self.filename = "nonblocking.wav"
        self.openWav()
        self.data = list(flatten(self.data))
        self.audio_m = self.data[:len(self.data)]
        self.largo =  len(self.audio_m)
        self.fourierData = self.fourierArray
        
    def openWav(self):
        Fs,data = waves.read(self.filename)
        self.rate = Fs
        self.data = data
  
    def fourierArray(self):
        arrayFourier = fourier.fft(self.audio_m)     #Aplicamos Fourier sobre el vector donde guardamos el audio
        arrayFourier = abs(arrayFourier)        #Sacamos el valor absoluto luego de aplicar Fourier
        arrayFourier = arrayFourier[0:self.largo//100] #Tomamos la mitad porque son 2 iguales y solo nos interesa tomar una
        return arrayFourier

    def fourierArray2(self):
        return self.audio_m




