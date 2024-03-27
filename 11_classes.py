class Person:
    def __init__(self,name,surname): # constructor de clase
        self.name = name
        self.surname = surname
    
my_person = Person("Miguel","Angel")
print(f"La Persona se llama {my_person.name} y se apellida {my_person.surname}")



class Person2():
    def __init__(self,name,surname):
        self.fullname = f"{name} {surname}"
        
    def walk(self):
        print(f"{self.fullname} Esta caminando...")

my_person2 = Person2("Miguel","Angel")
print(my_person2.fullname)
my_person2.walk()




