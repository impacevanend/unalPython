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
#*Rellenar matriz
"""
Programa que crea una matriz con los datos que introduces:
Filas, columnas y valores para cada elemento.
"""
"""

filas = int(input("Introduce número de filas: "))
columnas = int(input("Introduce número de columnas: "))

matriz = []

for i in range(filas):
    matriz.append([])
    for j in range(columnas):
        valor = float(input("Fila {}, columna {}: ".format(i+1, j+1)))
        matriz[i].append(valor)
        
print()
for fila in matriz:
    print("[",end=" ")
    for elemento in fila:
        print("{:8.2f}".format(elemento), end=" ")
    print("]")
print()
"""

"""
Definir una función que dadas dos matrices calcule su suma:
-Sólo se pueden sumar matrices el mismo orden.
-El resultado es otra matrizdel mismo orden que las sumadas.
"""
"""
a = [[21,18,35,40],
     [19,11,21,14],
     [12,15,20,30]]

b=[[11,7,21,32],
   [9,15,24,10],
   [23,8,12,22],]


def sumar_matriz(): 
"""

"""
replit-> https://replit.com/@leobusta/mintic13#main.py

"""

"""
Comsuma de una granja

                        GRANJA A
                    trigo       cebada      pienso      Paja
            
            vacas   21          18            35        40
            
            Cerdos  19          11            21        14
            
            vacas   12          15            20        30
            
                        GRANJA B
                    trigo       cebada      pienso      Paja
            
            vacas   11           7            21        32
            
            Cerdos   9          15            24        10
            
            vacas   23           8            12        22
            
"""

"""
a = [[21,18,35,40],
     [19,11,21,14],
     [12,15,20,30]]

b=[[11,7,21,32],
   [9,15,24,10],
   [23,8,12,22],]

def sumar_matrices(m1, m2):
    if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
        m3 = []
        for i in range(len(m1)):
            m3.append([])
            for j in range(len(m1[0])):
                m3[i].append(m1[i][j] + m2[i][j])
        
        return m3
    else:
        return None
    
c = sumar_matrices(a,b)

if c == None:
    print("No se pueden sumar") 
else:
    for fila in c:
        print("[", end=" ")
        for elemento in fila:
            print(elemento, end=" ")
        print("]")
        
"""
#*Multiplicación de matrices 
"""
Definir una función que dadas dos matrices calcule su multiplicación:

-Columnas de la primera matriz han de ser igual a filas de la segunda.
-Resultado será una matriz de orden filas de la 1° por columnas de la 2°

"""
""""
a = [[1,2,3], 
     [4,5,6]]

b = [[1,2],
     [3,4],
     [5,6]]
"""
"""
[1 2 3]      *     [1  2]    =       [22    28]         
[4 5 6]            [3  4]            [22    28]
       2*3         [3  4] 3*2                  2*2  


"""
"""
def multiplicar_matrices(m1, m2):
    if len(m1[0]) == len(m2):
        m3 = []
        for i in range(len(m1)):
            m3.append([])
            for j in range(len(m2[0])):
                m3[i].append(0)
                
        for i in range(len(m1)):
            for j in range(len(m2[0])):
                for k in range(len(m1[0])):
                    print((i,j),(i,k),(j,k),(k,j))
                    m3[i][j] += m1[i][k] * m2[k][j]
        return m3
    else:
        return None


c = multiplicar_matrices(a,b)  

if c == None:
    print("No se pueden multiplicar")
else:
    for fila in c:
        print("[", end=" ")
        for elemento in fila:
            print(elemento, end=" ")
        print("]")          

"""           
#*Matriz traspuesta
"""
Traspuesta de una matriz:
Trasponer (cambiar, trasladar) los elementos de las filas a las columnas, y los elementos de las
columnas a las filas.

m = [[1,2,3],
     [4,5,6]]
     
     
b = [[1,4], 
     [2,5],
     [3,6]]

"""
"""
matriz = [[1,2,3], 
          [4,5,6]]

def trasponer(m):
    t = []
    for i in range(len(m[0])):
        t.append([])
        for j in range(len(m)):
            t[i].append(m[j][i])
    return t

traspuesta = trasponer(matriz)

for linea in matriz:
    for elemento in linea:
        print(elemento, end=" ")
    print()

print("---------------------")

for linea in traspuesta:
    for elemento in linea:
        print(elemento, end=" ")
    print()        
"""

#*Rotar una matriz

"""
Rotar una matriz 90 grados en el sentido de lasmanecillas de un reloj
"""

una_matriz =[
    [11,12,13,14,15],
    [21,22,23,24,25],
    [31,32,33,34,35],
    [41,42,43,44,45]
]

flecha = [
    [0,0,0,0,1,0,0],
    [0,0,0,0,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,0,1,1,0],
    [0,0,0,0,1,0,0]
]


def rotar_matriz(matriz):
    rotada = []
    for i in range(len(matriz[0])):
        rotada.append([])
        for j in range(len(matriz)):
            rotada[i].append(matriz[len(matriz)-1-j][i])
    return rotada
    
print("-----------------------------")

for fila in flecha:
    for e in fila:
        print(e, end=" ")
    print()
    
rotada_1 = rotar_matriz(flecha)

for fila in rotada_1:
    for e in fila:
        print(e, end=" ")
    print()  
    
    
 
    