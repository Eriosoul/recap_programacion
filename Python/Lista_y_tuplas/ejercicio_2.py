"""
Escribir un programa que almacene las asignaturas de un curso
(por ejemplo Matemáticas, Física, Química, Historia y Lengua)
en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>,
donde <asignatura> es cada una de las asignaturas de la lista.
"""
from Python.Lista_y_tuplas.ejercicio_1 import asignaturas

for asignatura in asignaturas:
    print(f"Yo estudio: {asignatura}")