"""
Programa principal para calcular
"""

from modelo.funcion import Rectangulo
from servicios.calculo import RectanguloServicio

user_name = input("Ingrese su nombre: ")
width = float(input("Ingrese el ancho del rectángulo: "))
height = float(input("Ingrese el alto del rectángulo: "))

rectangulo = Rectangulo(width, height)
servicio = RectanguloServicio(area_minima=10)

area = servicio.calcular_area(rectangulo)
resultado = servicio.es_area_mayor(area)

print("\nResultados:")
print(f"Usuario: {user_name}")
print(f"Área del rectángulo: {area}")

if resultado:
    print("El área es mayor al mínimo establecido.")
else:
    print("El área es menor o igual al mínimo establecido.")
