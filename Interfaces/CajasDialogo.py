import Tkinter as tk 
from pygments.lexers._vim_builtins import command
import tkMessageBox
from Tkinter import PhotoImage, Image

class emergentes:
    def __init__(self,master):
        self.master = master
        self.principal()
        
    def principal(self):
        self.boton = tk.Button(text="Instalar",  command =self.Cancelar, bg="SteelBlue3")
        self.boton.place(x=10, y=100)
        
        self.boton1 = tk.Button(text="Cancelar", command = root.quit, bg="SteelBlue3")
        self.boton1.place(x=300, y=100)

    def Cancelar(self):
        if tkMessageBox.askyesno('ADVERTENCIA', 'Deseas continuar'):
            tkMessageBox.showinfo('Gracias', 'la instalacion continuara')
        else:
            tkMessageBox.showwarning('Cancelo', 'se cancelo la instalacion')
root = tk.Tk()
gui = emergentes(root)
root.title("Instalar Software conacyt")
root.config(bg="sky blue")
root.geometry("400x150")
root.resizable(width= False, height = False)
root.mainloop()