"""
Escribir una función que reciba una muestra de números en una lista y devuelva un diccionario con su media, varianza y desviación típica.
"""

def fun_cuadrado(lista):
    new_lista = []
    for num in lista:
        new_lista.append(num**2)
    return new_lista

def estadisticas(lista):
    stat = {}
    stat['media'] = sum(lista) / len(lista)
    stat['varianza'] = sum(fun_cuadrado(lista)) / len(lista) - stat['media'] ** 2
    stat['desviacion tipica'] = stat['varianza'] ** 0.5
    return stat


print(estadisticas([1, 2, 3, 4, 5]))
print(estadisticas([2.3, 5.7, 6.8, 9.7, 12.1, 15.6]))