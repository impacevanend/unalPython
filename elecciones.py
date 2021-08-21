def candidatos(lista):
     archivo = []
     for n in lista:
         if n not in archivo:
             archivo.append(n)
     return archivo
 
 
 
def auditoria1(lista1,lista2,string):
     archivo = []
    
     for n in lista1:
         if lista2[n] == "":
             archivo.append(n)
     return archivo 
 
 
def auditoria2(lista1, lista2):
     archivo = []
     for n in lista1:
         if n not in lista2:
             archivo.append(n)
     return archivo
 
 
def diferencia(lista1, lista2):
     
     count = 0
     for n in lista2:
         if n not in lista1:
             
             count +=1
     return count