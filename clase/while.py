# *explicaciòn inicial
# i = 0

# while i <=6:
#     print(i)
#     i +=1


# * Comparación de varialbes hasta salir del ciclo
# i = 2
# j = 25

# while i < j:
#     print(i,j, sep = ", ")
#     i *= 2
#     j += 10

# print("The end.")
# print(i,j, sep =", ")

#*Uso del break 

# suma = 0

# while True:
#     dato = int(input("Ingrese un número entero "+"a sumar o 0 para salir:"))
    
#     if dato == 0:
#         break
    
#     suma += dato
    
# print("La suma es: "+str(suma))

# *Cambio de break por hacer mientras

# dato = 0
# suma = 0
# bandera = True

# while bandera or dato != 0:
#     bandera = False
#     dato = int(input("Ingrese un número entero "+"a sumar o 0 para salir:"))
    
#     suma += dato

# print("La suma es: " +  str(suma))

#todo problemas
#*listado del uno al 100
# i = 1

# while i<=100:
#     print(f'numero: {i} cuadrado: {i**2}')
#     i +=1

#* pares impares
# i = 1
# while i <=1000:
#     if i%2 == 0:
#         print(f'Número par: {i}')
#     else:
#         print(f'Número impar: {i}')
#     i += 1

i = 10

while  i>0:

    if i%2 == 0:
        print(f'Número par: {i}')
        
    i -= 1