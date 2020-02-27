import Tkinter as tk 
from Tkinter import PhotoImage, Label


root= tk.Tk()
imagen =tk.PhotoImage(file='/home/gustavo/Desktop/images.gif')
etiqueta = tk.Label(root, compound=RIGTH,
                    text = "Hola conacyt",
                    fg="blue",
                    font=("times", "30", "italic"),
                    image = imagen
                    )
etiqueta.pack()
root.mainloop()