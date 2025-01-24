"""
Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas,
y muestre por pantalla cada uno de los productos en una línea distinta.
"""

def get_productos():
    productos = input("Introduce los productos separado por comas: ")
    print('\n'.join(productos.split(',')))

get_productos()

