def promedio(*args):                      # Este asterisco tiene que ir sin espacios, y sirve para poder aplicar la función a todos los elementos que se coloquen
    print(args)                           # Este asterisco tambien lo que hace es que listado ahora sea una tupla. Y siempre se debe declarar como args     
    print(type(args))

    return sum(args) / len(args)          


resultado = promedio(10, 10, 5, 7, 10)

print(resultado)

"""
sum es la suma total de los elementos, en este caso de "args"
len es la cantidad de elementos dentro del listado.
"""