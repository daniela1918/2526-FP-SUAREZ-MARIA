from .vehiculo import Vehiculo

# # Clase Moto hereda del Vehiculo (HERENCIA)
class Moto(Vehiculo):
    def __init__(self, marca, modelo, cilindrada):
        super().__init__(marca, modelo)
        self.cilindrada = cilindrada

    # Polimorfismo se escribe el metodo encender
    def encender(self):
        self._encendido = True
        print(f"Moto {self._marca} {self._modelo} de {self.cilindrada}cc encendida")
