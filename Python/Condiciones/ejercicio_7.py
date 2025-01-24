"""
En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en
la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. Los puntos que pueden
conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas.
A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad de dinero
conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.

Nivel	Puntuación
Inaceptable	0.0
Aceptable	0.4
Meritorio	0.6 o más

Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento,
así como la cantidad de dinero que recibirá el usuario.
"""

def retrubucion():
    try:
        salario_fijo = 2400
        nivel = str(input("Introduce el nivel del empleado: ")).lower()

        if nivel == "inaceptable":
            result = 0.0 * salario_fijo
            print(f"Nivel: Inaceptable\nSu puntuación es 0.0.\nSalario total: {salario_fijo + result}€")
        elif nivel == "aceptable":
            result = 0.4 * salario_fijo
            print(f"Su salario ha subido de 2400€ a {result + salario_fijo}€")
        elif nivel == "meritario":
            result = 0.6 * salario_fijo
            print(f"Su salario ha subido de 2400€ a {result + salario_fijo}€")
        else:
            print("No se reconocio el nivel")
    except ValueError as verr:
        print("Ha introducido caracteres no validos: ", verr)
    except Exception as ex:
        print(ex)

retrubucion()