import Tkinter as tk 
from pygments.lexers._vim_builtins import command
import tkMessageBox

class emergentes:
    def __init__(self,master):
        self.master = master
        self.principal()
        
    def principal(self):
        self.boton = tk.Button(text="Instalar",  command =self.Cancelar)
        self.boton.pack()

    def Cancelar(self):
        if tkMessageBox.askyesno('ADVERTENCIA', 'Deseas continuar'):
            tkMessageBox.showinfo('Gracias', 'la instalacion continuara')
        else:
            tkMessageBox.showwarning('Cancelo', 'se cancelo la instalacion')
        
    
root = tk.Tk()
gui = emergentes(root)
root.mainloop()