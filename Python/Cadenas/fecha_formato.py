"""
Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla,
el día, el mes y el año. Adaptar el programa anterior para que también funcione
cuando el día o el mes se introduzcan con un solo carácter.
"""
from datetime import date

def birth_date():
    day_birth = int(input("Introduce el día de nacimiento: "))
    month_birth = int(input("Introduce el mes de nacimiento: "))
    year_birth = int(input("Introduce el año de nacimiento: "))
    try:
        d = date(year=year_birth, month=month_birth, day=day_birth)
        # Formatear la fecha
        formatted_date = d.strftime("%d/%m/%Y")
        print(f"La fecha de nacimiento es: {formatted_date}")
    except ValueError as e:
        print(f"Error: {e}. Por favor, introduce una fecha válida.")

birth_date()
