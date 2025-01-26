"""
Escribir un programa que almacene en una lista los números del 1 al 10
y los muestre por pantalla en orden inverso separados por comas.
"""

lista_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

size = len(lista_num)

# Implementación manual del algoritmo de selección
for ind in range(size):
    min_index = ind
    for j in range(ind + 1, size):
        if lista_num[j] > lista_num[min_index]:
            min_index = j
    # Intercambiar elementos
    lista_num[ind], lista_num[min_index] = lista_num[min_index], lista_num[ind]

print(lista_num)