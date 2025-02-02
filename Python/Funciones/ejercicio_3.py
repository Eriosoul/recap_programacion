"""
Escribir una función que reciba un número entero positivo y devuelva su factorial.
"""

def fact_numb(numb):
    count = 1
    for i in range(numb):
        count *= i +1
    return count

print(fact_numb(6))
print(fact_numb(20))
