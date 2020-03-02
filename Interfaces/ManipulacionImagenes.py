import Tkinter as tk 
from Tkinter import PhotoImage, Label


root= tk.Tk()
imagen =tk.PhotoImage(file='')
etiqueta = tk.Label(root,
                    text = "Hola conacyt",
                    fg="blue",
                    font=("times", "30", "italic"),
                    image = imagen
                    )
etiqueta.pack()
root.geometry("300x150")
root.mainloop()
