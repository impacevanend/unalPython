# lista1 = [3,5,7,10,15,16]
# lista2 = [3,5,10,13]

# def capturar(): 
#     global lista
#     lista = []
    
#     print("Cuántos elementos va a tener la lista")
    
#     n = input()
#     n = int()
    
#     for i in range(0, n):
#         print("Ingresa el Elemento del indice ",i)
#         elemento = input()
#         lista.insert(i, elemento)

# capturar()



# lista1 = ["Carlos",
#         "Juan",
#         "Alberto",
#         "Carlos",
#         "Carlos",
#         "Alberto",
#         "Carlos",
#         "Juan"]

# numeros = [2,3,5,1,4,3,6,7,9,5,8]

# repetidos = []
# archivo = []

# for n in numeros:
#     if n not in archivo:
#         archivo.append(n)
#     else:
#         repetidos.append(n)


#* def candidatos(lista):
#     archivo = []
#     for n in lista:
#         if n not in archivo:
#             archivo.append(n)
#     return archivo

# print(candidatos(lista1))


# lista1=[3,5,7,10,15,16]
# lista2=[3,5,10,13]

# vacio = []


# for n in lista1:
#     print(n)
#     if n not in lista2:
#         vacio.append(n)
        
        

#* def auditoria2(lista1, lista2):
#     archivo = []
#     for n in lista1:
#         if n not in lista2:
#             archivo.append(n)
#     return archivo


# print(auditoria2(lista1, lista2))



lista1 = [1,3,5,6]

lista2 = ["Carlos",
         "Juan",
         "Alberto",
         "Carlos",
         "Carlos",
         "Alberto",
         "Carlos",
         "Juan"]

# archivo = []

# for n in lista1:
#     if lista2[n] == "Carlos":
#         archivo.append(n)
        
   
def auditoria1(lista1,lista2,string):
    archivo = []
  
    for n in lista1:
        if lista2[n] == string:
            archivo.append(n)
    return archivo

print(auditoria1(lista1,lista2,"Carlos"))


        
# lista1=[3,5,7,10,15,16]
# lista2=[3,5,10,13]

# vacio = []

# count = 0


# for n in lista2:
#     print(n)
#     if n not in lista1:
#         vacio.append(n) 
#         count +=1
        
        

# def diferencia(lista1, lista2):
     
#      count = 0
#      for n in lista2:
#          if n not in lista1:
#              count +=1
#      return count


# def diferencia(lista1, lista2):
#     count1 = 0
#     count2 = 0
#     for n in lista2:
#         if n not in lista1:
#             count1 +=1

#     for n in lista1:
#         if n not in lista2:
#             count2 += 1
            
#     if count1 > count2:
#         return count2
#     else:
#         return count1


# print(diferencia(lista1, lista2))
