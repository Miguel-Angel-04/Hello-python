tupla = tuple()
tupla2 = ()

tupla = (19,1.85,"Miguel","Angel")
print(tupla)

print(tupla[-3])
print(tupla.count(19))
print(tupla.index("Miguel"))
#! Las tuplas son inmutables al inicializarse

tupla2 = (30,60,70)
my_sum_tuple = (tupla + tupla2)
print(my_sum_tuple)
tupla = list(tupla)
tupla[3] = "Cambio"
tupla.insert(1,"azul")
tupla = tuple(tupla)

print(tupla)
print(type(tupla))