string1 = "My string"
string2 = 'mi otro string'
print(len(string1))
print(len(string2))
print(string1 + string2)
print(string1 + " " + string2)

my_new_line_string = "Este es un String\n\tcon salto de línea y tab"
print(my_new_line_string)


#!Formateo

name,surname,age = "Miguel","Angel",19
nombre = input("Nombre: ")
altura = float(input("Altura: "))
peso = float(input("Peso: "))
print("Mi nombre es {} {}, mi edad es: {}".format(name,surname,age))
print("Mi nombre es %s %s, mi edad es: %d" %(name,surname,age))
print("Se llama {}, su altura es de {:08.2f} y pesa {:.2f} kg".format(nombre,altura,peso))
print("Se llama %s, su altura es de %.2f y pesa %.2f kg" %(nombre,altura,peso))