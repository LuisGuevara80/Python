class SerVivo:      # Clase Padre

    def dormir(self):
        print("El ser duerme.")

class Animal(SerVivo):   # Clase hija
        
    def comer(self):
        print("El animal come.")

class Mascota(Animal):  # Clase hija
    
    def comer(self):
        super().comer()
        print("La mascota come.")
    

class Felino:   # Clase hija

    def cazar(self):
        print("El felino caza.")

class Gato(Mascota, Felino):   # Clase hija
    
    def __init__(self, nombre):
        self.nombre = nombre

    def comer(self):
        super().comer()
        print(f"{self.nombre} come.")

    def dormir(self):
        super().dormir()                     #Nos permite acceder al atributo de la clase Padre.
        print(f"{self.nombre} duerme.")
    

patricio = Gato("Patricio")

patricio.comer()
patricio.dormir()