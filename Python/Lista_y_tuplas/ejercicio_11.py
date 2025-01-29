"""
Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2)
en dos listas y muestre por pantalla su producto escalar.
"""

vector1 = [1, 2, 3]
vector2 = [-1, 0, 2]

# Calcular el producto escalar
producto_escalar = sum(a * b for a, b in zip(vector1, vector2))
print(producto_escalar)
