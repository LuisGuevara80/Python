nombre_completo = input("Ingresa tu nombre completo: ") # Siempre retorna string

edad = int(input("Ingresa tu edad: ")) # Esta es una forma más corta de hacerlo

altura = input("Ingresa tu altura: ")
altura = float(altura)

autorizacion = input("¿Autorizas el programa? (si/no)") == "si"
#autorizacion = autorizacion == "si"

print(nombre_completo)
print(type(nombre_completo))

print (edad)
print(type(edad))

print(altura)
print(type(altura))

print(autorizacion)
print(type(autorizacion))