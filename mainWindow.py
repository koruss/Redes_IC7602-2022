
from GUIcontroller import *
from recorder import *
from Reproductor import *
from tkinter import *
import tkinter as tk
from Fourier import *
from tkinter import ttk

class MainGUI:
    def __init__(self, root):
        self.root= root 
        self.root.title("TAREA CORTA 1 - REDES") # Se setea la pantalla principal 
        self.root.geometry('900x768')
        self.root.resizable(False, False)

        self.frame = Frame(root, bg = "red")
        self.frame.pack(expand=1, fill=BOTH)
        self.label = tk.Label(root, bg = "red", text="Grabe un audio!",font=('Helvetica bold',20), # Se setea un label para representar los estado de la app
        anchor="center")
        self.label.place(x=350,y=375)

        self.recordB = ttk.Button(root, text="Record", command=lambda:[self.message(1)])
        self.pauseB = ttk.Button(root, text="Pause", command= lambda:[self.message(2)])
        self.continueB = ttk.Button(root, text="Continue", command= lambda:[self.message(3)])
        self.endB = ttk.Button(root, text="End", command= lambda:[self.message(4)])
        self.hearB = ttk.Button(root, text="Hear", command= lambda:self.message(5))
        self.atmB = ttk.Button(root, text=".atm", command= lambda:self.message(6))
        self.fourierB = ttk.Button(root, text="Fourier", command=lambda:[self.controller.mostrarFourier(self.frame,self.label)])

        self.recordB.place(x=50,y=700)
        self.pauseB.place(x=125,y=700)
        self.continueB.place(x=200,y=700)
        self.endB.place(x=275,y=700)
        self.hearB.place(x=400,y=700)
        self.fourierB.place(x=700,y=700)
        self.atmB.place(x=775,y=700)

        self.controller = Controller()
        self.DeserializarController = DeserializarController()

    def message(self,val):
        if val == 1:
            for widgets in self.frame.winfo_children():
                widgets.destroy()
            self.label.place(x=400,y=375)
            self.label["text"] = "Grabando.."
            self.controller.start_recording()
        elif val == 2:
            self.label["text"] = "Pausado!"
            self.controller.pause()
        elif val == 3:
            self.label["text"] = "Grabando.."
            self.controller.start()
        elif val == 4:
            self.label.place(x=370, y=375)
            self.label["text"] = "Audio guardado!"
            self.controller.record()
        elif val == 5:
            self.label["text"] = "Reproducido!"
            self.controller.hear()
        else:
            self.DeserializarController.Deserializar(self.frame)

root = Tk()
gui = MainGUI(root)
root.mainloop()