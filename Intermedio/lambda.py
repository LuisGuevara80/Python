sum_two_values = lambda first_value, second_value: first_value + second_value
print(sum_two_values(5, 4))

multiply_values = lambda first_value, second_value: first_value * second_value - 3
print(multiply_values(5, 4))

def sum_three_values(value):
    return lambda first_value, second_value: first_value + second_value + value

print(sum_three_values(10)(5, 4))


"""
En general, es mejor trabajar con un lambda cuando se necesita una función que se utilizará solo una vez o de forma breve. 
Los lambdas son más concisos y fáciles de leer que las funciones tradicionales, lo que los hace ideales para tareas simples 
o para pasar como argumentos a otras funciones.

Por supuesto, hay también algunos casos en los que es mejor usar una función tradicional. Por ejemplo, si una función necesita 
ser reutilizada en varios lugares, es mejor definirla como una función tradicional. Además, si una función necesita acceder a 
variables globales o realizar operaciones complejas, es mejor definirla como una función tradicional.
"""