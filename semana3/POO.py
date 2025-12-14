# Programación Orientada a Objetos, este programa para es para calcular el promedio semanal del clima


class ClimaDiario:
    """
    Clase que representa la información diaria del clima.
    Aplica encapsulamiento.
    """

    def __init__(self, dia):
        self.__dia = dia
        self.__temperatura = 0.0

    def ingresar_temperatura(self):
        """
        Método para ingresar la temperatura del día.
        """
        self.__temperatura = float(input(f"Ingrese la temperatura del {self.__dia}: "))

    def obtener_temperatura(self):
        """
        Método para obtener la temperatura del día.
        """
        return self.__temperatura


class ClimaSemanal(ClimaDiario):
    """
    Clase que representa el clima semanal.
    Aplica herencia al extender ClimaDiario.
    """

    def __init__(self):
        self.dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        self.registro = []

    def registrar_temperaturas(self):
        """
        Método para registrar las temperaturas de toda la semana.
        """
        for dia in self.dias:
            clima = ClimaDiario(dia)
            clima.ingresar_temperatura()
            self.registro.append(clima)

    def calcular_promedio_semanal(self):
        """
        Método que calcula el promedio semanal.
        """
        total = sum(dia.obtener_temperatura() for dia in self.registro)
        return total / len(self.registro)


# Ejecución del programa
clima_semanal = ClimaSemanal()
clima_semanal.registrar_temperaturas()
promedio = clima_semanal.calcular_promedio_semanal()

print(f"\nEl promedio semanal de temperatura es: {promedio:.2f} °C")
