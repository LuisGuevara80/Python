elementos = {} #Las llaves denotan que es un diccionario


elementos["nombre"] = "Luis"  # Esto almacena en el diccionario "nombre" con el valor de "Luis"
elementos[(1,2,3)] = "La llave es una tupla" 

elementos["nombre"] = "Eduardo" # Esto es para cambiarle el valor a la llave. (Se utiliza la misma estructura.)

print(elementos)
print(len(elementos))  # Para conocer la longitud de un diccionario se utilza len

prueba = {"a": 1, "b": 2, "c": 3, "a": 4} #Esta declarada 2 veces la llave, pero se toma en cuenta el último valor.

print(prueba)
print(len(prueba))
