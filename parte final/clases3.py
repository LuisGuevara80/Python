class Usuario:
    username = "Username por default"               
    email = ""

# __dict__

# Esto es un objeto tipo Usuario, el cual también puede trabajar con los atributos de clase de Usuario.
user1 = Usuario()

# 1. Verifica si el atributo existe dentro del objeto.
# 2. Verifica si el atributo existe dentro de la clase.  -> Esto solo funciona para lectura.
# 3. Lanzar un error

print(user1.username)
print(Usuario.username)

print(id(user1.username))
print(id(Usuario.username))

print(user1.__dict__)  # Esto va a almacenar por medio de un diccionario todos aquellos atributos que tenga nuestro objeto.