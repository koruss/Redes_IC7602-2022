
from GUIcontroller import *
from recorder import *
from Reproductor import *
from tkinter import *
import tkinter as tk
from Fourier import *
from tkinter import ttk

rec = Recorder(channels=2)
controller = Controller()
DeserializarController = DeserializarController()
root = Tk()
root.title("TAREA CORTA 1 - REDES")
root.geometry('900x768')
frame = Frame(root, bg = "red")
frame.pack(expand=1, fill=BOTH)





label = tk.Label(root, bg = "red", text="Grabe un audio!",font=('Helvetica bold',20),
anchor="center")
label.place(x=350,y=375)


recordB = ttk.Button(root, text="Record", command=lambda:[message(1)])
pauseB = ttk.Button(root, text="Pause", command= lambda:[message(2)])
continueB = ttk.Button(root, text="Continue", command= lambda:[message(3)])
endB = ttk.Button(root, text="End", command= lambda:[message(4)])
hearB = ttk.Button(root, text="Hear", command= lambda:message(5))
atmB = ttk.Button(root, text=".atm", command= lambda:message(6))
fourierB = ttk.Button(root, text="Fourier", command=lambda:[controller.mostrarFourier(frame,label)])


recordB.place(x=50,y=700)
pauseB.place(x=125,y=700)
continueB.place(x=200,y=700)
endB.place(x=275,y=700)
hearB.place(x=400,y=700)
fourierB.place(x=700,y=700)

atmB.place(x=775,y=700)


def message(val):
    if val == 1:
        for widgets in frame.winfo_children():
            widgets.destroy()
        label.place(x=400,y=375)
        label["text"] = "Grabando.."
        controller.start_recording()
    elif val == 2:
        label["text"] = "Pausado!"
        controller.pause()
    elif val == 3:
        label["text"] = "Grabando.."
        controller.start()
    elif val == 4:
        label.place(x=370, y=375)
        label["text"] = "Audio guardado!"
        controller.record()
    elif val == 5:
        label["text"] = "Reproducido!"
        controller.hear()
    else:
        DeserializarController.Deserializar(label)

# fig,ax = plt.subplots()
# x = np.arange(0,2*1024,2)
# line, = ax.plot(x, np.random.rand(1024),'r')
# ax.set_ylim(-32770,32770)
# ax.ser_xlim = (0,1024)
# fig.show()



# Esta es la forma correcta de trabajar 

# figure = Figure(figsize=(6, 4), dpi=100)
# graphic = figure.add_subplot(111)
# plt.show()
  
# array = fouriercito.fourierArray()
# graphic.plot(array)
# canvas = FigureCanvasTkAgg(figure, frame)
# canvas.draw()
#canvas.get_tk_widget().pack(side = BOTTOM, fill = BOTH, expand = True)
#label1 = tk.Label(frame, text="FASDADADADASDADAD")

#label1.place(relx = 0.0,rely = 1.0,anchor ='sw')


root.mainloop()


