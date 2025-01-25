"""
Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
"""

num = int(input("introduce el numero y mostrare la tabla de multiplicar del 1 al 10: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

""" Mostrar todo del 1 al 10 """

for num in range(1, 11):
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")