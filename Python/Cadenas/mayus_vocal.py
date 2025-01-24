"""
Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.
"""

def vocal_text():
    text = input("Introduce la frase: ")
    vocal = input("Seleciona una vocal (a, e, i, o , u): ")
    new_text = ""
    voval_selected = vocal

    for char in text:
        if char == voval_selected:
            new_text = new_text + char.upper()
        else:
            new_text = new_text + char
    print(new_text)

vocal_text()