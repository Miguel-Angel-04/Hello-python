string1 = "My string"
string2 = 'Mi string'
print(len(string1))
print(len(string2))
print(string1 + " " + string2)

my_new_line_string = "Este es un String\ncon salto de línea"
print(my_new_line_string)

my_tab_string = "\tString con tabulacion"
print(my_tab_string)

my_scape_string = "\\tEste es un string \\n escapado"
print(my_scape_string)


#! FORMATEO

name,surname,age= "Miguel","Angel",19

print("Mi nombre es {}, {} y tengo {:0.8f} años.".format(name,surname,age))
# Para el .format solo se ponen {} consecutivamente
print("Mi nombre es %s, %s y tengo %d años." %(name,surname,age))

#! Inferencia de datos
print(f"Mi nombre es {name}, {surname} y tengo {age} años.") # Mejor forma para los printf

#Desempaquetado de caracteres
language = "python"
a,b,c,d,e,f = language

print(a)
print(b)


#!  Division
language_slice = language[1:3]
print(language_slice)
language_slice = language[-2]
print(language_slice)

#!  Reverse

reversed_language = language[::-1]
print(reversed_language)

#!  Funciones

print(language.capitalize())
print(language.upper())
print(language.count("y"))
print("1".isnumeric())
print(language.isnumeric())
print(language.upper().isupper())
print(language.lower().isupper())
print(language.startswith("p"))


