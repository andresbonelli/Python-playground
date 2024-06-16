from typing import List, Dict
"""
Suponer un sistema de reserva de asientos para un anfiteatro. El teatro cuenta con 10 filas de 10 asientos cada una.
Se necesita desarrollar un sistema (sin uso de bases de datos, únicamente manejo de datos de forma lógica)
que permita llevar a cabo lo siguiente:

Cargar el "mapa" de las filas y asientos. Indicando con una "X" los asientos ocupados y con una "L" los asientos libres.
Al iniciar el programa, todos los asientos deben estar libres.
Manejar la reserva de asientos contemplando que un asiento SOLO PUEDE SER RESERVADO si se encuentra en estado "L",
en caso de que esté en estado "X". se deberá permitir al comprador elegir otro asiento.
Si se encuentra en estado "L", deberá pasar automáticamente al estado x.
Para finalizar el programa se deberá ingresar un valor en particular.
Contemplar que no existe una cantidad exacta de veces que el programa se pueda ejecutar.
Contemplar que SOLO EXISTEN 10 FILAS y 10 ASIENTOS.
No se pueden vender asientos fuera de esas numeraciones. No se permite "sobreventa".
Consideraciones: No es necesaria implementación ni de IGU ni de BD.
Se evaluará 100% el manejo lógico del desarrollo de la aplicación.
Extra: En caso de que un cliente solicite visualizar cuáles son los asientos libres,
el sistema debe permitir mostrar de forma gráfica el mapa de asientos.
NO UTILIZAR IGU para este caso. Utilizar ÚNICAMENTE lógica y la salida por consola.

"""

asientos: List[List[str]] = [["[L]"] * 10 for _ in range(10)]
codigos_de_asiento_posibles: Dict = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10}


def mostrar_asientos() -> None:
    print("Asientos disponibles:")
    print(" \  A  B  C  D  E  F  G  H  I  J")
    for i, row in enumerate(asientos):
        if i < 9:
            print(f"0{i + 1} {''.join(seat for seat in row)}")
        else:
            print(f"{i + 1} {''.join(seat for seat in row)}")


print("-------- BIENVENIDO AL SISTEMA DE RESERVAS --------")
while True:
    print("1. Ver asientos disponibles")
    print("2. Reservar asiento")
    print("3. Salir del programa")
    opcion: str = input("Seleccione opción: ")
    if opcion.lower() not in ("1", "2"):
        exit()
        break
    elif opcion == "1":
        mostrar_asientos()
    elif opcion == "2":
        while True:
            print("\n Ingrese fila y asiento")
            fila: str = input("Fila (entre 1 y 10): ")
            asiento: str = input("Asiento (de A a J): ")
            if not fila or not fila.isnumeric() or int(fila) not in range(1, 11):
                print("[ERROR] - opción de fila no válida")
                continue
            elif not asiento or asiento.lower() not in codigos_de_asiento_posibles:
                print("[ERROR] - opción de asiento no válida")
                continue
            elif asientos[int(fila) - 1][codigos_de_asiento_posibles[asiento.lower()] - 1] == "[X]":
                print(f"El asiento {int(fila)}{asiento.upper()} esta ocupado, por favor elija otro")
                continue
            else:
                asientos[int(fila) - 1][codigos_de_asiento_posibles[asiento.lower()] - 1] = "[X]"
                print(f"El asiento {int(fila)}{asiento.upper()} fue reservado correctamente")
                break
