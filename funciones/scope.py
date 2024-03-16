animal = "León"                 # Variable global -> Puede ser utilizada en función, Condición o Ciclo

def imprimir_animal():
    global animal                # Con esto se indica que no vamos a crear una variable, sino que vamos a utilizar la global

    animal = "Ballena"         
    tipo = "mamifero"           # Variable local ->  solo se puede utilizar aca, si la imprimo fuera de la función, dará error. 
                                                #  Solo puede ser utilizada dentro del bloque donde fue creada
  

    print(animal)
    print(id(animal))

imprimir_animal()

print(animal)
print(id(animal))

"""
Para Python la variable "animal" de la linea 1 con la linea 4 son totalmente distintos
Y esto se debe a que fueron creadas en scopes diferentes.
"""