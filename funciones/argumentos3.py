def promedio(*args):                     
    return sum(args) / len(args)          


def usuarios (**kwargs):              # Cuando se trabaja con el doble asterisco, ya no se trabaja con tuplas, sino que con diccionarios
    print(kwargs)                     # Por convención se utiliza siempre el nombre de Kwargs
    print(type(kwargs))


def combinacion(*args, **kwargs):     # un * es Tupla y 2 * es Diccionario.
    print(args)
    print(kwargs)


usuarios(Luis=[10, 10, 9.8, 10, 8], Eduardo=[10, 8, 7, 6, 9])

combinacion(1,2,3,4,5, cody=True, curso="python")