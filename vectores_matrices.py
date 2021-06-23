"""
Es un conjutno de número ordenados en filas y/o columnas

A = 1 3
    7 2 -> Dimensión de 3 * 2 -> aij ejemplo: a11-> 1
    3 4     i-> fila . j-> columna
            Se pueden escribir números positivos o negatiovos incluso raices
            
Matriz fila: vector fila -> A=(a11,a12,a13... a1n)1*n
            




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