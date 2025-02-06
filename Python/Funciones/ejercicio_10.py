"""
Escribir una función que convierta un número decimal en binario y otra que convierta un número binario en decimal.
"""


def dec_to_bin(n):
    bin = []
    while n > 0:
        modulo = n % 2
        cociente = n // 2
        bin.append(modulo)
        n = cociente
    print(bin)
    """
    CORRECION 
    binario = []  # Lista para almacenar los residuos

    while n > 0:
        modulo = n % 2
        binario.append(modulo)
        n //= 2  # Actualiza n dividiéndolo por 2

    # Invertimos la lista para obtener el orden correcto
    binario.reverse()

    # Convertimos la lista en una cadena para mejor presentación
    print("".join(map(str, binario)))
    """

def bin_to_dec(n):
    decimal = 0

    for i, digit in enumerate(reversed(n)):
        decimal += int(digit) * ( 2 **i )
    return decimal

dec_to_bin(18)
print(bin_to_dec("10010"))
