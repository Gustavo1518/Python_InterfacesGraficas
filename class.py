class coches:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.color = "rojo"
    

    def elcolor(self):
        return self.color   

micoche = coches("Ferrari", "105")
print(micoche.elcolor())
print(type(micoche))    