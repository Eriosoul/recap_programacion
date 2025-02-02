"""
Escribir una función que calcule el total de una factura tras aplicarle el IVA.
La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura.
Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.
"""

def factura_IVA(factura, IVA=21):
    """Calcula el total de una factura aplicando el IVA."""
    total = factura + (factura * IVA / 100)
    return total

print(factura_IVA(9000, 5))
print(factura_IVA(9000))


def invoice(amount, vat=21):
    """Función de aplica el IVA a una factura.
    Parametros
    amount: Es la cantidad sin IVA
    vat: Es el porcentaje de IVA
    Devuelve el total de la factura una vez aplicado el IVA.
    """
    return amount + amount*vat/100

print(invoice(1000,10))
print(invoice(1000))