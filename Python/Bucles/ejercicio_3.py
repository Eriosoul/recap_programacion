"""
Escribir un programa que pida al usuario un número entero positivo y muestre por
pantalla todos los números impares desde 1 hasta ese número separados por comas.
"""

numero = int(input("Introduce el numero: "))
impar = 0
if numero <= 0:
    print("El numero no puede ser negativo o igual a 0 ")

else:
    for i in range(numero+1):
        if i % 2 != 0:
            impar = str(i) + ","
            print(impar)

""" === OTRA SOLUCION ==="""
n = int(input("Introduce un número entero positivo: "))
for i in range(1, n+1, 2):
    print(i, end=", ")