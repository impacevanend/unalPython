#for anidado

# for i in range(1,4):
#     for j in range(1,4):
#             print(i,j)


#Crea un baraja con bucles añadiendo las
#cartas a una lista mediante bucles for

#baraja 

tantos = ["A","2","3","4","5","6","7","S","C","R"]
palos = ["oro","copas","espadas","bastos"]


baraja =[]


for i in tantos:
    for j in palos:
        
        carta = "{} de {}".format(i,j)
        baraja.append(carta)
        
    
    
for i in range(0,40, 4):
    for j in range(4):
        print("{}".format(baraja[i+j]) , end="")
    print()