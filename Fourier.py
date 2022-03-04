import winsound
import scipy.io.wavfile as waves 
import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack as fourier

filename = "recording1.wav"
winsound.PlaySound(filename,winsound.SND_FILENAME)


Fs,data = waves.read(filename)
Audio_m = data[:,0]
Largo = len(Audio_m)
Ts= 0.001
n = Ts*np.arange(0,Largo)



fig,ax = plt.subplots()
plt.plot(n,Audio_m)
plt.xlabel('Tiempo')
plt.ylabel('Audio')


gk = fourier.fft(Audio_m) #Aplicamos Fourier sobre el vector donde guardamos el audio
M_gk = abs(gk) #Sacamos el valor absoluto luego de aplicar Fourier
M_gk = M_gk[0:Largo//2] #Tomamos la mitad porque son 2 iguales y solo nos interesa tomar una 

F= (Fs/Largo)*np.arange(0,Largo//2)
fig,bx= plt.subplots()
plt.plot(F,M_gk)
plt.xlabel('Frecuencia', fontsize='14')
plt.ylabel('Amplitud FFT', fontsize='14')
plt.show()