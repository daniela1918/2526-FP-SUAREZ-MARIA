from modelos import Auto, Moto
from servicios import GestionVehiculos

def main():
    gestion = GestionVehiculos()

    auto1 = Auto("Toyota", "Corolla", 4)
    moto1 = Moto("Yamaha", "FZ", 250)

    gestion.agregar(auto1)
    gestion.agregar(moto1)

    print("== Encendiendo vehículos (polimorfismo) ==")
    gestion.encender_todos()

if __name__ == "__main__":
    main()

