"""
Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
"""

while True:
    user_pass = input("Introduce tu contraseña: ")
    passw = "variable"
    if user_pass == passw:
        print("Felicidades")
        break
    else:
        print("Contraseña erronea vuelve a introducir la contraseña a continuacion \n")
