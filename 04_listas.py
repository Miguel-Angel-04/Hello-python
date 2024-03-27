my_list = list([1,2,3,1])
my_list2 = list({1,2,3,1})
my_other_list = []
print(len(my_list))
# {1,2,3,1} es un conjunto
# [1,2,3,1] es una lista

print(my_list)
print(my_list2)

my_other_list = [19, 1.85,"Miguel", "Angel"]
print(type(my_other_list))
print(my_other_list[-1])
print(my_other_list[my_other_list.count(19)])
edad,altura,nombre,apellidos = my_other_list
print(edad)
print(my_list2 + my_list2)

my_other_list.append("Ultimo")
my_other_list.insert(0,"Ahoraprimero")
my_other_list.remove(19)
print(my_other_list)

print(my_list.pop()) #quita el último
print(my_list)

print(my_list.pop(1)) #indice del elemento que quiero eliminar
print(my_list)

my_new_list = my_other_list.copy()
print(my_new_list)

