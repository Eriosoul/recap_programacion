""""
Escribir un programa que cree un diccionario simulando una cesta de la compra.
El programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar.
Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato

Lista de la compra
Artículo 1	Precio
Artículo 2	Precio
Artículo 3	Precio
…	…
Total	Coste
"""

compra = {}

continuar = True
while continuar:
    articulo = input("Nombre del articulo: ")
    precio = float(input(f"Precio de {articulo}: "))
    compra[articulo] = precio
    print(compra)

    continuar = input('¿Quieres añadir más artículos? (Si/No): ').strip().lower()
    if continuar != "si":
        break

# Mostrar lista de la compra
print("\nLista de la compra:")
for articulo, precio in compra.items():
    print(f"{articulo}: {precio:.2f}€")

# Calcular y mostrar el total
total = sum(compra.values())
print(f"\nTotal: {total:.2f}€")

