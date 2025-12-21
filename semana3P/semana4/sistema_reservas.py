# -------------------------------------------------------
# Caso del mundo real:
# Sistema simple de reservas de habitaciones en un hotel.
# Se utilizan clases para modelar habitaciones, clientes
# y el sistema de reservas.
# -------------------------------------------------------

class Habitacion:
    """
    Clase que representa una habitación de hotel.
    """
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.disponible = True

    def reservar(self):
        """Marca la habitación como no disponible."""
        if self.disponible:
            self.disponible = False
            return True
        return False


class Cliente:
    """
    Clase que representa a un cliente del hotel.
    """
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula


class SistemaReservas:
    """
    Clase que gestiona las reservas del hotel.
    """
    def __init__(self):
        self.habitaciones = []
        self.reservas = []

    def agregar_habitacion(self, habitacion):
        """Agrega una habitación al sistema."""
        self.habitaciones.append(habitacion)

    def reservar_habitacion(self, cliente, numero_habitacion):
        """Realiza la reserva si la habitación está disponible."""
        for habitacion in self.habitaciones:
            if habitacion.numero == numero_habitacion:
                if habitacion.reservar():
                    self.reservas.append((cliente, habitacion))
                    print(f"Reserva exitosa para {cliente.nombre}")
                    return
                else:
                    print("La habitación no está disponible")
                    return
        print("Habitación no encontrada")


# -------------------------------
# Ejecución del programa
# -------------------------------

# Crear sistema
sistema = SistemaReservas()

# Crear habitaciones
h1 = Habitacion(101, "Simple", 30)
h2 = Habitacion(102, "Doble", 50)

# Agregar habitaciones al sistema
sistema.agregar_habitacion(h1)
sistema.agregar_habitacion(h2)

# Crear cliente
cliente1 = Cliente("María Suárez", "0102030405")

# Realizar reserva
sistema.reservar_habitacion(cliente1, 101)
