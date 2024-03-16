promedio = lambda *args: sum(args) / len(args)

aprobatorio = lambda calificacion : calificacion >= 7

def es_aprobatorio(calificacion):
    return calificacion >= 90

def mostrar_mensaje(func_promedio, func_aprobatorio, *args):    # A estas funciones utilizadas acá, se les llama callbacks
    promedio = func_promedio(*args)

    if func_aprobatorio(promedio):
        print(f"Felicidades, aprobaste la materia con {promedio}.")
    else:
        print("No aprobaste la materia.")

mostrar_mensaje (promedio, aprobatorio, 10, 10, 8, 7, 7)


"""
print(promedio(10, 10, 9, 8, 7))
print(aprobatorio(6))

La ventaja de utilizar esto, es que nos permite cambiar las funciones y no afecta nada a la función principal.
Es por ello que esto es muy importante de utilizar cuando un programa es modular.
"""