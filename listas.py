"""
*Formas de asignar una lista

["Texto"]-> no se requiere en una lista con un sólo elemento una coma,
como en las tuplas.split()

x = []
lista = [1,2,3,4,5,6,7,'hola']

a = [1,2,3,4,5,6]
"""

#*Listas anidadas:
"""
lista1 =[0,1,2,3]
lista2 =["A","B","C"]
lista3 =[lista1,lista2]

print(lista3)
print(lista3[0])
print(lista3[1])
print(lista3[1][0])
"""
#*Concatenar listas:
"""
lista1 =[0,1,2,3]
lista2 =["A","B","C"]
lista3 =lista1 +lista2
print(lista3)
"""
#*Agregar al final de la lista:
"""
nombres = ["Antonio","María","Mabel"]
otros_nombres = ["Barry","John","Guttag"]

nombres.extend(otros_nombres)
print(nombres)
print(otros_nombres)
"""
#*Repetir listas:
"""
lista1= [1,3,4,5]
lista2= lista1 * 3
print(lista2)
"""

#*Comparación lexicográfica
"""

print(["Rojas", 123 ] <["Rosas", 123])
print(["Rosas", 123] == ["rosas", 123])
print(["Rosas", 123] > ["Rosas", 23])
print(["Rosas", "123"] > ["Rosas", "23"])
print(("Rosas", "123") > ("Rosas", 23))
"""

#*Subindice-> acceder elementos de una lista.
"""
avengers = ["Iroman","Thor", "Ant-man", "Hulk"]

print(avengers[0])
print(avengers[3])
print(avengers[-1])
print(avengers[-3])
"""
#*Consultar lista por medio de condicional.
"""
text = ["cien","años","de","soledad"]
if "años" in text:
    print("Si está en la lista")
else:
    print("No está en la lista")
"""    
#*Desempacar si un elemento no está en la lista.
"""
text = ["Cien", "años","de","soledad"]

if "sien" not in text:
    print("No está en la lista")
else:
    print("Está en la lista")
"""    
#*Iterar una lista.
"""
s= ["hola","amigos","mios"]

for palabra in s:
    print(palabra, end=" ")
"""    
#*Creando una lista con un ciclo for.
"""
d = 10
desplaza = [d + x for x in range(5)]
print(desplaza, end=" ")

potencia = [3 ** x for x in range(2, 6)]
print(potencia, end=" ")
"""
#*Asignando multiples variables desde una lista.
"""
lista = [1,-2,3]

a,b,c = lista
print(a,b,c, end=" ")
"""
#*Asignando múltiples variables desde una lista.
"""
lista = [11,9,-2,3,8,8]

var1, var2, var3 = [lista[i] for i in (1,3,5)]
print(var1, var2, var3, end = " ")
"""

#*Listas y funciones.
def minmax(a, b):
    if a < b:
        return [a,b]
    else:
        return [b,a]
    
x, y = minmax(5, 13)

print(f"min: {x}, max: {y}")

x, y = minmax(12, -4)

print(f"min: {x}, max: {y}")

#todo métodos:

#*longitud de lista.
"""
lista = [1,2,3,4]
nombre = ["Mich","Yoda"]
trabajo = ["Stars","War","Movie"]
empty = []
print(len(lista))
print(len(nombre))
print(len(trabajo))
print(len(empty))
"""
#*Cambiando elemento en listas(en duplas no es posible).
"""
lista =["E","1","m","e","j","o","r"]

lista[0] = "e"
print(lista)
lista[4] = "l"
print(lista)
lista[-1] = "s"
print(lista)
"""
#*Agregando elementos a la lista.
"""
nombres = ["Antonio", "Johan"]
nombres.append("Monica")
print(nombres)
nombres.append("Maria")
print(nombres)
nombres.append("Mabel")
print(nombres)
 """       
#*Insertando elementos-> agrega elemento en una posición especifica de una lista.append()
"""
nombres = ["Antonio", "Johan","Maria"]

nombres.insert(0, "Guttag")
print(nombres)

nombres.insert(2, "Petter")
print(nombres)

nombres.insert(len(nombres)//2, 10)
print(nombres)
"""
#*Eliminat elementos remove()-> lista.remove("elemento")
#*Sublisas avengers[:2] or avengers[::-1] 
#*Contar elemento de una lista lista.count("elemento") or lista.count(0) 
#*Busncado el indice de una lista  lista.index("elemento") or lista.index(0) 
#*Busncado el valor máximo o mínimo de una lista lista.max("elemento") or lista.min(0) 
#*Ordenar una lista lista.sor() or  lista.sor(reverse = True)-> ordena de manera inversa.
#*convertir a lista magicia = "Dumbledoer". list(magicia)


