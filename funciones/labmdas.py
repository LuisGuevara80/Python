def centigrados_a_farhenheit(grados):
    return grados * 1.8 + 32

mi_funcion = centigrados_a_farhenheit     #Es muy importante no colocar los parentesis aquí, ya que, si no Python pensará que estamos llamando a la función.

"""
Esto se utiliza para "guardar" la función en una variable y utilizar este término en vez, de la función directamente.
"""

print(type(mi_funcion))

print(mi_funcion(10))

"""
print(centigrados_a_farhenheit(10))
print(centigrados_a_farhenheit(-1))
print(centigrados_a_farhenheit(8))
"""
