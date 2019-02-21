class Perro():
    def caminar(self):
        print("camina en 4 patas")

class Pato():
    def caminar(self):
        print("camino en 2 patas o vuelo y exploto un auto con mi rasho laser!")

class Caracol():
    def arrastrar(self):
        print("Yo me arrastro alv")

def mover(animal):
    animal.caminar()

agustin = Perro()

donald = Pato()

gary = Caracol()

agustin.caminar()
donald.caminar()
gary.arrastrar()

mover(agustin)
mover(donald)
mover(gary)