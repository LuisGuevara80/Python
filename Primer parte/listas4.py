#                -6        -5        -4       -3      -2     -1
#                 0         1         2        3       4      5
lista_curso = ["Python", "Django", "Flask", "Ruby", "Java", "Rust"]
lista_curso2 = ["C", "C++", "Docker"]

print(len(lista_curso)) #sirve para ver la cantidad de elementos en una lista

lista_curso.append("MongoDB") # Agrega nuevos elementos en la lista
lista_curso.append("C#") 
lista_curso.append("JavaScript")

lista_curso.insert(1, "Rails") # Inserta un elemento en un lugar en especifico
lista_curso.insert(0, "PyGame")

lista_curso.extend(lista_curso2) # Agregar una lista

lista_curso.remove("MongoDB") #Eliminar un element

print(lista_curso)
print(lista_curso.pop(1)) # returna el ultimo elemento o el que se le coloque en el parametro y lo quita de la lista.
print(lista_curso)

del lista_curso[0] # Elminitar un elemento por su índice
lista_curso[1] = "Django modificado" # Modifica un elemento de la lista, por medio de su indice
print(lista_curso)

lista_curso_backup = lista_curso.copy() # Copiar una lista
lista_curso.clear() # Eliminar toda la lista

print(lista_curso)
print(len(lista_curso))

print(lista_curso_backup)
print(len(lista_curso_backup))

lista_curso_backup.reverse() # Coloca los datos en reversa
print(lista_curso_backup)


#sort() Ordena de menor a mayor, eso está en el doc "listas5.py"