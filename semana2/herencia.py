class Animal:
    def sonido(self):
        print("Este animal hace un sonido")

class Perro(Animal):  # Perro hereda de Animal
    def sonido(self):
        print("El perro ladra")

# Uso
p = Perro()
p.sonido()
