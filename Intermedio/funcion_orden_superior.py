from functools import reduce

### Higher Order Functions ###

def sum_one(value):
    return value + 1


def sum_five(value):
    return value + 5


def sum_two_values_and_add_value(first_value, second_value, f_sum):
    return f_sum(first_value + second_value)


print(sum_two_values_and_add_value(5, 2, sum_one))  #se le está pasando una función como parametro.
print(sum_two_values_and_add_value(5, 2, sum_five))

### Closures ###

def sum_ten(original_value):  #Esto de funciones anidadas, lo veo muy bien para hacer procesos largos con condicionales o algo por el estilo.
    def add(value):
        return value + 10 + original_value
    return add


add_closure = sum_ten(1)
print(add_closure(5))
print((sum_ten(5))(1))


### Built-in Higher Order Functions ###

numbers = [2, 5, 10, 21, 3, 30]

# Map


def multiply_two(number):
    return number * 2


print(list(map(multiply_two, numbers)))    # Este lo que hace es aplicar la función a cada uno de los objetos de la lista.
print(list(map(lambda number: number * 2, numbers)))  # Este lo que hace es aplicar el lambda a cada uno de los objetos de la lista.

# Filter


def filter_greater_than_ten(number):  
    if number > 10:
        return True
    return False


print(list(filter(filter_greater_than_ten, numbers)))    # Este lo que hace es filtrar según una función y valor booleano la lista. En este caso los numeros mayores a 10
print(list(filter(lambda number: number > 10, numbers)))  # Este lo que hace es filtrar según una lambda y valor booleano la lista. En este caso los numeros mayores a 10

# Reduce


def sum_two_values(first_value, second_value):
    return first_value + second_value


print(reduce(sum_two_values, numbers))  # Este lo que hace es sumar los 2 primeros valores y así sucesivamente en toda la lista, es por eso que da 71
                                        # Si en dado caso se quiere ver más claro puedes colocar un print del first_value y second_value antes del return
print(reduce(lambda first_value, second_value: first_value + second_value, numbers))                                  