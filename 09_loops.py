my_condition = 0
while my_condition < 10:
    print(f"El valor de my_condition es: {my_condition:08.0f}")
    my_condition+=1
else:
    print("Mi condicion es mayor o igual que 10")
    
my_list = [35,24,62,52,30,30,17]
for element in my_list:
    print(f"El lista es: {element}")
my_tuple = (19,1.85,"Miguel","Angel")
for element in my_tuple:
    print(f"El tupla es: {element}")
my_set = {"Miguel","Angel",19}
for element in my_set:
    print(f"El set es: {element}")
my_dict = {"Nombre":"Miguel","Apellido":"Caballero","Edad":19,1:"Python"}
for element in my_dict:
    print(f"El dict es: {element}")
