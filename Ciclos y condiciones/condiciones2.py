variable = "" or "CodigoFacilito"   # Se asigna a la primer opción que tenga un valor verdadero.
print(variable)                     # Y se lee de izquierda a derecha.

variable2 = "" or 0 or [] or True
print(variable2)

listado = [0]
nombre = "Cody"

"""
if listado:
    prueba = listado
else:
    prueba = nombre

print(prueba)
"""
#Esto se puede hacer en una sola linea

prueba = listado or nombre
print(prueba)
