from controller import *
from tkinter import *
from tkinter import ttk
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)





root = Tk()
root.title("TAREA CORTA 1 - REDES")
root.geometry('1366x768')
ttk.Label(root, text="Autrum").grid(column=0, row=0)
ttk.Button(root, text="Record", command=start(root)).grid(column=2, row=0)
ttk.Button(root, text="Pause", command=pause(root)).grid(column=3, row=0)
ttk.Button(root, text="Continue", command=resume(root)).grid(column=4, row=0)
ttk.Button(root, text="End", command=record(root)).grid(column=5, row=0)
root.mainloop()