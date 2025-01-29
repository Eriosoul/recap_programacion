"""
Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'},
pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.
"""

moneda = {
    'Euro': '€',
    'Dollar': '$',
    'Yen': '¥'
}
print("Opciones disponibles:", list(moneda.keys()))

divisa = input("Que divisa desea consultar: ")

if divisa in moneda:
    valor = moneda[divisa]
    print(f"El símbolo de {divisa} es: {valor}")
else:
    print(f"No encontrado {divisa}")
    