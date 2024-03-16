def suma(n1, n2):    # Todas sus letras deben de estar en minusculas, y si son 2 o más, separadas por un _

    return n1 + n2, "La función retorna 3 valores", "Hola"       # Se utiliza un return, para poder almacenar el resultado en una variable.
                                                                 # El return, puede retornar más de un valor, y se muestra como tupla. Sin embargo, es recomendable retornar un máximo de 3 valores.

numero_uno = int(input("Ingresa el primer número entero: "))
numero_dos = int(input("Ingresa el segundo número entero: "))

resultado, mensaje, _ = suma(numero_uno, numero_dos)   # Ahora como retorna 3 valores en forma de tupla, podemos agregar otra variable

# Con el guión bajo, omitimos el otro valor que returna la tupla

print("El resultado es:", resultado)
print(type(resultado))

print(mensaje)
print(type(mensaje))

"""
def se utiliza para declarar a la función. Y las funciones son creadas para que realicen una sola tarea. 
"""