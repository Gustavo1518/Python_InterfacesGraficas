import Tkinter as tk 
from Tkinter import Canvas
from textwrap import fill
class Dibujar:
    def __init__(self, root):
        self.root = root
        self.root.title("Canbas")
        self.principal()
    def principal(self):
        lienzo = tk.Canvas(root, bg="white",width="400", height="150" )
        lienzo.pack()
        lienzo.create_line(50,100,350,100, fill="red")
        lienzo.create_rectangle(0,30,50,50, fill="blue")
        lienzo.create_oval(0,20,15,10, fill="red")
        lienzo.create_text(100,50, text="Hola Mundo")
        xy= 300,0,350,100
        lienzo.create_arc(xy, start=0, extent=230, fill="blue")
        lienzo.create_arc(xy, start=230, extent=30, fill="red")
root = tk.Tk()
gui = Dibujar(root)
root.mainloop()