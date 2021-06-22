sindicato_superior = input()
sindicato_unitario = input()

sindicatos = input()

contador_sup = 0
contador_unitario = 0
contador_n = 0
conversor = " "
lista = list(sindicatos)


for i in lista:
    if (i in sindicato_superior) == True and (i  in sindicato_unitario)== False:
        contador_sup += 1 
    elif (i in sindicato_unitario) and (i in sindicato_superior)== False:
        contador_unitario += 1 
    else:
        contador_n +=1
    
    
        
    if contador_unitario > contador_sup and contador_n >= 0:
        conversor += "U"
        contador_n = 0
        
    if  contador_sup > contador_unitario and contador_n >= 0:
        conversor += "S"
        contador_n = 0
    else:
        conversor += "N"
        contador_n = 0
        
print(conversor)
    

"""
Ejemplo: si los sindicatos son: temporales(T), contratistas (C), obreros (O) dedicados(D), empleados (E) y regionales (R).
debo comparar superior con unitario, y colocar si la votación pertenece a cada uno de ellos:

ejemplo:
TSDC   (superior)
REOU  (unitario)

La primera vez que ingrese voto para ese sindicato
el segundo voto queda en espera de un proximo valor a favor, para sumarlo
si no perntenece a ninguno, entonces el votor es neutral 

T E D D O O O O S S D O Q W E T T O O O E E E

S N S S S N U U U N S N N N U N S N U U U U U

comparar cada sindicato con la secunecia y asignarlo un voto

"""

"""
pollos = ["Angie","Andrés","Gabriela","Oscar","Kevin","victor","Gustavo","Annie","Maria"]

contL = [0] * len(pollos)

voto= input("Ingrese el nombre del estudiante a votar o ingrese 'Fin': ")

while voto != "Fin":
    votosMayus = voto.capitalize()
    if votosMayus.title() in pollos:
        pos = pollos.index(votosMayus)
        contL[pos] +=1
    else:
        print("Voto no valido")
    voto= input("Ingrese el nombre del estudiante a votar o ingrese 'FIN': ")

cantEst = sum(contL)
cantMax = max(contL)
posCont = contL.index(cantMax)
gana = pollos[posCont]

print(f"El total de estudianes que votaron fue: {cantEst}")
print(f"Gana: {gana} con {cantMax}")

"""