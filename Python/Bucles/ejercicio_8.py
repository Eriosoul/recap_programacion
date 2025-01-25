"""
Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo
como el de más abajo.

1
3 1
5 3 1
7 5 3 1
9 7 5 3 1
"""

num = int(input("Introduce un número positivo impar para generar el patrón: "))

if num <= 0 or num % 2 == 0:
    print("Número no válido. Debe ser positivo e impar.")
else:
    for i in range(1, num + 1, 2):  # Bucle externo para las filas (1, 3, 5, ..., num)
        for j in range(i, 0, -2):  # Bucle interno para números decrecientes en la fila
            print(j, end=" ")  # Imprime en la misma línea con un espacio
        print("")  # Salto de línea después de cada fila
