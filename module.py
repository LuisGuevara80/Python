import my_function

my_function.print_name_with_default("José", "Guevara", "Papu")

from my_function import print_name_with_default

print_name_with_default("José", "Guevara", "Papu")


"""
Esto sirve para poder utilizar otras funciones ya creadas, para no recrearlas y almacenar mucho más código.
Y hay 2 formas de importarlo. Ya sea la función que queremos o si no directamente todas
"""

# import modulos de python

import math

print(math.pi)
print(math.pow(2,3))

from math import pi as pi_value    # El as es un renombre, por si en dado caso lo queremos llamar de otra forma en nuestro programa

print(pi_value)