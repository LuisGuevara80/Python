nombre = "Luis Eduardo"
apellido = "Guevara"

#Esta es una forma de concatenar
nombre_completo = "ing."+ " " + nombre + " " + apellido + "."
print(nombre_completo)

print("-----------------------------------")

#Esta es otra manera de concatenar

nombre_completo2 = "Ing. %s %s %s." %(nombre, apellido, "Juárez")
print(nombre_completo2)

print("-----------------------------------")

#Esta es otra manera de concatenar

nombre_completo3 = "Ing. {} {} {}.".format(nombre, apellido, "Juárez")
print(nombre_completo3)

nombre_completo4 = "Ing. {nombre} {primer_apellido} {segundo_apellido}.".format( # Lo interesante de esta forma, es que puedo mover las llaves a la posición que yo quiera.
    nombre = nombre,
    primer_apellido = apellido,
    segundo_apellido = "Juárez"
)
print(nombre_completo4)
print(type(nombre_completo4))

print("EXTRA:  ")
print(" ")

lista_nombre = nombre_completo4.split()
print(lista_nombre)
print(type(lista_nombre))


lista_nombre_string = " ".join(lista_nombre)
print(lista_nombre_string)
print(type(lista_nombre_string))

