"""
Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que
ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.
"""

abecedario = [chr(letra) for letra in range(ord('a'), ord('z') + 1)]

# Mostrar el abecedario
print("El abecedario es:", abecedario)

for i in range(len(abecedario), 1, -1):
    if i % 3 == 0:
        abecedario.pop(i-1)

print(abecedario)
