"""
Para tributar un determinado impuesto se debe ser mayor de 16 años
y tener unos ingresos iguales o superiores a 1000 € mensuales.
Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales
y muestre por pantalla si el usuario tiene que tributar o no.
"""

def trib():
    try:
        age = int(input("Introduce tu edad: "))
        salary = float(input("Introduce tu salario mensual: "))
        if age >= 15 and salary >= 1000:
            print("Usted debe tributar")
        else:
            print("Usted no debe tributar")

    except ValueError as verr:
        print("Hay valores incorrectos: ", verr)
    except Exception as ex:
        print("Ha occurdio un error: ", ex)

trib()