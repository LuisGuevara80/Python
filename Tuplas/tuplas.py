#            0         1       2       3        4
tupla = ("String", 10, 12.20, True, [1,2,3], (4,5,6))

print(tupla)

print(type(tupla))

# Las tuplas son más rápidas que las tablas, ya que, se almacenan en otro espacio.

tupla[0] = "String modificado"

#Esta es una de las diferencias con las listas, y es que en las tuplas son valores constantes e inmutables.