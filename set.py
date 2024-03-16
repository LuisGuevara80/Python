my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set))

my_other_set = {"Luis", "Guevara", 18}
print(type(my_other_set))
print(len(my_other_set))

my_other_set.add("Luigi")  # Un set no es una estructura ordenada
my_other_set.add("Luigi")  # Un set no admite repetidos
print(my_other_set)

print("Luis" in my_other_set)
print("Luisi" in my_other_set)

my_other_set.remove("Luis")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

del my_other_set

# Clear limpia los elementos, en este caso del set.
# del elimina la variable que almacena a esos elementos.

my_set = {"Eduardo", "Juárez", 17}
my_other_set = {"Luis", "Guevara", 18}

my_new_set = my_set.union(my_other_set) # Une elementos
print(my_new_set)

print(my_new_set.union(my_new_set).union(my_other_set).union({"Jeje", "No es repetido"})) #Une

print(my_new_set.difference(my_other_set)) #Elimina los que tengan iguales 