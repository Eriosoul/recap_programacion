"""
Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
"""

def user_ages():
    try:
        age = int(input("Introduce tu edad: "))
        if age >= 18:
            print("Usted es mayor de edad")
        else:
            print("Usted es menor de edad")

    except ValueError as e:
        print("Ha introducito una letra no un numero", e)
    except Exception as ex:
        print("Ha ocurrido un error inesperado: ", ex)

user_ages()