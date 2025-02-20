"""
Escribir una función que simule una calculadora científica que permita calcular el seno,
coseno, tangente, exponencial y logaritmo neperiano.
La función preguntará al usuario el valor y la función a aplicar, y mostrará por pantalla una tabla con los enteros
de 1 al valor introducido y el resultado de aplicar la función a esos enteros.
"""
#  Seno: sen(α) = y r = PQ r
def seno():
    cateto_opuesto = float(input("Introduce el cateto opuesto: "))
    hipotenusa = float(input("Introduce la hipotenusa: "))
    if hipotenusa == 0:  # Evitar división por cero
        print("⚠️ Error: La hipotenusa no puede ser 0.")
        return None

    resultado_seno = cateto_opuesto / hipotenusa
    print(f"✅ El seno del ángulo es: {resultado_seno:.4f}")
    return resultado_seno

#  Coseno: sen(α) = x r = OQ r
def coseno():
    cateto_adyacente = float(input("Introduce el cateto opuesto: "))
    hipotenusa = float(input("Introduce la hipotenusa: "))
    if hipotenusa == 0:  # Evitar división por cero
        print("⚠️ Error: La hipotenusa no puede ser 0.")
        return None

    resultado_coseno = cateto_adyacente / hipotenusa
    print(f"✅ El seno del ángulo es: {resultado_coseno:.4f}")
    return resultado_coseno

def tangente(r_seno, r_coseno):
    cateto_opuesto = float(input("Introduce el cateto opuesto: "))
    cateto_adyacente = float(input("Introduce la hipotenusa: "))
    if cateto_adyacente == 0:  # Evitar división por cero
        print("⚠️ Error: La hipotenusa no puede ser 0.")
        return None

    resultado_tang = cateto_opuesto / cateto_adyacente
    print(f"✅ El seno del ángulo es: {resultado_tang:.4f}")
    return resultado_tang

def exponencial():
    pass
def logaritmo_neperiano():
    pass

def menu():
    print("MENU")
    print("1. SENO")
    print("2. COSENO")
    print("3. TANGENTE")
    print("4. L.NEPERIANO")
    print("5. SALIR ")

def calculadora():
    while True:
        menu()
        opcion = int(input("Seleciona que desea calcular: "))
        if opcion == 1:
            seno()
        elif opcion == 2:
            coseno()
        elif opcion == 3:
            tangente()
        elif opcion == 4:
            logaritmo_neperiano()
        elif opcion == 5:
            break
        else:
            print("Opcion no reconocida ")

calculadora()