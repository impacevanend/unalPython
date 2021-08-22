lista = [5,7,3,1,8,4,9,2,6]


#Ordenamiento por selección






longitud = len(lista)


for i in range(longitud-1):
    
    
    menor = i
    
    print("El indicie actual para comparar es", menor)
    for j in range(i+1, longitud):
        print(j)
        if lista[j] < lista[menor]:
            menor = j
            print("Recorriendo lista. Es menor el indice",menor)
    temporal = lista[menor]
    lista[menor] = lista[i]
    print(lista)
    lista[i] = temporal
    print(lista)
    print("Cambiamos el elemento", lista[menor], "por el elemento",lista[i])
    
    '''
    temporal = 1-> posición 3
    lista[menor}->[5]
    
    '''
 
    
    