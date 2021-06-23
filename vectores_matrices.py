"""
Es un conjutno de número ordenados en filas y/o columnas

A = 1 3
    7 2 -> Dimensión de 3 * 2 -> aij ejemplo: a11-> 1
    3 4     i-> fila . j-> columna
            Se pueden escribir números positivos o negatiovos incluso raices
            
Matriz fila: vector fila -> A=(a11,a12,a13... a1n)1*n
            




"""
"""
a = [[21,18,35,40],
      [19, 11,21, 14],
      [12, 15,20, 30]]
 
b = [[11, 7, 21, 32],
      [9,15,24,10],
      [23, 8,12,22]]

def sumar(m1, m2):
    if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
        
        m3 = []
        for i in range(len(m1)):
            m3.append([])
            for j in range(len(m1[0])):
                m3[i].append(m1[i][j]  + m2[i][j]) 
                       
               
        return m3
    else:
        return None
    
c = sumar(a,b)

if c == None:
    print("No se pueden sumar")
else:
    for fila in c:
        print("[", end=" ")
        for elemento in fila:
            print(elemento, end=" ")
        print("]")
        
"""

"""
Matrices son conjuntos de datos, ordenados en finlas y columnas.

*Matriz de ejemplo:

Comsuma de una granja
                    trigo       cebada      pienso      Paja
            
            vacas   21          18            35        40
            
            Cerdos  19          11            21        14
            
            vacas   12          15            20        30
            
"""

#*Simulación de matrices con listas anidads:

consumo = [[21,18,35,40],
           [19, 11,21,14],
           [12,15,20,30]]

acumulador = 0
#*mostrando datos de la lista(recoriendo lista)
"""
for lista in consumo:
    print("[", end=" ")
    for elemento in lista:
        print(elemento, end=" ")
    print("]")
"""    
#*Creación de lista nula
"""
matriz_cero = [[0]*15]*10 #*Forma incorrecta, crea multiples veces la misma lista

for fila in matriz_cero:
    print(fila)
"""
#*Forma correcta
"""
lista_nula = []

for i in range(10):
    lista_nula.append([0]*15) 

lista_nula[2][2] = 2   

for fila in lista_nula:
    print(fila)   
"""  
#*Forma utilizando dos bucles:
"""

matriz_nula2 = []

for i in range(10):
    matriz_nula2.append([])
    for j in range(15):
        matriz_nula2[i].append(0)
        

for fila in matriz_nula2:
    print(fila)

"""
"""
matriz_nula2 = []

cantidad_filas = int(input("¿Catindad de filas de la matriz?: "))
cantidad_columnas = int(input("¿Catindad de filas de la matriz?: "))
dato = 0

for i in range(cantidad_filas):
    matriz_nula2.append([])
    for j in range(cantidad_columnas):
        while dato < cantidad_columnas:
            dato = int(input("Ingrese valor: "))
            matriz_nula2[i].append(dato)
        

for fila in matriz_nula2:
    print(fila)
    
"""
