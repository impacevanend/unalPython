voto = ["T","T","T","A","A","A","C","C","C","C","H","Z","Z","Z","O","O","O","H","M","F","F","F","F","F"]# Linea de prueba, para validar funcionamiento del código

#* list(input().split()) -> linea para entrada para la plataforma.




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

"""
Todo Resultado esperado ++++ Salida del programa
T A C H Z O H M F            T A C H Z O H M F
3 3 4 1 3 3 1 1 5            3 3 4 1 3 3 1 1 5
"""