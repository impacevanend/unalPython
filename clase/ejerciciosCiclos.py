
#lista.append()-> ingresa valor al final.
#lista.insert(index,nuevoElemento))-> añadir nuevo elemento. No remplaza adicina un nuevo elemento.
#lista.extend(nuevaLista)-> adiciona nuevos valores que pertenecen a otra lista.
#Lista.remove(Elemento a eliminar)-> eilimina elementos de la lista
# del lista[indice] -> eiimina los indices de la lista indicados.
# lista.clear()-> elimina todos los elementos de la lista
#lista.sort()-> ordena las listas de manera ascendente predeterminadamente
#lista.sort(reverse=True)-> ordena las listas de manera aescendente predeterminadamente
#lista.min()-> retorna el valor mínimo
#lista.max()-> retorna el valor máximo
# valor in lista -> retorna un valor verdadero o falso (saber la existencia o no de un elemento dentro de una lisa )
# valor not in lista -> verficar que el elemnto no existe dentro de la lista.

#lista = ['Python','Django','Flask','Ruby','Java']


""" 
Pedir 10 números por teclado. Sumarlos y mostar el resultado por pantalla.
"""

"""

lista = []
suma = 0
i = 0

while i < 10 :
    
    lista.append(int(input("Ingrese un numero: ")))
    
    suma = suma + lista[i]
    
    
    i += 1

print(suma)

"""

#*Tabla de multiprica de un número 'n' ciclo for

# Todo con for
# comprobar = True

# while comprobar == True:

#     n = int(input("Ingrese un número entero positivo: "))

#     if n > 0:
#         for i in range(1, 11): # range(númeroInicial, número final+1)-> crea una list1a
#             print(f'{n} por {i} es igual a: {n*i}')
    
#         comprobar = False

#     else:
#         print("El número ingresado no es correcto. Inténtelo nuevamente")
        
        
#Todo con while       
# comprobar = True

# while comprobar == True:

#     n = int(input("Ingrese un número entero positivo: "))

#     if n > 0:
#         i = 1
#         while i <= 10:
            
#              print(f'{n} por {i} es igual a: {n*i}')
#              i +=1
       
    
#         comprobar = False

#     else:
#         print("El número ingresado no es correcto. Inténtelo nuevamente")


#*Escribe un programa que, al recibir como dato un número entero positivo N, calcule el
#*Resultado de la siquiente serie:

# 1 + (1/2) + (1/3)+ (1/4) + ... + (1/n)

#* Si el usuario escribe un número incorrecto, programa no se ejecuta. En cambio,pregunta 
#* de nuevo por la información que el dato ingresado sea correcto

#n = int(input("Ingrese un número para la serie: "))

# for i in range(1, n):
#     valor = i/n
#     print(valor)

# print(f'El valor de la serie es: {valor}')

# todo con while
# comprobar = True


# while comprobar == True:
    
#     n = int(input("Ingrese un número entero positivo: "))

#     if n > 0 :
#         print("Es correcto")
#         resultado = 0
    
#         for i in range(1, n+1):
#             resultado  += (1/i)
    
#         print(f'El resultado de la serie es: {resultado}')
    
#         comprobar = False

#     else:
#         print("El número ingresado no es correcto. Inténtelo nuevamente.")
        

# todo con while  
        
# comprobar = True


# while comprobar == True:
    
#     n = int(input("Ingrese un número entero positivo: "))

#     if n > 0 :
       
#        comprobar = False
#        resultado = 0
       
#        i = 1
       
#        while i <= n:
           
#            resultado += (1/i)
#            i += 1
        
#        print(f"El resultado de la serie es: {resultado}")

#     else:
#         print("El número ingresado no es correcto. Inténtelo nuevamente.")


#* Construye un programa que, al recibir como datos N números naturales, determine cuántos de ellos son positivos, negativos
#* o nulos

#* Si el usuario escribe un número incorrecto, programa no se ejecuta. En cambio,pregunta 
#* de nuevo por la información que el dato ingresado sea correcto

# contador = int(input("¿Cuántos número desea ingresar"))

# for numero in range(1, contador+1):
       
#     numero = int(input("Ingrese un número natural"))
    
#     if numero > 0:
#         print("Número positivo"
#               )
#     elif numero < 0:
#         print("Número es negativo")
        
#     else:
#         print("Número es nulo") 

# comprobar = True

# while comprobar == True:

#     n = int(input("Ingrese la cantidad de datos que desea procesar: "))

#     if n > 0:
        
#         positivos = 0
#         negativos = 0
#         nulos = 0
        
#         for i in range(n):
            
#             dato = int(input("Ingrese un número natural: "))
            
#             if dato >0:
#                 positivos +=1
            
#             elif dato < 0:
#                 negativos += 1
#             else:
#                 nulos += 1
            
#         print(f'La cantidad de números positivos es: {positivos}\nLa cantidad de números negativos es: {negativos}\nLa cantidad de números nulos es: {nulos}\n')
#         comprobar = False
#     else:
#         print("El número ingresado no es correcto. Inténtelo nuevamente.")



# *Construye un programa que, al recibir como datos el peso, la altura y el género de n persona que pertenecen a un estado
# *de un país, obtenga el promedio del peso y el promedio de la altura, tando de la población masculica como de la
# *femeninda

n = int(input("Ingrese la cantidad de personas a registrar"))



contadorM = 0
contadorF = 0

pesoM = 0
pesoF = 0

alturaM = 0
alturaF = 0

promedioM = 0
promedioMF = 0

promedioMA = 0
promedioMAF = 0



for i in range(n):
    
    genero = input("Ingrese su genero: ")
    
    
    if genero == "masculino":
        alturaM = float(input("Ingrese su altura: "))
        pesoM = float(input("Ingrese su peso: "))
        contadorM +=1
        alturaM += alturaM
        pesoM += pesoM
        
    elif genero == "femenino":
        
        alturaF = float(input("Ingrese su altura: "))
        pesoF = float(input("Ingrese su peso: "))
        
        contadorF +=1
        alturaF += alturaF
        pesoF += pesoF
        
    
promedioM = pesoM/contadorM
promedioMA = alturaM/contadorM

promedioMF = pesoF/contadorF
promedioMAF = alturaF/contadorF
        
print(f'peso: {pesoM} altura: {alturaM} peso:cantidad:{contadorM} promedio peso: {promedioM} promedio altura:{promedioMA}')
print(f'peso: {pesoF} altura: {alturaF} peso:cantidad:{contadorF} promedio peso: {promedioMF} promedio altura:{promedioMAF}')
    
    
        
        
        