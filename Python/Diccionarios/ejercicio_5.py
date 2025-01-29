"""
Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso
{'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada asignatura en el
formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas del curso,
y <créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso.
"""


asignaturas = {
    'Matemáticas': 6,
    'Física': 4,
    'Química': 5
}

for i in asignaturas:
    value = asignaturas[i]
    print(f'{i} tiene {value}')

for asignatura, creditos in asignaturas.items():
    print(f'{asignatura} tiene {creditos} créditos.')

total_creditos = sum(asignaturas.values())
print(f'\nEl número total de créditos del curso es: {total_creditos}')
