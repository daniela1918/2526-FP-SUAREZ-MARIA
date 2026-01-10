"""""
Programa para calcular el área de un rectángulo.
El usuario ingresa el ancho y el alto, y el programa calcula el área.
También verifica si el área es mayor a un valor mínimo.
"""
print("Programa para calcular el área de un rectángulo\n")

# Solicitar datos al usuario
user_name = input("Ingrese su nombre: ")  # string
width = float(input("Ingrese el ancho del rectángulo: "))  # float and intergers
height = float(input("Ingrese el alto del rectángulo: "))  # float

# Cálculo del área
area = width * height  # float

# Definir un área mínima
minimum_area = 10  # integer

# Verificar si el área es mayor al mínimo
is_large_area = area > minimum_area  # boolean

# Mostrar resultados
print("\nResultados:")
print(f"Usuario: {user_name}")
print(f"Área del rectángulo: {area}")

if is_large_area:
    print("El área es mayor al mínimo establecido.")
else:
    print("El área es menor o igual al mínimo establecido.")
