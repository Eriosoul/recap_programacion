"""
Escribir un programa que pida al usuario dos números y muestre por pantalla su división.
Si el divisor es cero el programa debe mostrar un error.
"""

def numb_div():
    num1 = int(input("Introduce el primer numero: "))
    num2 = int(input("Introduce el segundo numero: "))

    try:
        result = num1 / num2
        print(result)
    except ZeroDivisionError as zero:
        print("No se puede dividir con 0: ", zero)
    except Exception as e:
        print(e)

numb_div()