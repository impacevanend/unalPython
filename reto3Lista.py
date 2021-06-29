voto = ["T","T","T","A","A","A","C","C","C","C","H","Z","Z","Z","O","O","O","H","M","F","F","F","F","F"]

#* list(input().split()) -> linea para entrada del programa de validación.
#

#

print(voto)

cantidad_votos = []
cantidato = []
voto_previo = []
contador = 1

for i in voto:
    
    
    if i != voto_previo:
    
        if voto_previo:
            cantidad_votos.append(str(contador))
            cantidato.append(voto_previo)
        contador = 1
        voto_previo = i
    
    else:
        contador +=1
else:
    cantidad_votos.append(str(contador))
    cantidato.append(voto_previo)
    
    
caracterI = " ".join(cantidato)#*Convierte las listas en cadeas y les asigna un espacio
caracterII = " ".join(cantidad_votos)#*Convierte las listas en cadeas y les asigna un espacio
print(caracterI)
print(caracterII)
