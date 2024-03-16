lista = [1, 2, 3, 4, 5, 6, 7]

tupla = (10, 20, 30, 40, 50, 60, 70)

lista_2 = [100, 200, 300, 400, 500, 600, 700] 

tupla_2 = (1000, 2000, 3000, 4000, 5000, 6000)

resultado = zip(lista, tupla, lista_2, tupla_2) # -> Devuelve un tipo Zip

resultado = tuple(resultado)  #Esto se puede pasar a lista con un list, en vez de tuple

print(resultado)

uno, dos, tres, cuatro, cinco, seis = resultado

print(uno)
print(dos)
print(tres)
print(cuatro)
print(cinco)
print(seis)




#Deben de tener la misma cantidad de elementos, si en dado caso se tienen más, estos se omiten.