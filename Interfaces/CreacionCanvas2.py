import Tkinter as tk 
from Tkinter import Canvas
from textwrap import fill
from pygments.lexers._vim_builtins import command
class Dibujar:
    def __init__(self, root):
        self.root = root
        self.root.title("Canbas")
        self.principal()
    def principal(self):
        self.lienzo = tk.Canvas(root, bg="white",width="400", height="150" )
        self.lienzo.pack()
        
        boton = tk.Button(self.root, text="Dibujar", command= self.Dibujo)
        self.lienzo.create_window(200,10, window=boton)
        
    def Dibujo(self):
        self.lienzo.bind("<B1 Motion>",
                         lambda e: self.lienzo.create_oval(
                             e.x-2,
                             e.y-2,
                             e.x+2,
                             e.y+2,
                             fill="black"
                             ))
        
root = tk.Tk()
gui = Dibujar(root)
root.mainloop()