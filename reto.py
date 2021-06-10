#variables 

A = int(input())
B = 2*A+4
C = (B+A)//5




#Grupos

if C <= 20:
    grupo = 'uno'
elif C >= 20 and C <= 30:
    grupo = 'dos'
elif C >= 31 and C <= 50:
    grupo = 'tres'
else:
    grupo = 'cuatro'



#Imprimier por pantalla
print(f'{A} {B} {C}')

#Grupo de semilla:
print(grupo)