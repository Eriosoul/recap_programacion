"""
Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función.
"""

def circulo(area):
    result = 3.1416 * (area * area)
    print(f"El area del circulo es: {result}")

def cilindro(n, a):
    result = 3.1416 * (n * n) * a
    print(f"El volumen del cilindro es {result}")

circulo(9)
cilindro(9, 6)


def circle_area(radius):
    """Función que calcula el area de un círculo.
    Parámetros
    radius: Es el radio del círculo.
    Devuelve el área del círculo de radio radius. 
    """
    pi = 3.1415
    return pi*radius**2

def cilinder_volume(radius, high):
    """Función que calcula el volumen de un cilindro.
    Parámetros
    radius: Es el radio de la base del cilindro.
    high: Es la altura del cilindro.
    Devuelve el volumen del clindro de radio radius y altura high.
    """
    return circle_area(radius)*high

print(cilinder_volume(3,5))