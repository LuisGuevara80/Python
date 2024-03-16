class Usuario:
    username = "Username por default"               
    email = ""

# __dict__

# Esto es un objeto tipo Usuario, el cual también puede trabajar con los atributos de clase de Usuario.
user1 = Usuario()

# 1. Verifica si el atributo existe dentro del objeto.
# 2. Verifica si el atributo existe dentro de la clase.  -> Esto solo funciona para lectura.
# 3. Lanzar un error

user1.username = 'cody' # Añadimos el atributo en el objeto
user1.password = "1234" # Añadimos el atributo en el objeto
user1.password = "password"  # así es cómo se modifica un atributo de un objeto.

print(user1.username)   # Atributo de instancia (El cual le pertenece al objeto). 

print(id(user1.username))
print(id(Usuario.username))

print(user1.__dict__)  # Esto va a almacenar por medio de un diccionario todos aquellos atributos que tenga nuestro objeto.

"""
El objeto, no puede moficar los atributos de clase. Pero si puede crear atributos para sí mismo.

El objeto, puede acceder a atributos de clase, pero no puede acceder a atributos de otro objeto.
"""