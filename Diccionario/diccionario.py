diccionario = {}
diccionario = dict()

# { llave: el valor el cual queremos asociar. }

diccionario = {"total": 55}

diccionario = {"total": 55, "descuento": True, "subtotal":15}

diccionario = {"total": 55, 10: "Curso de Python", (1,2,3): True}

# Un string ("total")
# Un número entero (10)
# Una tupla que almacena números enteros (1,2,3)

# Creacién del diccionario
#diccionario = dict()

# Agregar nueva llave valor
diccionario["usuario"] = "eduardo"

# Actualizar valor mediante una llave
diccionario["usuario"] = "eduardo_gpg"

# Obtener valor mediante una llave
print(diccionario["usuario"])

print(diccionario)

#Eliminar un dato del diccionario
del diccionario[(1,2,3)]
print(diccionario)

#Comprobar si hay un valor en el dict (Es por medio de la llave, no el valor.)
print("usuario" in diccionario)
print("eduardo gpg" in diccionario)

#Esto copia todas las llaves del diccionario, pero sin valores (Esto también lo puede hacer con una lista)
my_new_dict = dict.fromkeys(diccionario)
print(my_new_dict)

#Con esto ya no es vacio, pero todas las llaves tendrían ese valor
my_new_dict = dict.fromkeys(diccionario, "Hola")
print(my_new_dict)

#Crear una lista/tupla/set con un diccionario
lista_del_diccionario = list(diccionario.values())
print(lista_del_diccionario)