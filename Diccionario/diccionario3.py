diccionario = {"a": 1, "b": 2, "c": 3, "d": 4}

print("a" in diccionario) #Esto sirve para saber si existe o no dentro del diccionario

valor = diccionario["d"]

print(valor)
print(type(valor))

# get se utilza para obtener el valor de una llave de manera segura

print("x" in diccionario)

valor1 = diccionario.get("x", "La llave no existe en el diccionario.") # Este mensaje solo se mostrará si en dado caso la llave no existe.
                                                                       # de lo contrario se mostrará el valor correspondiente de dicha llave. Es importante aclarar que se puede devolver cualquier valor
print(valor1)                                                          # ya sea booleano, decimal, entero, etc.
print(type(valor1))

"""
El get es muy útil, ya que, si en dado caso se coloca una llave que no existe, se obtendra
el valor de "none", sin causar ningún error en el programa.
"""

valor2 = diccionario.setdefault("e", 5)
print(valor2)
print(type(valor2))

"""
El setdefault, lo que hace es almacenar el valor, pero si en dado caso esa llave no se encuentra
en el diccinario, pues, la agrega.
"""
print(diccionario)