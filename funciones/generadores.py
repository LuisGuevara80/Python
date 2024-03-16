def pares():     # con el Yield ya es un generador -> Que lo convierte ene un Lazy iterator
    for numero in range(0, 100, 2):  # Aquí estoy diciendo que está en un rango del 0 al 100 y con saltos de 2 en 2.
        yield numero             # Aquí no puedo utilizar un return, ya que acabaría con la corrida desde el número 0, en cambio el yield se queda suspendida y se retoma cuando se le solicita.

        print("Se reanuda la ejecución")

for par in pares():
    print (par)

"""
La principal ventaja es la forma en cómo nosotros vamos a iterar cada uno de los objetos que
el generador genera y retorna.
"""