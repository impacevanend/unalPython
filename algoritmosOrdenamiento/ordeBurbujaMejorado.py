lista = [5,7,3,1,8,4,9,2,6]

comparaciones = 0
hay_cambios = True
i = 0
#*Se reduce a 35 las comparaciones
while hay_cambios and i < len(lista)-1:
    hay_cambios = False
    for j in range(len(lista)-i-1):
        comparaciones += 1
        if lista[j]>lista[j+1]:
            temporal = lista[j]
            lista[j] = lista[j+1]
            lista[j+1] = temporal
            
            hay_cambios = True
    i += 1
'''
* Estrategía de reducción de comparaciones
con for.
for i in range(len(lista)-1):
    for j in range(len(lista)-i-1):
        comparaciones += 1
        if lista[j]>lista[j+1]:
            temporal = lista[j]
            lista[j] = lista[j+1]
            lista[j+1] = temporal
'''        
            
print(lista)
print(comparaciones)