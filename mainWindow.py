from prueba import *
from tkinter import *
from tkinter import ttk
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)




rec = Recorder(channels=2)
isStopped = False
with rec.open('nonblocking.wav', 'wb') as recfile:  
    root = Tk()
    root.title("TAREA CORTA 1 - REDES")
    root.geometry('1366x768')
    rec
    ttk.Label(root, text="Autrum").grid(column=0, row=0)
    ttk.Button(root, text="Record", command=recfile.start_recording).grid(column=2, row=0)
    ttk.Button(root, text="Pause", command=recfile.stop_recording).grid(column=3, row=0)
    ttk.Button(root, text="Continue", command=recfile.start_recording).grid(column=4, row=0)
    ttk.Button(root, text="End", command=recfile.close).grid(column=5, row=0)
    root.mainloop()