"""
Escribir una función que reciba una muestra de números en una lista y devuelva su media.
"""

def fun(lista):
    cont = len(lista)
    nueva = sum(lista)
    result = nueva / cont
    print(f"La mitad de la lista es: {result}")

lista = [2,3,3,5,7,10]
fun(lista)

""" Otra opcion """


def calcular_media(lista):
    """Calcula la media de una lista de números."""
    if not lista:
        return "La lista está vacía."

    return sum(lista) / len(lista)


# Ejemplo de uso
lista = [2, 3, 3, 5, 7, 10]
print(f"La media de la lista es: {calcular_media(lista)}")


def fun_sin_sum(lista):
    suma = 0
    for num in lista:
        suma += num

    print(suma)
    return suma / len(lista)


lista = [2, 3, 3, 5, 7, 10]
print(f"La media de la lista es: {fun_sin_sum(lista)}")
