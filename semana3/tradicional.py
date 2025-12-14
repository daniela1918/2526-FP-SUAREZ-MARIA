# Programacion tradicional para poder calcular el promedio semanal del clima

def ingresar_temperaturas():
    """
    Función que solicita al usuario las temperaturas diarias
    de una semana y las guarda en una lista.
    """
    temperaturas = []
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    for dia in dias:
        temp = float(input(f"Ingrese la temperatura del {dia}: "))
        temperaturas.append(temp)

    return temperaturas


def calcular_promedio(temperaturas):
    """
    Función que calcula el promedio de una lista de temperaturas.
    """
    suma = sum(temperaturas)
    promedio = suma / len(temperaturas)
    return promedio


def main():
    """
    Función principal del programa.
    """
    temperaturas = ingresar_temperaturas()
    promedio_semanal = calcular_promedio(temperaturas)

    print(f"\nEl promedio semanal de temperatura es: {promedio_semanal:.2f} °C")
# Ejecución del programa
main()

