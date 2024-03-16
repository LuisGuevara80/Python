def area_circulo(radio, pi=3.14):        # No hay que utilizar espacios para definir el valor por default de un parametro.
    return pi * (radio ** 2)             # Los parametros con valores por default, se deben agregar siempre a la derecha.

resultado = area_circulo(pi=3.141592, radio=10)
print(resultado)

"""
A la hora de aplicar la función se le puede agregar el nombre de los parametros y el dato que vamos a utilizar, para 
que así, no se vea afectado lo que coloquemos por su orden. Ya que, tiene el nombre de los parametros.
"""