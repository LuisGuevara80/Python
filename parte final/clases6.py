"""
Esto lo que hace es que cuando se cree un objeto de tipo Usuario(), obligatoriamente  este objeto tenga 2 atributos,
y que opcionalmente se le puedan agregar valores a dichos atributos.
"""

class Usuario:

    def __init__(self):      #El método init se va a ejecutar siempre que creemos un objeto de la clase.
        self.username = ""
        self.password = ""


user1 = Usuario()
user2 = Usuario()
user3 = Usuario()


print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)

# Esta es con parametros:

class Usuario1:

    def __init__(self, username="", password=""):      #El método init se va a ejecutar siempre que creemos un objeto de la clase.
        self.username = username                       # def __init__(self) Esto es necesario siempre para crear un constructor de clase, es decir cuando se piden parametros, de lo contrario no es necesario.
        self.password = password


user1 = Usuario1("user1", "Password1")
user2 = Usuario1("user2", "Password2")
user3 = Usuario1("user3", "Password3")
user4 = Usuario1()


print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)
print(user4.__dict__)

"""
En esto también se puede usar lo de las funciones, por lo tanto le podemos colocar valores por predeterminado
En este caso fue un elemento vacio.
"""