"""
Servicios de cálculo matematico
"""

class RectanguloServicio:
    def __init__(self, area_minima):
        self.area_minima = area_minima

    def calcular_area(self, rectangulo):
        return rectangulo.ancho * rectangulo.alto

    def es_area_mayor(self, area):
        return area > self.area_minima
