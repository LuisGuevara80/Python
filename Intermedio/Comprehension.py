my_original_list = [0, 1, 2, 3, 4, 5, 6, 7]
print(my_original_list)

my_range = range(11)
print(list(my_range))

my_list = [i + 1 for i in range(11)] #sumandole uno a la lista, haciendo que llegue a 11
print(my_list)

my_list = [(i + 1) * 2 for i in range(11)] # Multiplicando por 2, para tener el doble de cada uno. Sin contar el cero, por esto tenemos el +1
print(my_list)

my_list = [(i + 1) * (i + 1) for i in range(11)] # Aquí se multiplica por si mismo, teniendo al cuadrado cada núnero. Sin contar el cero, por esto tenemos el +1
print(my_list)

def sum_five(number):
    return number + 5

my_list = [sum_five((i+1)) for i in range(11)] # Aquí se le está sumando 5 a cada valor, por medio de una función. Sin contar el cero, por esto tenemos el +1
print(my_list)