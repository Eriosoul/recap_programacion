"""
Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro
correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.
"""
import re


def check_if_mail_valid():
    try:
        mail = input("Introduzca el correo electronico: ")
        new_mail = mail.rsplit('@', 1)[-2]
        domain = "@ceu.es"
        match = re.search(r'[\w.-]+@[\w.-]+.\w+', mail)
        if match:
            print(f'Su nuevo correo es: {new_mail}{domain}')
        else:
            print("not valid:::")
    except Exception as e:
        print(e)

check_if_mail_valid()