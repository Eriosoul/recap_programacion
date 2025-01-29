"""
Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario.
Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección>
y su número de teléfono es <teléfono>.
"""

usuario = {
    "nombre": "",
    "edad": "",
    "direccion": "",
    "telefono": ""
}

nombre = input("Introduce tu nombre: ")
edad = input("Introduce tu edad: ")
direccion = input("Introduce tu direccion: ")
telefono = input("Introduce tu telefono: ")

usuario.update({"nombre": nombre, "edad": edad, "direccion": direccion, "telefono": telefono})
print(f"{usuario['nombre']} tiene {usuario['edad']}, vive en {usuario['direccion']} y su telefono es {usuario['telefono']}")


"""=== OTRA FORMA ==="""

nombre = input("Introduce tu nombre: ")
edad = input("Introduce tu edad: ")
direccion = input("Introduce tu dirección: ")
telefono = input("Introduce tu teléfono: ")

usuario = {
    "nombre": nombre,
    "edad": edad,
    "direccion": direccion,
    "telefono": telefono
}


print(f"{usuario['nombre']} tiene {usuario['edad']} años, vive en {usuario['direccion']} y su teléfono es {usuario['telefono']}.")
