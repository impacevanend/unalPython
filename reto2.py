sindicato_superior = "TSDC"
sindicato_unitario = "REOU"

sindicatos = "TEDDOOOOSSDOQWETTOOOEEE"

contador_sup = 0
contador_unitario = 0
conversor = ""
contador = 0
lista = list(sindicatos)
"""

T E D D O O O O S S D O Q W E T T O O O E E E

S N S S S N U U U N S N N N U N S N U U U U U

S N S S S N U U U N S N N N U N S N U U U U U 
"""


for i in lista:
    if (i in sindicato_superior) and (i  in sindicato_unitario)== False:
        contador_sup += 1 
    elif (i in sindicato_unitario) and (i in sindicato_superior)== False:
        contador_unitario += 1 
       
    if contador_unitario > contador_sup:
        conversor += "U"
        
        
    elif contador_sup > contador_unitario:
        conversor += "S"
        
    else:
        conversor += "N"
                
print(conversor)