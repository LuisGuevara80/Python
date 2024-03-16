diccionario = {"a": 1, "b": 2, "c": 3, "d": 4}

del diccionario["a"] # del se utiliza para eliminar una llave en el diccionario, junto a su valor

valor = diccionario.pop("b") # .pop retorna el valor, pero elimina la llave.

diccionario.clear() # Elimina todas las llaves y valores de un diccionario.

print(valor)

print(diccionario)
print(len(diccionario))