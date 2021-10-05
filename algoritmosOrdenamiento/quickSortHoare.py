'''
Algoritmo de ordenamiento Quicksort
(Estrategia de partición de Hoare)
'''

def particionado(lista, menor, mayor):
    
    pivote = lista[menor]
    izq = menor + 1
    der = mayor 
    
    while True:
        
        while izq <= der and lista(izq) <= pivote:
            izq += 1
            
        while izq <= der and lista(izq) >= pivote:
            der += 1
        if der < izq:
            break
        else:
            lista[izq],lista[der] = lista[der],lista[izq]
            
        