class Mascota:  # Clase Padre
    
    def comer(self):
        print("La mascota come.")

    def dormir(self):
        print("La mascota duerme.")

class Perro(Mascota):   # Clase hija
    pass

class Gato(Mascota):
    pass



duke = Perro()

duke.comer()
duke.dormir()

patricio = Gato()

patricio.comer()
patricio.dormir()


# Este es un ejemplo, donde si se piden parametros y por ende se usa el __init__

class Perro(Mascota):

    def __init__(self, nombre):
        self.nombre = nombre

    def comer(self):
        print(f"El perro {self.nombre} come.")

    def dormir(self):
        print(f"El perro {self.nombre} duerme.")


perro = Perro("Fido")

perro.comer()
perro.dormir()


# MIN 8:47:52 EXPLICA PARA PODER HACERLAS "PRIVADAS" Y QUE NO SE PUEDAN MODIFICAR
# CURSO DE PYTHON 10 HORAS
