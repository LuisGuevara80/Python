
number_one = 1
number_two = 7

# Try except
try:
    print(number_one + number_two)
    print("Todo funciona a la perfección")
except:
    # Se ejecuta si se produce una excepción
    print("El programa tiene errores")

# Try except Else

try:
    print(number_one + number_two)
    print("Todo funciona a la perfección")
except:
    print("El programa tiene errores")
else:
    # Se ejecuta si no se produce una excepción 
    print("La ejecución continua correctamente")

# Try except Else Finally

try:
    print(number_one + number_two)
    print("Todo funciona a la perfección")
except:
    print("El programa tiene errores")
else:
    print("La ejecución continua correctamente")
finally:
    # Se ejecuta siempre
    print("La ejecución continua")


# Excepciones por tipo

try:
    print(number_one + number_two)
    print("No se ha producido un error")
except ValueError:
    print("Se ha producido un ValueError")
except TypeError:
    print("Se ha producido un TypeError")


# Captura de la información de la excepción

try:
    print(number_one + number_two)
    print("No se ha producido un error")
except ValueError as error:
    print(error)
except Exception as my_random_error_name:
    print(my_random_error_name)