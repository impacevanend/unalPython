""" 
Pedir 10 números por teclado. Sumarlos y mostar el resultado por pantalla.
"""



#lista = ['Python','Django','Flask','Ruby','Java']

lista = []
suma = 0
i = 0

while i < 10 :
    
    lista.append(int(input("Ingrese un numero: ")))
    
    suma = suma + lista[i]
    
    
    i += 1

print(suma)




