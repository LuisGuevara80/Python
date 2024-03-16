mensaje = "Hola mundo!"

# ljust -> Justificar a la izquierda
# rjust -> Justificar a la derecha
# center -> centrar

mensaje1 = mensaje.ljust(20)
print(mensaje1, ".")

mensaje2 = mensaje.center(20)       #Estas variables no modifican a la principal, solo apartir de él se generan unos nuevos.
print(mensaje2, ".")

mensaje3 = mensaje.rjust(20)
print(mensaje3, ".")

