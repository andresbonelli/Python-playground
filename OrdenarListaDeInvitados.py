from unidecode import unidecode
import re

def ordenar_por_apellido(lista_de_nombres: list):
    """
    Ordenar alfabéticamente una lista de nombres por apellido

    :param lista_de_nombres: (list of strings) Lista de nombres a ordenar.
    :return: (list of dictionaries) Lista de nombres completos separados
            por nombre de pila y apellido en forma de pares 'key/value'.
    """
    # Lista para almacenar nombres divididos y ordenados por apellido
    splitlist = []
    for index, name in enumerate(lista_de_nombres):
        # Eliminar espacios adicionales y caracteres especiales
        name = re.sub(r'\s+', ' ', name.replace('\xa0', ' '))
        # Convertir a ASCII para facilitar la comparación
        name = unidecode(name)
        # Dividir el nombre en partes: nombre y apellido
        splitname = name.split(" ", maxsplit=2)

        # Verificar si hay más de un nombre, asumiendo que el último es el apellido
        if len(splitname) >= 3 and len(splitname[2]) >= 3:
            # Si hay más de un nombre, agregar a la lista concatenando ambos en el mismo key y separar del apellido
            splitlist.append({"nombre": splitname[0]+" "+splitname[1], "apellido": splitname[2]})
        else:
            # Si no hay más de un nombre, agregar nombre y apellido.
            splitlist.append({"nombre": splitname[0], "apellido": splitname[1]})

    # Ordenar la lista de nombres divididos por el apellido y retornar
    return sorted(splitlist, key=lambda x: x["apellido"])



if __name__ == "__main__":

    with open("invitades.txt", encoding="utf-8") as f:
        invitades = f.read().splitlines()


    lista_ordenada = ordenar_por_apellido(invitades)

    for name in lista_ordenada:
        print(name)