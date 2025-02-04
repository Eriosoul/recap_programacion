"""
Escribir una función que pida un número entero entre 1 y 10 y guarde en un fichero con el nombre tabla-n.txt la tabla
de multiplicar de ese número, done n es el número introducido.
"""

def fun():
    nombre = "tabla-"
    num = int(input("Introduce un numero entre 1 al 10: "))
    nombre = nombre + str(num)
    print(nombre)
    for i in range(11):
        n = num * i
        result = f'{str(num)} * {i} = {n}'
        print(result)
        with open(nombre+".txt", 'a') as file:
            file.write(result + "\n")

fun()

"""MEJORAS"""
def fun():
    """Función que guarda la tabla de multiplicar de un número en un archivo."""
    while True:
        try:
            num = int(input("Introduce un número entre 1 y 10: "))
            if 1 <= num <= 10:
                break
            else:
                print("⚠️ Número fuera de rango. Inténtalo de nuevo.")
        except ValueError:
            print("⚠️ Entrada no válida. Introduce un número entero.")

    nombre_archivo = f"tabla-{num}.txt"

    with open(nombre_archivo, 'w') as file:  # 'w' para sobrescribir en cada ejecución
        for i in range(11):
            resultado = f"{num} * {i} = {num * i}"
            print(resultado)
            file.write(resultado + "\n")

    print(f"\n✅ La tabla de multiplicar de {num} ha sido guardada en '{nombre_archivo}'.")

fun()
