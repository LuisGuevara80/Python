#                -5        -4        -3       -2      -1
#                 0         1         2        3       4
lista_curso = ["Python", "Django", "Flask", "Ruby", "Java"]

# El primero si se toma en cuenta 
# Se toma en cuenta uno anterior del ultimo
sub_lista = lista_curso[0:3]  #Esto solo toma en cuenta del 0 al 2
print(sub_lista)

sub_lista2 = lista_curso[:4]
print(sub_lista2)

sub_lista3 = lista_curso[1:]
print(sub_lista3)

#Si quiero hacer saltos de línea se hace con un tercer valor
sub_lista4 = lista_curso[0:5:3]
print(sub_lista4)

sub_lista5 = lista_curso[::2] # solo : abarca toda la lista y el otro : con el 2 los saltos de línea
print(sub_lista5)

sub_lista6 = lista_curso[::-1] # Tenemos la lista inversa
print(sub_lista6)
