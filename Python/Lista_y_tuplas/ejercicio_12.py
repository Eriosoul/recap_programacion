"""
Escribir un programa que almacene las matrices
     ( 123)
A = ( 456 )  y B

en una lista y muestre por pantalla su producto.
Nota: Para representar matrices mediante listas usar listas anidadas, representando cada vector fila en una lista.
"""

a = [[1,2,3], [4,5,6]]
b = [[-1, 0], [0, 1], [1, 1]]

result = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]

for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            result[i][j] += a[i][k] * b[k][j]

for fila in result:
    print(fila)
