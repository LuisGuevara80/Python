class Animal():   # Clase Padre
        
    def comer(self):
        print("El animal come.")

    def dormir(self):
        print("El animal duerme.")

class Mascota(Animal):  # Clase hija
    pass

class Felino:   # Clase hija

    def cazar(self):
        print("El felino caza.")

class Gato(Mascota, Felino):   # Clase hija
    pass

patricio = Gato()

patricio.comer()
patricio.dormir()
patricio.cazar()