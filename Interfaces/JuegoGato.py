import Tkinter as tk 
from Tkinter import PhotoImage, Label, Button

class Gato:
    def __init__(self, root):
        self.root=root
        self.Inicio()
    def Inicio(self):
        self.root.title("Juego del gato")
        self.marcoinicio = tk.Frame(self.root)
        self.marcoinicio.grid()
        
        imagen = tk.PhotoImage(file="/home/gustavo/Desktop/gato.jpg")
        bienvenida = tk.Label(self.marcoinicio, image = imagen)
        bienvenida.grid(row=0, column=0)
        bienvenida.image= imagen
        
        NuevaP = tk.Button(self.marcoinicio, text="Nueva partida", fg="blue", bg="white",
                           command = lambda: self.cambiarpantalla('a'), anchor='w').grid(row=1, column=0, stichy='ew')
        Records = tk.Button(self.marcoinicio, text="Puntaje", fg="blue", bg="white",
                            anchor='w', command = self.btnrecords).grid(row=2, column=0, stichy='ew')
        salir = tk.Button(self.marcoinicio, text="salir del juego", fg="blue", bg="white",
                          anchor='w', command = self.root.quit).grid(row=3, column=0, stichy='ew')
        
    def Datos(self):
        self.title("Jugadores")
        self.marcodatos = tk.Frame(self.root)
        self.marcodatos.grid()
        
        self.jugador1 = tk.Label(self.marconombres, text="jugador1", fg="blue", bg="white").grid(row=0, column=0)
        self.jugador2 = tk.Label(self.marconombres, text="jugador2", fg="blue", bg="white").grid(row=0, column=0)
        
        nombre1 = tk.Entry(self.marconombres,width=40, textVariable=self.jug1)
        nombre1.grid(row=0, column=1, stichy='nsew')
        nombre2 = tk.Entry(self.marconombres, width=40, textVariable=self.jug2)
        nombre2.grid(row=1, column=1, stichy='nsew')
        
        comenzar = tk.Button(self.marconombres, text="comenzar", fg="blue", bg="white",
                             command = lambda: self.cambiarpantalla('b'), anchor="w").grid(row=2, column=0,stichy="ew", columnspan=2)
        regresar= tk.Button(self.marconombres, text="regresar", fg="blue", bg="white",
                             command = lambda: self.cambiarpantalla('c'), anchor="w").grid(row=3, column=0,stichy="ew", columnspan=2)
        salir = tk.Button(self.marconombres, text="salir", fg="blue", bg="white",
                          command = self.root.quit, anchor='w').grid(row=3, column=0,stichy="ew", columnspan=2)
        
    def Partida(self):
        self.title("Partida")
        self.marcopartida = tk.Frame(self.root)
        self.marcopartida.grid()
        
        self.casillas = []
        k=0
        for i in range (3):
            for j in range (3):
                self.casillas.append(Button(self.marcopartida, fg="blue", bg="white", bd=1,width=5,
                                            command = lambda e=k: self.mostrarcasilla(e)))
                self.casillas[k].grid(row=i, column = j)
                k+=1
            jugarOtraVez = tk.Button(self.marcopartida, text="Jugar de nuevo", fg="blue", bg="white",
                                     command = lambda: self.cambiarpantalla('d'), anchor='w').grid(row=4, column=0,stichy='ew', columnspan=3)
            salir = tk.Button(self.marcopartida, text="salir del juego", fg="blue", bg="white",
                              command = self.root.quit, anchor="w").grid(row=5, column=0, stichy="ew", columnspan=3)
            
root = tk.Tk()
root.mainloop()