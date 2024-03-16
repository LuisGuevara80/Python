# Docstring
# Por convension de la comunidad python, se hace en la primer linea de la función y con """""". Y a esto se le llama Docstring
# el Docstring será almacenado en el atributo __Doc__ (Módulos, clases, métodos y funciones)

def suma(numero_1, numero_2):
    """
    La función suma 2 números enteros.

    Argumentos:
    numero_1 (int)
    numero_2 (int)

    se retorna la suma de los parámetros.

    >>> suma(10, 20)
    30                                  

    >>> suma(100, 300)                     
    400     
    """
    return numero_1 + numero_2


def resta(numero_1, numero_2):
    """
    >>> resta(100, 200)
    -100
    """
    return numero_1 - numero_2


# Para testear una función, se colocar triple >, el llamado de la función y el ejemplo de la ejecución.
# Es recomendable, hacer unas 2 o como mucho unas 3 pruebas.
# -m doctest "nombre de archivo" para hacer la prueba.