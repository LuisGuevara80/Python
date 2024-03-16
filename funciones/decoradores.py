"""
Un decorador es una función que toma como input una función y la cual retorna otra función.

Para trabajar con un decorador, tenemos que trabajar por lo menos con 3 funciones: el input, el output y la función principal.

a -> La función principal (Decorador)
b -> La función a decorar
c -> La función decorada

a(b) -> c
"""

def funcion_a(funcion_b):

    def funcion_c():
        print(">>>>Antes del llamado.")
        funcion_b()
        print(">>>>Despues del llamado.")
        # print("Nos encontramos en la función C")
    
    return funcion_c

@funcion_a                                          # Esto se utiliza para decorar la función, y que la función a tome la funcion saludar como argumento
def saludar():
    print("Hola, nos encontramos en una función")
saludar()                                        # Este retonrna el valor de la función C, si en dado caso queremos retornar el mensaje de la función saludar
                                                 # Debemos cambiar el print dentro de la funcion_c por la funcion_b

@funcion_a
def suma():
    print(10+30)
suma()  