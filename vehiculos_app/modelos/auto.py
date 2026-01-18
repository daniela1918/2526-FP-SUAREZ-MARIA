from modelos.vehiculo import Vehiculo

# Clase Auto hereda del Vehiculo
class Auto(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas

    # Polimorfismo: se sobrescribe el método encender
    def encender(self):
        self._encendido = True
        print(f"Auto {self._marca} {self._modelo} encendido con {self.puertas} puertas")
