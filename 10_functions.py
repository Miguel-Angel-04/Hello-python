def my_function():
    print("Esto es una funcion")
    
    
my_function()

def sum_two_values(first_number, second_number):
    return(first_number + second_number)

def print_name_with_defaults(name,surname,alias = "Sin alias"):
    print(f"{name},{surname},{alias}")

suma = sum_two_values(2,3)
print(suma)

name = input("Nombre: ")
surname = input("Surname: ")
#alias = input("Alias: ")
print_name_with_defaults(name,surname)

def print_texts(*text):
    for element in text:
        print(element)
print_texts("Hola","Msg 2","Msg 3")