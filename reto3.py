import re

voto = "TTTAAACCCCHZZZOOOHMFFFFF"


cantidad_votos = ""
cantidato = ""
voto_previo = ""
contador = 1





for i in voto:
    
    if i != voto_previo:
        
        if voto_previo:
            
            cantidad_votos += str(contador)
            cantidato += voto_previo
        contador = 1
        voto_previo = i

        
    else:
        contador += 1
        
else:
    cantidad_votos += str(contador)
    cantidato += voto_previo

"""
def separar(item):
    valor = r'(\w)([A-Z])'
    return re.sub(valor, r'\1 ', item)
"""



for i in cantidato:
    
    print(f"{i}",  end="*")

print()

for i in cantidad_votos:
    print(f"{i}",  end="*")

    



