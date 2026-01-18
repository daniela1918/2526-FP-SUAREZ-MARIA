# Clase encargada de la lógica del dicho sistema
class GestionVehiculos:
    def __init__(self):
        self.vehiculos = []

    def agregar(self, vehiculo):
        # Se agregan objetos de diferentes clases
        self.vehiculos.append(vehiculo)

    def encender_todos(self):
        # Polimorfismo: mismo método, diferente comportamiento
        for v in self.vehiculos:
            v.encender()
