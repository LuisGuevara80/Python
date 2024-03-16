def pares():     # con el Yield ya es un generador -> Que lo convierte ene un Lazy iterator
    for numero in range(0, 12, 2):  # Aquí estoy diciendo que está en un rango del 0 al 12 y con saltos de 2 en 2.
        yield numero             # Aquí no puedo utilizar un return, ya que acabaría con la corrida desde el número 0

        print("Se reanuda la ejecución")


generador = pares()

while True:                            # Este es un ciclo while infinito
    try:
        par = next(generador)
        print(par)
    except StopIteration:              # Cuando se quede sin valores por retornar en vez de tirar un error se imprimira el siguiente mensaje en pantalla
        print("El generador finalizo.")
        break                          # Se usa para finalizar el ciclo while

"""
generador = pares()

print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print("Esto es un código que está de por medio")
print(next(generador))
print(next(generador))
print(next(generador))                   # Aquí hay error y es porque se pasa de la cantidad que tiene la variable generador.

"""

"""
Usar los generadores es recomendable cuando se va a utilizar el programa para registar muchos registos
Estoy hablando de miles, cientos de miles y millones de datos.
"""