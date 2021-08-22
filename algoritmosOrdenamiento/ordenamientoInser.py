#ordenamiento por burbuja

#poco efciente -> hace en este caso
#64 iteraciones 8*8
#Se cambia multiples veces.
#Se llevan a cabo muchos cambios, muchas comparaciones.

lista =[5,7,3,1,8,4,9,2,6]

for i in range(len(lista)-1):
    
    for j in range(len(lista)-1):
        
        print("Comparando:", lista[j],"con",lista[j+1])
        if lista[j] > lista[j+1]:
        
            #lista[j], lista[j+1] = lista[j+1],lista[j]  
            temporal = lista[j]
            lista[j] = lista[j+1]
            
            lista[j+1] = temporal
            
            print("Intercambiando: ",lista[j], "por", lista[j+1])
            
