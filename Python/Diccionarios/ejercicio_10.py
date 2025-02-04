"""
Escribir un programa que permita gestionar la base de datos de clientes de una empresa.
Los clientes se guardarán en un diccionario en el que la clave de cada cliente será su NIF,
y el valor será otro diccionario con los datos del cliente (nombre, dirección, teléfono, correo, preferente),
donde preferente tendrá el valor True si se trata de un cliente preferente.
El programa debe preguntar al usuario por una opción del siguiente menú:
(1) Añadir cliente,
(2) Eliminar cliente,
(3) Mostrar cliente,
(4) Listar todos los clientes,
(5) Listar clientes preferentes,
(6) Terminar.
En función de la opción elegida el programa tendrá que hacer lo siguiente:

Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
Preguntar por el NIF del cliente y mostrar sus datos.
Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
Terminar el programa.
"""


clientes = {}

def añadir_cliente():
    nif = input("Introduce el NIF: ").strip()
    if nif in clientes:
        print("Ese NIF ya esta en nuestra base de datos")
        return

    nombre = input("Introduce tu nombre: ").strip()
    direccion = input("Introduce tu direccion: ").strip()
    telefono = input("Introduce tu telefono: ").strip()
    correo = input("Introduce tu correo: ").strip()
    preferente = input("¿Es liente preferente si/no?").strip().lower() == "si"

    clientes[nif] = {
        "nombre": nombre,
        "dirección": direccion,
        "teléfono": telefono,
        "correo": correo,
        "preferente": preferente
    }
    print(f"✅ Cliente {nombre} añadido correctamente.")

def eliminar_cliente():
    nif = input("Introduce el NIF del cliente que se va a eliminar: ").strip()
    if nif in clientes:
        del clientes[nif]
        print(f"✅ Cliente con NIF {nif} eliminado correctamente.")
    else:
        print("⚠️ Cliente no encontrado.")

def mostrar_cliente():
    nif = input("Introduce el NIF del cliente que desea ver: ").strip()

    if nif in clientes:
        cliente = clientes[nif]
        for clave, valor in cliente.items():
            print(f"  {clave.capitalize()}: {valor}")
    else:
        print("⚠️ Cliente no encontrado.")

def listar_clientes():
    if not clientes:
        print("⚠️ No hay clientes")
        return

    print("\n📋 Lista de clientes:")
    for nif, datos in clientes.items():
        print(f"  🆔 {nif}: {datos['nombre']}")


def listar_preferentes():
    preferentes = {nif: datos for nif, datos in clientes.items() if datos["preferente"]}

    if not preferentes:
        print("⚠️ No hay clientes preferentes registrados.")
        return

    print("\n🌟 Clientes preferentes:")
    for nif, datos in preferentes.items():
        print(f"  🆔 {nif}: {datos['nombre']}")

def menu():
    """Función principal del menú."""
    while True:
        print("\n===== MENÚ CLIENTES =====")
        print("1. Añadir cliente")
        print("2. Eliminar cliente")
        print("3. Mostrar cliente")
        print("4. Listar todos los clientes")
        print("5. Listar clientes preferentes")
        print("6. Terminar")

        try:
            opcion = int(input("Selecciona una opción: "))

            if opcion == 1:
                añadir_cliente()
            elif opcion == 2:
                eliminar_cliente()
            elif opcion == 3:
                mostrar_cliente()
            elif opcion == 4:
                listar_clientes()
            elif opcion == 5:
                listar_preferentes()
            elif opcion == 6:
                print("👋 Saliendo del programa. ¡Hasta luego!")
                break
            else:
                print("⚠️ Opción no válida. Inténtalo de nuevo.")
        except ValueError:
            print("⚠️ Debes ingresar un número válido.")


# Ejecutar el menú
menu()