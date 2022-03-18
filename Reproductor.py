from matplotlib.figure import Figure
from Fourier import Graphic
from recorder import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import pickle
import sounddevice as sd
from tkinter import *
from tkinter import ttk

class DeserializarController(object):
    def __init__(self):
        self.filename = "autrum.atm"

    def Deserializar(self,frame):
        try:
            Archivo = open(self.filename,"rb")
            lista = pickle.load(Archivo)

            data = lista[0]
            fs = lista[1]
            array = lista[2]
            array2 = lista[3]


            figure = Figure(figsize=(7, 3.2), dpi=100)
            graphic = figure.add_subplot(111)
            plt.show()


            graphic.plot(array)
            canvas = FigureCanvasTkAgg(figure, frame)
            canvas.draw()
            canvas.get_tk_widget().pack()

            figure2 = Figure(figsize=(7, 3.2), dpi=100)
            graphic2 = figure2.add_subplot(111)
            plt.show()

            graphic2.plot(array2)
            canvas2 = FigureCanvasTkAgg(figure2, frame)
            canvas2.draw()
            canvas2.get_tk_widget().pack()

        except:
            return 0

        sd.play(data, fs)
        status = sd.wait()