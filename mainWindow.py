
from GUIcontroller import *
from recorder import *
from tkinter import *
import tkinter as tk
from Fourier import *



rec = Recorder(channels=2)
controller = Controller()


root = Tk()
root.title("TAREA CORTA 1 - REDES")
root.geometry('1366x768')
frame = Frame(root, bg = "red")
frame.pack(expand=1, fill=BOTH)

tk.Button(root, text="Record", command= controller.start_recording).pack()
tk.Button(root, text="Pause", command=controller.pause).pack()
tk.Button(root, text="Continue", command=controller.start).pack()
tk.Button(root, text="End", command=controller.record).pack()
tk.Button(root, text="Fourier", command=lambda: controller.mostrarFourier(frame)).pack()

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


