numeros = (1, 2, 3, 4, 5)

uno, dos, tres, cuatro, cinco = numeros

print(uno)
print(dos)
print(tres)
print(cuatro)
print(cinco)
print("------------------------------------------------------")

# * -> lista
# *_ -> Denota que no se va a trabajar con esos valores.
numero2 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

uno, dos, tres, cuatro, *resto_numeros = numero2
print(uno)
print(dos)
print(tres)
print(cuatro)
print(resto_numeros)

print("------------------------------------------------------")

numero3 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

uno, dos, tres, cuatro, *_ = numero3
print(uno)
print(dos)
print(tres)
print(cuatro)

print("------------------------------------------------------")

numero4 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

uno, _ , tres, cuatro, *_ , nueve, diez = numero4  # Con este guión bajo indicamos que el 2 no lo vamos a utilizar.
print(uno)

print(tres)
print(cuatro)

print(nueve)
print(diez)






"""
Las tuplas son útiles en estos casos, ya que, podemos convertir su contenido
En variables de ésta manera tan sencilla.
"""
