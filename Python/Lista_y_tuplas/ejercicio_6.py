"""
Escribir un programa que almacene las asignaturas de un curso
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado
en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las
asignaturas que el usuario tiene que repetir.
"""
from Python.Lista_y_tuplas.ejercicio_1 import asignaturas

notas = []

for asignatura in asignaturas:
    nota = float(input(f"¿Que nota has sacado en {asignatura}?: "))
    notas.append(nota)

reprobadas = []
for i in range(len(asignaturas)):
    if notas[i] < 5:  # Si la nota es menor que 5, se considera reprobada
        reprobadas.append(asignaturas[i])

# Mostrar asignaturas que deben repetirse
if reprobadas:
    print("Debes repetir las siguientes asignaturas:")
    for asignatura in reprobadas:
        print(f"- {asignatura}")
else:
    print("¡Felicidades! No tienes que repetir ninguna asignatura.")

