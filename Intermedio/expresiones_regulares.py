### Regular Expressions ###

import re

# match

my_string = "Esta es la lección número 7: Lección llamada Expresiones Regulares"
my_other_string = "Esta no es la lección número 6: Manejo de ficheros"

print(re.match("Esta es la lección", my_string, re.I))
print(re.match("es la lección", my_string)) #Es importante saber que el match busca desde el comienzo, por eso aquí aparece none.

match = re.match("Esta es la lección", my_string, re.I) # se guarda el march en una variable
print(match) 
start, end = match.span() # Se guarda el rango en las variables star y end
print(my_string[start:end]) #  Se imprime desde la variable el rango que nos dió span.

match = re.match("Esta no es la lección", my_other_string)
# if not(match == None): # Otra forma de comprobar el None
# if match != None: # Otra forma de comprobar el None
if match is not None:  #En este se trabajó lo mismo, solo que con una condicional.
    print(match)
    start, end = match.span()
    print(my_other_string[start:end])


# search

search = re.search("lección", my_string, re.I)  # Este encuentra la primera ocurrencia de la palabra
print(search)
start, end = search.span()
print(my_string[start:end])

# findall

findall = re.findall("lección", my_string, re.I) # Este encuentra todas las ocurrencias de la palabra
print(findall)

# split

print(re.split(":", my_string)) # Separa en elementos diferentes cada vez que encuentra ":" en el string

# sub

print(re.sub("[l|L]ección", "LECCIÓN", my_string))  # En este caso cambia Lección y lección (mayuscula y minuscula) por LECCIÓN
print(re.sub("Expresiones Regulares", "RegEx", my_string)) # Cambia el string encontrado por lo que le pongamos

### Regular Expressions Patterns ###

# Para aprender y validar expresiones regulares: https://regex101.com

pattern = r"[lL]ección" # la r indica que es una expresión regular
print(re.findall(pattern, my_string)) # Busca todas las palabras con l y L que termine con ección

pattern = r"[lL]ección|Expresiones" # Busca todas las palabras con l y L que termine con ección. Además de la palabra Expresiones.
print(re.findall(pattern, my_string))

pattern = r"[0-9]" # Busca todos los números del 0 al 9
print(re.findall(pattern, my_string))
print(re.search(pattern, my_string))

pattern = r"\d" # Busca todos los valores númericos
print(re.findall(pattern, my_string))

pattern = r"\D" # Busca todos los valores no númericos.
print(re.findall(pattern, my_string))

pattern = r"[l].*" # sin el asterisco busca a todas las letras l con un valor a la par como la, le, ll y así. # Como está ahorita, busca la primer l y todo lo que sigue de ella. string, int, float, etc.
print(re.findall(pattern, my_string))

email = "luis@luis.com"
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-.]+$"
print(re.match(pattern, email))
print(re.search(pattern, email))
print(re.findall(pattern, email))

email = "luis@luis.com.mx"
print(re.findall(pattern, email))