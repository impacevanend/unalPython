import random, copy



class Zombi:
    
    def __init__(self):
        self.calle = random.randint(10,20)
        self.direccion = random.choice(["izquiera","derecha"])
        
#*Cómo copiar un objeto que 
#*no dependa de la misma referencia de memoría:      

# z1 = Zombi() 
# z2 = copy.copy(z1)

# print(z1.calle)
# print(z2.calle)

# z1.calle = 100

# print("----------")

# print(z1.calle)
# print(z2.calle)


#*Qué hacer cuando queremos hacer 
#*copias de listas o copias de objeto
horda = []
for i in range(5):
    z = Zombi()
    horda.append(z)
    
copia = copy.deepcopy(horda)

horda[3].calle = 200 
horda[4].calle = 300 

for z in horda:
    print(z.calle)
    
print("-----------")
for z in copia:
    print(z.calle)
    