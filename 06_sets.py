my_set = set()
my_other_set = {}
print(type(my_other_set))
my_other_set = {"Miguel","Angel",19}
print(len(my_other_set))

print(my_other_set.add("Hola")) #Añade al inicio pq no es una estructura ordenada
print(my_other_set)

my_other_set.add("Hola") # un set no admite repetidos
print(my_other_set)

print("Miguel" in my_other_set)
print("Migue" in my_other_set)

my_other_set.remove("Miguel")
print(my_other_set)

my_other_set.clear()
print(my_other_set)

#del my_other_set #nos hemos cargado la variable
#print(my_other_set)

my_set = {"Miguel","Angel",19}
my_list = list(my_set)
print(my_list)
print(my_list[0]) #no conoces el orden de la lista siempre

my_other_set = {"Kotlin","Swift","Python"}
my_new_set = my_set.union(my_other_set)
print(my_new_set)