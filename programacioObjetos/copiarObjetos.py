#permite copiar objetos
import copy

a = 5
b = 5

print(id(a))
print(id(b))

d = [5,2,3]

e = [5,2,3]

g = d[:]

d[1] = 8
print(id(d))
print(id(e))
print(id(g))


# d = list(a) Crea un objeto lista diferente
print(d)
print(e)
print(g)

#Describe las funcionalidades de libreria copy
dir(copy)
a = [[1,2],[3,4]]

#Se crea una lista distinta externa, pero no interna.
b = list(a)

print(a)
print(b)

print(id(a))
print(id(b))

a[0][0]= 5



#*Copia profunda de todos los elementos de la lista.
c = copy.deepcopy(a)

print((a))
print((b))
print((c))

c[0][1] = 7 
print((a))
print((b))
print((c))