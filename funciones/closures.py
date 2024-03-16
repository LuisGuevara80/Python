e = "e" #Variable global

def funcion_principal():
    a = "a"                   # Estas también son variables locales, pero están en un rango superior a la variable c.
    b = "b"

    def funcion_anidada():
        c = "c"               # Variables locales (Por ser un variable local, no se puede usar fuera de la función)

        nonlocal b            # Para modificar una variable local que se encuentra en un scout superior, se puede hacer con el nonlocal
        b = "cambio de valor"

        print(a)
  
        print(b)
        print(id(b))

        print(e)
    
    funcion_anidada()
    #print(c)                   No se puede utilizar acá porque es local de la función_anidada
    print(b)
    print(id(b))

funcion_principal()