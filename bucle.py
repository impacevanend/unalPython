
"""
listado = [1,2,3,4,5,6]

*Program de practica

for lis in listado:
    if lis % 2 == 0:
        print(lis)
        continue
"""
#*Bucle Whyle (se utiliza si no se conoce la cantidad de iteraciones a realizar.)
contador = 1  #* importante-> indica el número de veces que recorera el ciclo

while contador <= 10:
    print(contador)
    contador += 1 #* muy importante-> si no se indica el ciclo será infinito.

numero = 12345578979
contador_digitos = 0

while numero >= 1:

    contador_digitos +=1
    numero /= 10
else:
    print('Fin del ciclo while')#* El termino "else", en un ciclo "while", es opcional.

print(f'La cantidad de digitos es: {contador_digitos}')




