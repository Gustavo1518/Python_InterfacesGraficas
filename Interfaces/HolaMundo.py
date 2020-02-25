import Tkinter as tk 
from Tkconstants import INSIDE
# Creacion de la ventana raiz
root = tk.Tk()
# Codigo de los widget
label = tk.Label(root,text="Hola Mundo Del Python!",cursor="pencil", bg="white", fg="black")
boton = tk.Button(root, text="Cerrar Ventana",fg="black",bg="white",cursor="pencil", command=root.quit)
# Codigo para hacer visibles los widgets
boton.pack()
# le pasamos parametros de anchura y lago
label.pack(padx=100, pady=100)
#Darle propiedades a la ventana
root.config(bg="lightblue")
root.title("Conacyt")
#Bloqueamos la modificacion de la ventana)
root.resizable(width=False, height=False)
# le decimos que se cierre automaticamente despues de un tiempo
#root.after(5000,root.quit)******************
# Codigo para ejecutar el ciclo
root.mainloop()
