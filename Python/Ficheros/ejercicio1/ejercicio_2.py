"""
Escribir una función que pida un número entero entre 1 y 10, lea el fichero tabla-n.txt con la tabla de
multiplicar de ese número, done n es el número introducido, y la muestre por pantalla.
Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.
"""

class FicheroMultiplic:
    def __init__(self):
        self.file = "tabla-"

    def get_numb(self):
        try:
            n = int(input("Número de la tabla de multiplicación: "))
            return n
        except ValueError:
            print("⚠️ Error: Debes ingresar un número entero válido.")
            return None  # Retornar None si hay error

    def check_file(self, n):
        if n is None:
            return  # No ejecutar si hubo error en get_numb()

        file_name = self.file + str(n) + ".txt"
        print(f"📄 Nombre del archivo generado: {file_name}")

        try:
            with open(file_name, 'r') as fil:
                contenido = fil.read()
                if contenido:
                    print("📖 Contenido del archivo:")
                    print(contenido)
                else:
                    print("⚠️ El archivo está vacío.")
        except FileNotFoundError:
            print("❌ Error: El archivo no existe.")
        except Exception as ex:
            print(f"⚠️ Error inesperado: {ex}")

if __name__ == '__main__':
    f = FicheroMultiplic()
    n = f.get_numb()  # Guardamos el número obtenido
    f.check_file(n)
