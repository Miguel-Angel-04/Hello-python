my_dict = dict()
my_other_dict = {"Nombre":"Miguel","Apellidos":"Caballero","Edad":19,1:"Python"}
print(my_other_dict.get("Apellidos"))


my_dict = {"Nombre":"Miguel","Apellidos":"Caballero","Edad":19,"Lenguajes":{"Python","Swift","Kotlin"},
            1:1.85}
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

print(my_dict[1])
print(my_dict["Nombre"])

my_dict["Nombre"] = [my_dict["Nombre"],"Fran"]
print(my_dict)
print(my_dict["Nombre"][1])

del my_dict[1]
print(my_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())
my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict)

print(list(my_new_dict.values()))
print(tuple(my_new_dict))
print(set(my_new_dict))


