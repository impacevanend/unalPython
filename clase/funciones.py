#*Función cuadrado

def f(x):
    return x ** 2

#print(f(2))

#*área circulo

def area(radio):
    pi = 3.14159265
    return pi * radio ** 2

#print(f'El area del circulo es: {area(10)}')

#*área rectangulo

def area_rectangulo(largo, ancho):
    return largo * ancho

#print(f'El area del rectangulo es: {area_rectangulo(2,10)}')
"""
largo = float(input("Largo del rectángulo: "))
ancho = float(input("Ancho del rectángulo: "))
print("El área del rectángulo es: ", end="")
print(area_rectangulo(largo,ancho))"""

#* Ley Coulomb
KAPPA = 9E+9

print(KAPPA)


def ley_coulomb(Q1,Q2,r):
    modulo = KAPPA * Q1 * Q2 / r**2
    return modulo

carga1 = float(input("Carga 1: "))
carga2 = float(input("Carga 2: "))
distancia = float(input("Distancia entre cargas: "))
print("El módulo de la fuerza es: ", end="")
print(ley_coulomb(carga1,carga2,distancia))



