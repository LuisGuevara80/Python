### Python Package Manager ###

# PIP https://pypi.org

# pip install pip
# pip --version

# pip install numpy
import pandas
from mypackage import arithmetics
import requests
import numpy

print(numpy.version.version)

numpy_array = numpy.array([35, 24, 62, 52, 30, 30, 17])
print(type(numpy_array))

print(numpy_array * 2)

# pip install requests

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
print(response)
print(response.status_code)
print(response.json())

# Arithmetics Package

print(arithmetics.sum_two_values(1, 4))

"""
En esta lección básicamente aprendí que existen distintos modulos que uno puede importar, los cuales son muy útiles para el manejo de paquetes.
Sin embargo, todo va a depender de la situación, para saber qué es lo mejor a utilizar
"""