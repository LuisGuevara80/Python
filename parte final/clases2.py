# Attrs de clase
# Attrs de instancia

class Usuario:
    username = "Username por default"               # Estos son atributos de la clase
    email = ""

Usuario.username = "User1"             # Aquí se está modificando el valor del atributo username
Usuario.email = "lg526443@gmail.com"

#Para usar estos atributos, es necesario colocar le nombre de la clase un "." y el atributo

print(Usuario.username)                # Aquí se está mostrando el valor del atributo username.
print(Usuario.email)



