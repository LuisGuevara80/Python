
lenguajes = "python Ruby Java Rust C++ C"

listado_lenguajes = lenguajes.split() #El split genera un elemento de la lista, por cada espacio. Si no hay, genera un solo elemento
print(listado_lenguajes)

print("-------------------------------------------------")

lenguajes = "python-Ruby-Java-Rust-C++-C"

listado_lenguajes = lenguajes.split("-") #Al split se le puede indicar a partir de qué, generar un nuevo elemento en la lista. 
print(listado_lenguajes)                 #En este caso fue un guión


print("-------------------------------------------------")

lenguajes = "python/()Ruby/()Java/()Rust/()C++/()C"

listado_lenguajes = lenguajes.split("/()", 2) #Pero también se puede con cualquier otra cosa
print(listado_lenguajes)                      # Este ,2 hace que se tome en cuenta solo 2 veces el patron y lo demás, lo coloca como un solo elemento

print("-------------------------------------------------")

lenguajes =["Python", "Ruby", "Java", "Rust"]

string_lenguajes = "-".join(lenguajes) # Este lo que genera es la union de los elementos de una lista en un solo string, y se pueden unir con un espacio, guión, etc.
print(string_lenguajes)


#split separa el string en elementos de lista
#join une los elementos de una lista en un string