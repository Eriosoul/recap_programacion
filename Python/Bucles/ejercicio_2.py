"""
Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos
los años que ha cumplido (desde 1 hasta su edad).
"""

edad = int(input("Introduce tu edad: "))
count = 0
for _ in range(1, edad):
    count +=1
    print(count)