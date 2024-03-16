lista = [8, 90, 1, 5, 44, 132, 600, 3, 4]

lista.sort() # Ordena de menor a mayor
print(lista)

print(lista[0]) # El primer valor
print(lista[-1]) # El ultimo valor

lista.sort(reverse=True) # Ordenar de mayor a menor
print(lista)

print(min(lista)) # El minimo valor sin importar el orden
print(max(lista)) # El máximo valor sin importar el orden

print(10 not in lista) # Este es para ver si el valor está en la lista o no
print(5 in lista)
