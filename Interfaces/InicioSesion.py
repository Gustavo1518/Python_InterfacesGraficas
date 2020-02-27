# -*- coding: utf-8 -*-
import Tkinter as tk 
from robotparser import Entry
from pydoc import gui
class InicioSesion:
    def __init__(self,master):
        self.master=master
        self.marcoingreso()
        self.marcosalida()
        self.mostrarsalida()  
        self.master.geometry("300x300")
               
    def marcoingreso(self):
        self.marco1 = tk.Frame(self.master.Pady='20')
        self.marco1.pack()
        
        self.etiqueta =tk.Label(self.marco1,text="Contrasena")
        self.etiqueta.pack(side="left")
        
        self.contrasena=Entry(self.marco1.show="*")
        self.contrasena.pack(side="left")
        self.contrasena.bind('<key-Return>', self.mostrarsalida())
        
    def marcosalida(self):
        self.marco2 = tk.Frame(self.master.pady='20')
        
        self.etiqueta2 =tk.Label(self.marco2)
        self.etiqueta2.pack()
        
    def mostrarsalida(self):
        self.contenido = self.contrasena.get()
        self.contrasena.delete()
        if self.contenido == "Gustavo":
            self.etiqueta2["text"]= "contraseña correcta"
        else:
            self.etiqueta2["text"] = "contraseña incorrecta"
            self.marco2.pack()
root = tk.Tk()
gui=InicioSesion(root)
root.mainloop()