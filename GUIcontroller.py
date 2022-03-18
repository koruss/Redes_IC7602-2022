from matplotlib.figure import Figure
from Fourier import Graphic
from recorder import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import pickle
from tkinter import *
import tkinter as tk
from tkinter import ttk
class Controller(object):

    def __init__(self):
        self.recorder = Recorder(channels=2)
        self.file = ''

    def start_recording(self):
        self.file = self.recorder.open('nonblocking.wav', 'wb')
        self.file.start_recording()

    def start(self):
        self.file.start_recording()


    def pause(self):
        self.file.stop_recording()

    def hear(self):
        self.file.hear()

    def record(self):
        self.file.close()

    def mostrarFourier(self,parent,label):
        try:
            fourier = Graphic()
            for widget in parent.winfo_children():
                widget.destroy()
            figure = Figure(figsize=(7, 3.2), dpi=100)
            graphic = figure.add_subplot(111)
            plt.show()

            array = fourier.fourierArray()
            graphic.plot(array)
            canvas = FigureCanvasTkAgg(figure, parent)
            canvas.draw()
            canvas.get_tk_widget().place(x=100,y=10)


            figure2 = Figure(figsize=(7, 3.2), dpi=100)
            graphic2 = figure2.add_subplot(111)
            plt.show()
            array2 = fourier.fourierArray2()
            graphic2.plot(array2)
            canvas2 = FigureCanvasTkAgg(figure2, parent)
            canvas2.draw()
            canvas2.get_tk_widget().place(x=100, y=350)


            listatm = [self.recorder,array,array2]
            fileatm = open("autrum.atm","wb")
            pickle.dump(listatm,fileatm)
            fileatm.close()
            label.place(x=0, y=0)
            label["text"] = ""
        except:
            label.place(x=240, y=375)
            label["text"] = "Primero debes de grabar un audio"

