def saludar(username):
    mensaje = f"Hola {username}" #variable locar

    def mostrar_mensaje():   # anidada
        print(mensaje)

    return mostrar_mensaje

username = "cody"

respuesta = saludar(username)    # Se sigue imprimiento "cody" porque este era el valor que tenía username cuando a la variable respuesta se le asignó la función saludar.

username = "Luis"

respuesta()


"""
Un closure es una función que puede generar de manera dinamica otra función.
Y esta otra función puede acceder a las variables locales aún cuando las primeras hayan finalizado.
"""