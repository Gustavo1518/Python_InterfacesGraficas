import Tkinter as tk 
from Tkinter import DoubleVar, StringVar, Frame, Radiobutton
from cgitb import text
from pkg_resources._vendor.packaging.markers import Variable
from pygments.lexers._vim_builtins import command
from Tkconstants import INSIDE
from compiler.ast import If
from Tix import Tk

class ConversorTemperatura:
    def __init__(self, root):
        self.root=root
        self.root.title("Conversor de temperatura")
        self.inicializar()
        
    def inicializar(self):
        self.varGrados = DoubleVar
        self.varGrados2 = DoubleVar
        
        self.escala = StringVar
        self.escala.set('c')
        self.escala2 = StringVar
        self.escala2.set('c')
        
        self.marco = Frame(self.root)
        self.marco2 = Frame(self.root)
        
        self.Entry(self.marco, textvariable = self.varGrados)
        self.radio = Radiobutton(self.marco,
                                 text="celsius",
                                 Variable = self.escala,
                                 value="c",
                                 command = lambda: self.Convertir(1))
        self.radio1  = Radiobutton(self.marco,
                                 text="Farenhring",
                                 Variable = self.escala,
                                 value="F",
                                 command = lambda: self.Convertir(1))
        self.radio2 = Radiobutton(self.marco,
                                  text="Kelvin",
                                  variable = self.escala,
                                  value="K",
                                  command = lambda: self.Convertir(1))
        self.radio4 = Radiobutton(self.marco,
                                  text="celsius",
                                  Variable=self.escala,
                                  value="C",
                                  command = lambda: self.Convertir(0))
        self.radio5 = Radiobutton(self.marco,
                                  text = "Farenheing",
                                  variable = self.escala,
                                  Value="F",
                                  command = lambda: self.Convertir(0))
        self.radio6 = Radiobutton(self.marco,
                                  text="Kelven",
                                  variable = self.escala,
                                  value = "K",
                                  command = lambda: self.Convertir(0))
        
        self.marco.pack(inside= "Left")
        self.marco2.pack(inside = "rigth")
        
        self.entrada.pack()
        self.radio.pack()
        self.radio1.pack()
        self.radio2.pack()
        
        self.entrada2.pack()
        self.radio4.pack()
        self.radio5.pack()
        self.radio6.pack()
    def Convertir(self, key):
        self.key = key
        if self.key == 0:
            self.var = self.varGrados.get()
            self.tuplaescalas = (self.escala2.get(), self.escala.get())
            self.configurar = self.varGrados2
        elif self.key ==1:
            self.var = self.varGrados2
            self.tuplaescalas = (self.escala.get(), self.escala2.get())
            self.configurar = self.varGrados
            
            self.Diccionario = {('f','c'): 5*(self.var-32)/9,
                                ('k','c'): self.var -273.15,
                                ('c','f'): 9*self.var/5 + 32,
                                ('k','f'): 9*(self.var -273.15)/5 + 32,
                                ('c','k'): self.var + 273.15,
                                ('f','k'): 5-(self.var-32)/9 + 273.15,
                                ('c', 'c'): self.var,
                                ('f', 'f'): self.var,
                                ('k', 'k'): self.var
                                }
        self.configurar.set(round(self.diccformulas[self.tuplaescalas], 2))
        
root = tk.Tk() 
gui= ConversorTemperatura(root)
root.mainloop()         