"""
Escribir un programa que gestione las facturas pendientes de cobro de una empresa. Las facturas se almacenarán en un
diccionario donde la clave de cada factura será el número de factura y el valor el coste de la factura.
El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar.
Si desea añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá al diccionario.
Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario.
Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.
"""

diccionario = {}

continuar = True
while continuar:
    print("\n==============MENU================\n")
    print("1.==============Añadir Factura=======")
    print("2.==============Pagar Factura =======")
    print("3.==============Terminar=============")
    option = int(input("Seleciona una opcion: "))
    if option == 1:
        num_factura = int(input("Intorduce el numero de la factura: "))
        precio = float(input("Introduce coste de dicha factura: "))
        diccionario[num_factura] = precio
        print(f"Se ha añaido la factura al diccionario: {diccionario}")
    elif option == 2:
        print(diccionario)
        num_factura = int(input("Introduce el numero de la facuta que desea pagar: "))
        if num_factura in diccionario:
            eliminado = diccionario.pop(num_factura)
            print(f"Ha pagado la factura {eliminado}")
        print(diccionario)
    elif option == 3:
        continuar = input('¿Estas seguro de que deseas salir? (Si/No): ').strip().lower()
        if continuar == "si":
            break
    else:
        print("Se ha producido un error")


"""MEJORA"""

# Diccionario para almacenar facturas
facturas = {}

# Variables para el control de los montos
total_pendiente = 0
total_cobrado = 0

while True:
    print("\n===== MENÚ =====")
    print("1. Añadir Factura")
    print("2. Pagar Factura")
    print("3. Salir")

    try:
        opcion = int(input("Selecciona una opción: "))

        if opcion == 1:
            num_factura = input("Introduce el número de factura: ")
            if num_factura in facturas:
                print("⚠️ La factura ya existe.")
                continue

            try:
                precio = float(input("Introduce el coste de la factura: "))
                if precio <= 0:
                    print("⚠️ El precio debe ser un número positivo.")
                    continue
                facturas[num_factura] = precio
                total_pendiente += precio
                print(f"✅ Factura {num_factura} añadida con un costo de {precio:.2f}€.")
            except ValueError:
                print("⚠️ Ingresa un valor numérico válido para el coste.")

        elif opcion == 2:
            if not facturas:
                print("⚠️ No hay facturas pendientes.")
                continue

            print("\nFacturas pendientes:")
            for num, costo in facturas.items():
                print(f"📄 Factura {num}: {costo:.2f}€")

            num_factura = input("Introduce el número de la factura a pagar: ")

            if num_factura in facturas:
                monto_pagado = facturas.pop(num_factura)
                total_pendiente -= monto_pagado
                total_cobrado += monto_pagado
                print(f"✅ Factura {num_factura} pagada por {monto_pagado:.2f}€.")
            else:
                print("⚠️ La factura no existe.")

        elif opcion == 3:
            salir = input("¿Estás seguro de que deseas salir? (Si/No): ").strip().lower()
            if salir == "si":
                print(f"\n💰 Total cobrado: {total_cobrado:.2f}€")
                print(f"💼 Total pendiente: {total_pendiente:.2f}€")
                print("✅ Saliendo del programa.")
                break

        else:
            print("⚠️ Opción no válida. Elige una opción del 1 al 3.")

    except ValueError:
        print("⚠️ Ingresa un número válido.")

