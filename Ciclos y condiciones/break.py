titulo_curso = "Curso profesional de Python"

for caracter in titulo_curso:

    if caracter == " ":                #El continue se utiliza para saltarse lo que colocamos. En este caso los espacios. Pero puede ser lo que deseamos. 
        continue

    if caracter == "P":
        break

    print (caracter)


# El break se utilza para terminar de forma inmediata cualquier tipo de ciclo, ya sea for, while, etc.