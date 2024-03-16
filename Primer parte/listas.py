#           0      1     2     3    a esta posición se le conoce como índice
lista = ["string", 10, 12.5, True] # list()  # De estas 2 formas se pueden crear listas
print(lista)

# Esto es solo para ver cómo se crean las listas
# Lo ideal sería trabajarlo así

lista_string = ["Luis", "Eduardo", "Guevara", "Juárez"]

lista_int = [-20, 10, 8, -5, -20]

lista_float = [1.2, 5.6, -45.6, 57.2]

lista_bool = [True, True, (2 < 100), (4>3 and 10 != 11)]

print(lista_string)
print(lista_int)
print(lista_float)
print(lista_bool)

print(lista_int.count(-20))   # Este count cuenta las veces que se encuentra el valor dentro de la lista.

name, name2, lastname, lastname2 = lista_string # Esto funciona solo si asignamos la misma cantidad de variables que elementos. Pero hay que tener cuidado con esto. Pueden surgir muchos errores.


print(lastname)