"""
Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida.
"""

def easy_mode():
    text = input("Introduce un texto: ")
    print(text[::-1])

easy_mode()

def more_steps():
    empty_reverse = ""
    text = input("introduce el texto a continuacion: ")

    for char in text:
        empty_reverse = char + empty_reverse
    print(empty_reverse)

more_steps()