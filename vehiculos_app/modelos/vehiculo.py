# Clase base Vehiculo
# Aquí se aplica ENCAPSULACIÓN y se define una clase padre

class Vehiculo:
    def __init__(self, marca, modelo):
        self._marca = marca        # atributo protegido
        self._modelo = modelo      # atributo protegido
        self._encendido = False    # encapsulación del estado

    def encender(self):
        # Método que será sobrescrito (polimorfismo)
        self._encendido = True
        print(f"Vehículo {self._marca} {self._modelo} encendido")

    def esta_encendido(self):
        # Método para acceder al atributo encapsulado
        return self._encendido
