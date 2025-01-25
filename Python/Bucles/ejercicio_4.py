"""
Escribir un programa que pida al usuario un número entero positivo y muestre por
pantalla la cuenta atrás desde ese número hasta cero separados por comas.
"""

numero = int(input("Introduce un numero entero positivo: "))

if numero <= 0:
    print("Error esto no es un numero entero positivo")
else:
    for i in range(numero, -1, -1):
        print(i, end=",")