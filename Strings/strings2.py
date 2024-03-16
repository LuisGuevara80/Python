titulo_curso = "Curso profesional de Python, donde aprenderemos Python"

contador = titulo_curso.count("a") #count nos permite contar las veces que se encuentra un string, dentro de otro.
print(contador)                         #Permitiendonos encontrar letras, palabras, frases, etc.
print(type(contador))

"""
Otra forma de hacerlo es la siguiente
"""
print("python" in titulo_curso.lower()) #in da un valor booleano

print("luis guevara" not in titulo_curso.lower())

print(titulo_curso.lower().startswith("curso")) #Sirve para ver si iniciar con ese término.

print(titulo_curso.lower().endswith("python")) #Sirve para ver si termina con ese término.

"""
El in permite saber si la palabra python se encuentra o no en el string, sin embargo, muchas veces
la diferencia es una mayuscula o una minuscula, por lo que, el termino .lower, nos permite buscar el
string en minuscula, lo cual es muy útil para ser acertados.
"""