from matplotlib.figure import Figure
from Fourier import Graphic
from recorder import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from tkinter import *

class Controller(object):

    def __init__(self):
        self.recorder = Recorder(channels=2)
        self.file = ''
        self.fourier = Graphic()

    def start_recording(self):
        self.file = self.recorder.open('nonblocking.wav', 'wb')
        self.file.start_recording()

    def start(self):
        self.file.start_recording()


    def pause(self):
        self.file.stop_recording()



    def record(self):
        self.file.close()

    def mostrarFourier(self,parent):
        for widget in parent.winfo_children():
            widget.destroy()
        figure = Figure(figsize=(6, 4), dpi=100)
        graphic = figure.add_subplot(111)
        plt.show()     
        array = self.fourier.fourierArray()
        graphic.plot(array)
        canvas = FigureCanvasTkAgg(figure, parent)
        canvas.draw()
        canvas.get_tk_widget().pack(side = BOTTOM, fill = BOTH, expand = True)

