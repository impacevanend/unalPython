#Algoritmo de ordenamiento rápido - quicksort

'''
-De los más rápidos y usados (hasta hace poco)

-Utiliza la estrategia de: Divide y vencerás
(Se implementa de forma recursiva)

-Complejidad de tiempo media: n log n
(En el peor caso puede llegar hasta n^2)

-Complejidad de espacio constante(in-place)
(la versión simple sería de n -  Usa listas auxiliares)

- No es estable

'''

lista = [8,12,3,11,5,9,10,4,15,7]

#lista = [2,3,1]

def particionado(lista):
    pivote = lista[0]
    menores = []
    mayores = []
    
    for i in range(1,len(lista)):
        if lista[i] < pivote:
            menores.append(lista[i])
        else:
            mayores.append(lista[i])
    return menores, pivote, mayores



def quicksort(lista):
    if len(lista) <2:
        return lista
    
    menores, pivote, mayores = particionado(lista)
    
    return quicksort(menores) + [pivote] + quicksort(mayores)

print(quicksort(lista))
