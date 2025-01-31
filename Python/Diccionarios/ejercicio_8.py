"""
Escribir un programa que cree un diccionario de traducción español-inglés.
El usuario introducirá las palabras en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción>
separados por comas. El programa debe crear un diccionario con las palabras y sus traducciones.
Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra.
Si una palabra no está en el diccionario debe dejarla sin traducir.
"""

spn_eng = {}

# Bucle para ingresar palabras
while True:
    entrada = input("Introduce las palabras en formato 'español:inglés', separadas por comas: ").strip()

    # Procesar múltiples pares
    pares = entrada.split(",")  # Separa por comas cada par de palabras

    for par in pares:
        try:
            esp, eng = par.strip().split(":")  # Separa por ":" cada palabra
            spn_eng[esp.strip()] = eng.strip()  # Añade al diccionario eliminando espacios extra
        except ValueError:
            print(f"Error en la entrada: '{par}', asegúrate de usar el formato 'palabra:traducción'.")

    # Preguntar si quiere seguir añadiendo
    continuar = input("¿Quieres añadir más palabras? (Si/No): ").strip().lower()
    if continuar != "si":
        break

# Mostrar el diccionario final
print("\nDiccionario de traducción:")
for esp, eng in spn_eng.items():
    print(f"{esp} -> {eng}")
