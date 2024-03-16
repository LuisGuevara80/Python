
"""
contador = 1

while contador <= 10:
    print(contador)

    contador = contador + 1
"""

numero = 123456789
contador_digitos = 0

while numero >= 1:

    contador_digitos = contador_digitos + 1
    #contador_digito += 1                   Estas 2 lineas hacen lo mismo

    numero = numero/10
else:
    print(contador_digitos)



# El ciclo while se utiliza siempre y cuando nosotros no sepamos la cantidad de iteraciones que vamos a utilizar