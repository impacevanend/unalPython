##Ordenamiento por selección, burbuja, burbuja mejorado


import random

lista1 = [random.randint(1, 100) for i in range(100)]

lista2 = list(lista1)
lista3 = list(lista1)
lista4 = list(lista1)
lista5 = list(lista1)

print("----------------------------------")
comparaciones = 0
cambios = 0
#Burbuja básico
for i in range(len(lista1)-1):
    for j in range(len(lista1)-1):
        comparaciones += 1
        if lista1[j] > lista2[j+1]:
            temporal = lista1[j]
            lista1[j] = lista1[j+1]
            lista1[j+1] = temporal
            cambios +=1
            
print(lista1)
print("Burbuja básico. Comparaciones:",comparaciones,"Cambios:",cambios)

print("----------------------------------")

comparaciones = 0
cambios = 0

for i in range(len(lista2)):
    for j in range(len(lista2)-i-1):
        comparaciones +=1
        if lista2[j] > lista2[j+1]:
            temporal = lista2[j]
            lista2[j] = lista2[j+1]
            lista2[j+1] = temporal
            cambios += 1
        
print(lista2)
print("Con reducción. Comparaciones:",comparaciones,"Cambios:",cambios)

print("----------------------------------")

comparaciones = 0
cambios = 0

desordenada = True

while desordenada:
    desordenada = False
    for j in range(len(lista3)-1):
        comparaciones += 1
        if lista3[j] > lista3[j+1]:
            temporal = lista3[j]
            lista3[j] = lista3[j+1]
            lista3[j+1] = temporal
            cambios += 1
            desordenada = True
            
print(lista3)
print("Con centinela. Comparaciones:",comparaciones,"Cambios:",cambios)

print("----------------------------------")

comparaciones = 0
cambios = 0

desordenada = True

i=0

while desordenada and i<len(lista4)-1:
    desordenada = False
    for j in range(len(lista4)-i-1):
        comparaciones += 1
        if lista4[j] > lista4[j+1]:
            temporal = lista3[j]
            lista4[j] = lista4[j+1]
            lista4[j+1] = temporal
            cambios += 1
            desordenada = True
    i +=1
print(lista4)
print("Con centinela y reducción. Comparaciones:",comparaciones,"Cambios:",cambios)

print("----------------------------------")

comparaciones = 0
cambios_lista = 0
cambios_variable = 0

for i in range(len(lista5)-1):
    menor = i
    for j in range(i+1, len(lista5)):
        comparaciones +=1
        if lista5[j] < lista5[menor]:
            menor = j
            cambios_variable +=1
    
    temporal = lista5[menor]
    lista5[menor] = lista5[i]
    lista5[i] = temporal
    cambios_lista += 1
    
print(lista5)
print("Por selección. Comparaciones:",comparaciones)
print("Camibos lista:",cambios_lista," Cambios de variable:",cambios_variable)