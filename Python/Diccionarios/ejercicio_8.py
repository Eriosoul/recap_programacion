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

# Traducir una frase
frase = input("\nIntroduce una frase en español: ")
traduccion = " ".join(spn_eng.get(palabra, palabra) for palabra in frase.split())

print("\nFrase traducida:")
print(traduccion)
