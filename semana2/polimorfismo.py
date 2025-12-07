class Gato:
    def sonido(self):
        return "Miau"

class Vaca:
    def sonido(self):
        return "Muu"

# Polimorfismo
def hacer_sonido(animal):
    print(animal.sonido())

hacer_sonido(Gato())
hacer_sonido(Vaca())

