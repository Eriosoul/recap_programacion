"""
Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por
pantalla el número de euros y el número de céntimos del precio introducido.
"""

def get_euro():
    precio = input("Intoruduce el euro y sus centimos ej:5.69 recuerda usar el punto para separar los centimos: ")
    print("El euro es:",precio[:precio.find('.')], "y el centimo es: ", precio[precio.find('.')+1:])

get_euro()
