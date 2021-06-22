"""
Se delimita por medio de una coma  y paréntesis redondos
(,)
No se pueden modificar después de definidas

("Texto",) Una tupla con elemento que e una cadena. Para el caso de una tuplas de un sólo elemento
Python requiere una coma final para considerarla una tupla.

*Formas de crear tuplas:
x = ()

tup =(1,2,3,4,5,'hola','a')

a = 1,2,3


*tuplas anidadas

"""
"""
tuple1 = (0,1,2,3)
tuple2 = ("A","B","C")
tuple3 = (tuple1,tuple2)

print(tuple3)
print(tuple3[0])
print(tuple3[1])
print(tuple3[1][0])
"""

#*Concatenar tuplas
"""
tuple1 = ("A","B","C")
tuple2 = (0,1,2,3)
tuple3 = tuple1 + tuple2

print(tuple3)
"""
#*Repetir tuplas
"""
tuple2 = (0,1,2,3)
tuple3 = tuple2 * 3

print(tuple3)
"""
#*Comparación lexicográfica:

"""
Comparar las tuplas sólo con el mismo tipo de dato: ("texto",) >= ("texto",).
Genera error si se compara con tipos de datos distintos.
"""
"""
print(("Rojas", 123) < ("Rosas", 123))
print(("Rosas", 123) == ("rosas", 123))
print(("Rosas", 123) > ("Rosas", 23))
print(("Rojas", "123") > ("Rosas", 23))
print(("Rosas", "123") > ("Rosas", 23))
"""
"""


avengers = ( "Ironman","Thor","Ant-man","Hulk")

print(avengers[0])
print(avengers[3])
print(avengers[-1])
print(avengers[-3])
"""

#*Consultando una tupla condicional.

"""
text = ("cien","años","de","soledad")

if "perro" in text:
    print("Si está en la tupla")
else:
    print("No está en la tupla")
"""
#*Verificar si un elemento no está en la tupla
"""
text = ("cien","años","de","soledad")

if "compañia" not in text:
    print("No está en la tupla")
else:
    print("Si está en la tupla")
"""

#*Iteraciòn de una tupla
"""
s = ("Hola","amigos","mios")

for palabra in s:
    print(palabra, end = ", ")
    
"""

#*Asignaciòn de multiples variables.
"""
tupla = (1, -2, 3)

a,b,c = tupla

print(a, b, c, end = " ")
"""
#* Intercambio de variables
"""
a = 1
b = 3

a, b = b, a,

print(a, b, end = " ")
"""
#*Asignando multiples variables.
"""
tupla = (11, 9, -2,3,8,5)

var1, var2, var3 = (tupla[i] for i in (1,3,5))

print(var1, var2, var3, end = " ")
"""
#*Tuplas y fuciones:
"""
def minmax(a, b):
    if a < b:
        return a, b
    else: 
        return b, a

x, y = minmax(5, 13)

print(f'min: {x}, max: {y}')

x, y = minmax(12, -4)

print(f'min: {x}, max: {y}')

#todo Métodos de tuplas:
"""
#*lem()-> determina la longitud de una tupla.append()
"""
tup = (1,2,3,4)
nombre =("Mich","Yoda")
trabajo =("Stars","War","Movie")
empty =()

print(len(tup))
print(len(nombre))
print(len(trabajo))
print(len(empty))
"""
#*Subtuplas slice -> obtiene una porcion de una tupla.
"""
avenger = ("Iroman","Thor","Ant-man","Hulk")

print(avenger[:2])
print(avenger[1:3])
print(avenger[3:3])
print(avenger[::-1])
"""

#*Contar elementos de una tupla:
"""
tupla = (4,3,8,8,2,5,4,6,8,9)
print(tupla.count(2))
print(tupla.count(8))
print(tupla.count(5))
print(tupla.count(7))
"""
#*Encontrar el indice de un elementos en una tupla:
"""
tupla = (4,3,8,8,2,5,4,6,8,9)
print(tupla.index(2))
print(tupla.index(8))
print(tupla.index(5))
"""
#*Hallar un máximo y un mínimo en una tupla:
"""
t = (4, 5, -1,6, 7)

print(max(t))
print(min(t))
"""
#*Crear una cadena a través:
"""
magician = "Dumbledoer"
tm = tuple(magician)
print(tm)
"""
#*Desempacar variables (unpacking)
"""
tup1 =(1,2,3)

a,b,c = tup1

print(f"{a} {b} {c} ")
"""
#*Función map

t = tuple(map(int, input().split(" ")))

print(t)

print(t[0] + t[8])