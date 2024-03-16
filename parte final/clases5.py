class Usuario:
    
    def inicializar(self):          # Por convención de la comunidad python, el nombre de este parametro es self
        # Añadiendo atributos al objeto
        self.username = ""
        self.password = ""

user1 = Usuario()
user2 = Usuario()

user1.inicializar()
user2.inicializar()

print(user1.__dict__)
print(user2.__dict__)

# Existen estas dos maneras de hacerlo, en la primera toma el valor que ay tiene la clase.
# En la segunda uno le puede asignar el valor

class Usuario1:
    
    def inicializar(self, username, password):          # Por convención de la comunidad python, el nombre de este parametro es self
        # Añadiendo atributos al objeto
        self.username = username
        self.password = password

user1 = Usuario1()
user2 = Usuario1()
user3 = Usuario1()


user1.inicializar("username1", "password1")
user2.inicializar("username2", "password2")
user3.inicializar("Luigi", "password3")

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)

"""
Este método es útil y funciona, pero es mejor ver el de la clase 6 y aplicar ese.
"""