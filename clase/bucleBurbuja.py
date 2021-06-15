
#*lgoritmo de ordenamiento burbuja.append()
"""

lista = [5,7,3,1,8,4,9,2,6] #Longitud de la lista menos uno.

#todo este algortimo hace 8 * 8 = 64 iteraciones

for i in range(len(lista)-1): #Vueltas a la lista
    
    for j in range(len(lista)-1): #compara cada uno de los elementos de la lista.
        
        print(f'Comparando {lista[j]} con {lista[j + 1]}')
        
        if lista[j] > lista [j+1]:
            # lista[j], lista[j + 1] = lista[j+1], lista[j] forma asignación multiple
    
            temporal = lista[j]
            lista[j] = lista[j + 1]
            lista[j+1] = temporal
            
            print(f'Intercambiando: {lista[j]} por {lista[j + 1]}')
            
print(lista)#Comprobación del algoritmo

"""

#*Optimización del ordenamiento tipo burbuja


lista = [5,7,3,1,8,4,9,2,6] 

comparaciones = 0

hay_cambios = True #Centinela

"""
for i in range(len(lista)-1): 
    
    for j in range(len(lista)- i -1): #Se reduc el número de comparaciones, ahora aparecerán solo 36 iteraciones.
        
        comparaciones += 1
        
       
        
        if lista[j] > lista [j+1]:
           
    
            temporal = lista[j]
            lista[j] = lista[j + 1]
            lista[j+1] = temporal
            
            
            
print(lista)
print(comparaciones)
"""
i = 0 #* Aplicando estrategía anterior. 

while hay_cambios and i < len(lista) -1: 
    
    hay_cambios = False
    
    for j in range(len(lista)-i -1): #Se reduc el número de comparaciones, ahora aparecerán solo 36 iteraciones.
        
        comparaciones += 1
        
       
        
        if lista[j] > lista [j+1]:
           
    
            temporal = lista[j]
            lista[j] = lista[j + 1]
            lista[j+1] = temporal
            
            hay_cambios = True
            
    i += 1 #*Incrementando la i        
            
print(lista)
print(comparaciones)