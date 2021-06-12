from math import pi


"""
Volumen esfera
V = 4/3 πr**3

Volumen cono
V = 1/3 πr**2 h

"""

"""
todo funcion volumen de solido
def volumen_esfera(re):
    return (4/3) * pi * re**3 
    
def volumen_cono(re,h):
    return (1/3) * pi * re**2 * h 
    
radio_esfera = float(input("Ingrese el radio de la esfera: "))
radio_cono = float(input("Ingrese el radio del cono: "))
altua_cono = float(input("Ingrese el radio de la altura: "))

print(f'El volumen del solido:{volumen_esfera(radio_esfera)+volumen_cono(radio_esfera, altua_cono)}')
"""

"""
Todo cantidad de carne

def cantidad_carne(tipo,q):
    if tipo == "gallina":
        return 6 * q
    elif tipo == "gallo":
        return 7 * q
    elif tipo == "pollito":
        return 1 * q
    
tipo_animal = input("Por favor, ingrese el tipo de animal: ")
cantidad_animal = input("Por favor, ingrese el cantidad de animales: ")
    
    
print(f'La cantidad de {tipo_animal}/s es de: {cantidad_carne(tipo_animal,cantidad_animal)}')

"""


"""
Mi mama me manda a comprar P panes a $ 300 cada uno, M bolsas
de leche a $ 3300 cada una y H huevos a $ 350 cada uno. Hacer un
programa que me diga las vueltas (o lo que quedo debiendo) cuando
me da un billete de B pesos.
"""

 

def calcular_comprar(p,b,h):
    
    p_panes = 300 * p
    m_bolsas = 3300 * b
    h_huevos = 350 *h
    
    return p_panes + m_bolsas + h_huevos


panes = int(input("Por favor, ingrese cuàntos panes desea comprar: "))
leche = int(input("Por favor, ingrese cuàntas bolsas de leche desea comprar: "))
huevos = int(input("Por favor, ingrese cuàntos huevos desea comprar: "))

b_billete = int(input("Con qué billete deseas pagar la compra.: "))

valor_total = calcular_comprar(panes, leche, huevos)
vueltas = b_billete -  valor_total #valor positivo o negativo

if vueltas > 0:
    print(f'Su vueltas son: {vueltas}')
elif vueltas == 0: 
    print(f'No tienes vueltas a tú favor.: {vueltas}')
else:
    print(f'Quedas deviendo: {abs(vueltas)}') #-3200
    
    
    
    
    