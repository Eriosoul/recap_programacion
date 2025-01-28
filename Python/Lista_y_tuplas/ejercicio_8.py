"""
Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.
"""

palabra = input("Introduce la palabra: ")

nueva_palabra = ""

for i in palabra:
    print(i)
    nueva_palabra = i + nueva_palabra

print(nueva_palabra)

if nueva_palabra == palabra:
    print("Sí, es un palíndromo.")
else:
    print("No, no es un palíndromo.")