"""
Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.
"""
from Python.Funciones.ejercicio_6 import lista


def fun(lista):
    new_lista = []
    for num in lista:
        new_num = num **2
        new_lista.append(new_num)
    print(new_lista)

fun(lista)
