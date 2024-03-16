def saludar():

    def mostrar_mensaje():
        print("Hola, nos encontramos en el curso de python")

    return mostrar_mensaje

respuesta = saludar()

print(respuesta)
print(type(respuesta))

respuesta()