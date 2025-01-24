"""
Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:

Renta	Tipo impositivo
Menos de 10000€	5%
Entre 10000€ y 20000€	15%
Entre 20000€ y 35000€	20%
Entre 35000€ y 60000€	30%
Más de 60000€	45%
Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde
"""

def declaración_de_la_renta():
    salario = int(input("Introduce el salario que tiene anual: "))

    if salario < 10000:
        print("Menos de 10000€	5%")
    elif 10000 <= salario <= 20000:
        print("Entre 10000€ y 20000€	15%")
    elif 20000 <= salario <= 35000:
        print("Entre 20000€ y 35000€	20%")
    elif 35000 <= salario <= 60000:
        print("Entre 35000€ y 60000€	30%")
    else:
        print("Más de 60000€	45%")

declaración_de_la_renta()
