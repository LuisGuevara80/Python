nombre = "Luis Eduardo"
apellido = "Guevara"

nombre_completo = f'Ing. {nombre} {apellido} {"Juárez"} {15*21}'
print(nombre_completo)
print(type(nombre_completo))

prueba = nombre_completo.split()
print(prueba)
print(type(prueba))

prueba_string = "/-/".join(prueba)
print(prueba_string)
print(type(prueba_string))


#El F en la línea 4 es lo que hace que se considere un f string, y se pueda trabajar de esta manera.
#Esta es una de las formas más efectivas y útiles para poder generar estos strings.