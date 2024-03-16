diccionario = {"a": 1, "b": 2, "c": 3, "d": 4}

# Keys Muestran las llaves de un diccionario
# Values Muestran los valores de un diccionario
# Items Muestran las llaves con sus valores.


llaves = tuple(diccionario.keys())  # La tupla es para que se vea mejor. Y las facilidades que ofrece.
print(llaves)

valores = tuple(diccionario.values())
print(valores)

elementos = tuple(diccionario.items())
print(elementos)

#Los datos siempre se muestran en el orden del diccionario

#Esto sirve para crear un diccionario sin valores.

#my_other_dict = diccionario.fromkeys(("Nombre", "Apellido", "Edad"))  De esta forma también se puede, ya que diccionario es tipo dict. Pero es mejor usar la palabra dict como en el ejemplo de abajo
my_other_dict = dict.fromkeys(("Nombre", "Apellido", "Edad"))
print(my_other_dict)