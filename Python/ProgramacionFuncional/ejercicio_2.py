"""
Escribir una función que simule una calculadora científica que permita calcular el seno,
coseno, tangente, exponencial y logaritmo neperiano.
La función preguntará al usuario el valor y la función a aplicar, y mostrará por pantalla una tabla con los enteros
de 1 al valor introducido y el resultado de aplicar la función a esos enteros.
"""
import math

def calcular_tabla(funcion, nombre):
    """Genera una tabla con los valores de la función aplicada a enteros del 1 al valor dado."""
    try:
        valor = int(input(f"Introduce un número para calcular {nombre} desde 1 hasta ese número: "))
        if valor < 1:
            print("⚠️ Error: Introduce un número mayor o igual a 1.")
            return

        print(f"\n📊 Tabla de {nombre}:")
        print(f"{'Número':<10} {'Resultado':<10}")
        print("-" * 25)
        for i in range(1, valor + 1):
            print(f"{i:<10} {funcion(i):<10.4f}")
        print("-" * 25)

    except ValueError:
        print("⚠️ Error: Debes ingresar un número entero válido.")

def seno():
    calcular_tabla(math.sin, "Seno")

def coseno():
    calcular_tabla(math.cos, "Coseno")

def tangente():
    calcular_tabla(math.tan, "Tangente")

def exponencial():
    calcular_tabla(math.exp, "Exponencial")

def logaritmo_neperiano():
    try:
        valor = int(input("Introduce un número mayor que 0 para calcular el logaritmo neperiano: "))
        if valor <= 0:
            print("⚠️ Error: El número debe ser mayor que 0.")
            return
        calcular_tabla(math.log, "Logaritmo Neperiano")
    except ValueError:
        print("⚠️ Error: Debes ingresar un número válido.")

def menu():
    print("\n🔢 MENU CALCULADORA CIENTÍFICA")
    print("1. Seno")
    print("2. Coseno")
    print("3. Tangente")
    print("4. Exponencial")
    print("5. Logaritmo Neperiano")
    print("6. Salir")

def calculadora():
    while True:
        menu()
        try:
            opcion = int(input("Selecciona qué deseas calcular: "))
            if opcion == 1:
                seno()
            elif opcion == 2:
                coseno()
            elif opcion == 3:
                tangente()
            elif opcion == 4:
                exponencial()
            elif opcion == 5:
                logaritmo_neperiano()
            elif opcion == 6:
                print("👋 Saliendo de la calculadora...")
                break
            else:
                print("⚠️ Opción no reconocida. Intenta nuevamente.")
        except ValueError:
            print("⚠️ Error: Debes ingresar un número válido.")

calculadora()
