### Type Hints ###

my_string_variable = "My String variable"
print(my_string_variable)
print(type(my_string_variable))

my_string_variable = 5
print(my_string_variable)
print(type(my_string_variable))

"""
Es bueno indicar si es str, int , float, etc. Por más que el tipado sea dinámico, ya que al momento que le queremos aplicar alguna función.
Se va a basar de eso, para indicar que funciones se pueden utilizar. supongamos que tengo un string, pero coloco que es int. A la hora de 
aplicar una función a esa variable VS me va a mostrar funciones para int.

Pero, dejando esto de lado, también es importante hacer esto, ya que FastApi, trabaja de manera más rápida y segura si se le declara el 
tipo que es.
"""

my_typed_variable: int = "My typed String variable" 
#my_typed_variable.

my_typed_variable: str = "My typed String variable" 
#my_typed_variable.

print(my_typed_variable)
print(type(my_typed_variable))

my_typed_variable = 5
print(my_typed_variable)
print(type(my_typed_variable))