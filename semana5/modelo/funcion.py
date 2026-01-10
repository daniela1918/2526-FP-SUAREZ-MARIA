"""
Modelo del dicho rectángulo
"""

class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def obtener_dimensiones(self):
        return self.ancho, self.alto
