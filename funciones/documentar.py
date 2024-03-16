# Docstring
# Por convension de la comunidad python, se hace en la primer linea de la función y con """""". Y a esto se le llama Docstring
# el Docstring será almacenado en el atributo __Doc__ (Módulos, clases, métodos y funciones)

def suma(numero_1, numero_2):
    """
    La función suma 2 números enteros.

    Argumentos:
    numero_1(int)
    numero_2(int)

    se retorna la suma de los parámetros
    """
    return numero_1 + numero_2

print(suma.__doc__)
print(help(suma))

"""
Estas son 2 formas de mostrar el Docstring de una función.
"""