"""
Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.
"""

palabra = input("Introduce la palabra: ")

vocales = ['a', 'e', 'i', 'o', 'u']

for vocal in vocales:
    times = 0
    for char in palabra:
        if char == vocal:
            times +=1
    print("La vocal " + vocal + " aparece " + str(times) + " veces")
