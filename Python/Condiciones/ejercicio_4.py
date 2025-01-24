"""
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
"""

def par_impar():
    try:
        numb = int(input("Introduce el numero: "))
        if numb == 0:
            print("0 es un numero neutro")
            raise
        elif numb % 2 == 0:
            print("El numero es par")
        else:
            print("El numero es impar")

    except ValueError as verror:
        print(verror)
    except Exception as err:
        print(err)

par_impar()