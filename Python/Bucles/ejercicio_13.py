"""
Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.
"""
while True:
    words = input("Introduce la palabra: ").lower()
    if words == "salir":
        break
    if words:  # Verifica que no sea vacío
        print(words)
    else:
        print("No has introducido ninguna palabra.")