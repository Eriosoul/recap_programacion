"""
Escribir un programa que almacene las asignaturas de un curso
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado
en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde
<asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas
introducidas por el usuario.
"""
from Python.Lista_y_tuplas.ejercicio_1 import asignaturas

notas = []
for asignatura in asignaturas:
    nota = input(f"que nota has sacado en {asignatura}?")
    notas.append(nota)
for i in range(len(asignaturas)):
    print("En " + asignaturas[i] + " has sacado " + notas[i])
