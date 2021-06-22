def potencia(x, n):
    pow = 1
    for i in range(1, n+1):
        
        pow *= x
    return pow   

def factorial(n):

    fact = 1
    for i in range(1,n+1):
        
        fact *=i
    return fact   

def exponencial(x,n):
    
    suma = 0
    
    for i in range(n+1):
        
        suma += potencia(x, i)/ factorial(i)
    return suma
    
  

numero = int(input("Ingrese el nùmero natual: "))
real = float(input("Ingrese el nùmero real: "))
    
#print(f"La potencia del nùmero es: {potencia(real,numero)}")
#print(f"El factorial del nùmero es: {factorial(numero)}")

print(f"la aproximación requerida es: {exponencial(real, numero)}")