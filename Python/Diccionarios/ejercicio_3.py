"""
Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla,
pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta.
Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.

Fruta	Precio
Plátano	1.35
Manzana	0.80
Pera	0.85
Naranja	0.70
"""

frutas = {
    "platano":	1.35,
    "manzana":	0.80,
    "pera":	0.85,
    "naranja":	0.70
}

fruta_deseada = input("Que fruta quiere: ").lower()
kilos = float(input("Cuantos kilos quiere: "))

if fruta_deseada in frutas:
    precio_kilo = frutas[fruta_deseada]
    total = precio_kilo * kilos
    print(f"El precio de {kilos} kilos de {fruta_deseada} es: {total:.2f}€")
else:
    print(f"La frutoa {fruta_deseada} no esta en la tienda")