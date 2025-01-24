"""
Descripción:
Escribe un programa que pida al usuario una cadena de texto y luego calcule la frecuencia de aparición de cada carácter en la cadena.

Requisitos:

Ignora los espacios en blanco al contar la frecuencia.
La frecuencia debe distinguir entre mayúsculas y minúsculas (por ejemplo, A y a son diferentes).
Imprime cada carácter y su frecuencia en el formato: carácter: frecuencia.
Entrada de ejemplo:

yaml
Copiar código
Introduce una cadena: Hola Mundo
Salida de ejemplo:

makefile
Copiar código
H: 1
o: 2
l: 1
a: 1
M: 1
u: 1
n: 1
d: 1
Sugerencias:

Usa un Map o una estructura similar para almacenar los caracteres y sus frecuencias.
Recorre la cadena carácter por carácter y actualiza las frecuencias en el Map.
Para ignorar los espacios en blanco, usa una condición como if (caracter != ' ').
Finalmente, recorre el Map para imprimir el carácter y su frecuencia.
"""

def cadena_frecuencia():
    count = 0
    char = []
    cad = input(str("Introduce tu cadena: "))
    cad.replace(" ", "")
    for c in cad:
        print(c)

if __name__ == '__main__':
    cadena_frecuencia()