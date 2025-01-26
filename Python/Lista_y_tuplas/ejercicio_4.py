"""
Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva,
los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
"""

num_primitiva = []
for i in range(6):
    while True:
        try:
            numero_de_usuario = int(input(f"Introduce el número {i+1} de la primitiva: "))
            if numero_de_usuario < 1 or numero_de_usuario > 49:
                print("El número debe estar entre 1 y 49.")
            else:
                num_primitiva.append(numero_de_usuario)
                break
        except ValueError:
            print("Por favor, introduce un número válido.")

# Ordenar la lista de números
num_primitiva.sort()
print("Los números ganadores son:", num_primitiva)

def ordenar_num_primitiva(lista):
    size = len(lista)
    for ind in range(size):
        min_index = ind
        for j in range(ind + 1, size):
            if lista[j] < lista[min_index]:
                min_index = j
        # Intercambio de posiciones
        lista[ind], lista[min_index] = lista[min_index], lista[ind]
    return lista

# Mostrar la lista ordenada usando tu algoritmo manual
print("Usando algoritmo manual:", ordenar_num_primitiva(num_primitiva))