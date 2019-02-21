class Persona():

    def __init__(self, altura=1.65,nombre="Luis"):
        self.altura=altura
        self.nombre=nombre

    def saludo(self,mensaje):
        print(mensaje)

Luis = Persona()
Luis.saludo("Hola")
print (Luis.nombre)
Luis.nombre="Francisco"
print (Luis.nombre)
Luis.apellido="Ley"
print(Luis.apellido)

Fer = Persona()

#print (Fer.apellido)