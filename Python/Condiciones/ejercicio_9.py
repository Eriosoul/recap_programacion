"""
La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes.
Los ingredientes para cada tipo de pizza aparecen a continuación.

Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no,
y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija.
Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas.
Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.
"""

def pizza_bella_napoli():
    user = str(input("Que pizza desea vegetariana o no vegetariana: ")).lower()

    if user == "vegetariana":
        print("Puede selecionar un ingrediente mas, ingredientes vegetarianos: Pimiento y tofu.")
        ingredient = str(input("Puede añadir un ingrediente mas: "))
        print(f"Usted eligio la pizza Vegetariana con: tomate, mozzarella, {ingredient}")
    else:
        print("Puede selecionar un ingrediente mas, Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.")
        ingredient = str(input("Puede añadir un ingrediente mas: "))
        print(f"Usted eligio la pizza no vegetariana con: tomate,mozzarella, {ingredient}")

pizza_bella_napoli()

