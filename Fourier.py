import winsound
import scipy.io.wavfile as waves 
import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack as fourier
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)

filename = "recording1.wav"
#winsound.PlaySound(filename,winsound.SND_FILENAME)# play the selected file 


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


def plot(root):
    winsound.PlaySound(filename,winsound.SND_FILENAME)# play the selected file 
    canvas = FigureCanvasTkAgg(fig, master = root)
    canvas.draw()
    canvas.get_tk_widget().pack()
    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas,root)
    toolbar.update()
    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()

