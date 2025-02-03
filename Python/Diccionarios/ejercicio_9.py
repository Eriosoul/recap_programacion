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