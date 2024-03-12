# Variables

my_string_variable = "My string variable"
my_int_variable = 5
my_bool_variable = False
my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

print(my_string_variable)
print(my_int_variable)
print(my_bool_variable)

#Concatenacion de variables en un print
print(my_string_variable,my_int_variable,my_bool_variable)
print(my_string_variable,str(my_int_variable),my_bool_variable)
print("Este es el valor de: ",my_bool_variable)

#Variables en una sola línea
name,surname,alias,age = "Miguel","Angel","Vextial",19
print("Me llamo:",name,surname,"Mi edad es:",age,". Y mi alias es:",alias)

print(len(my_string_variable)) # Contar longitud del string

# Inputs
first_name = input("Nombre: ")
age = input("Edad: ")
print("Nombre:",first_name)
print("Edad:",age)
#! Le puedes dar a las variables EL TIPO QUE QUIERAS
#!                               ===================                            
name = 123
print(type(name)) #--> Type int



