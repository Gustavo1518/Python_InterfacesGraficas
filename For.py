#Metodo upper() convierte a mayusculas
micadena = raw_input("ingresa un texto")
for cadena in micadena:
    print(cadena.upper())
# metodo lower() convierte a minusculas
micadena2 = raw_input("ingresa un segundo texto")
for i in micadena2:
    print(i.lower())

#iteracion sobre un rango
saludo = "HOLA MUNDO"
for numero in range(len(saludo)):
    print(numero+1, saludo[numero])
#iteracion sobre una lista
hola="hola mundo"
milista = list(hola)
for elemento in milista[:]:
    milista.append(elemento*2)
print(milista)

mitupla = {"hola", 1, True}
for elemento in mitupla:
    print(elemento, "es", type(elemento))
print("*********fin del ejemplo*************") 