from math import pi


"""
Volumen esfera
V = 4/3 πr**3

Volumen cono
V = 1/3 πr**2 h

"""


def volumen_esfera(re):
    return (4/3) * pi * re**3 
    
def volumen_cono(re,h):
    return (1/3) * pi * re**2 * h 
    
radio_esfera = float(input("Ingrese el radio de la esfera: "))
radio_cono = float(input("Ingrese el radio del cono: "))
altua_cono = float(input("Ingrese el radio de la altura: "))

print(f'El volumen del solido:{volumen_esfera(radio_esfera)+volumen_cono(radio_esfera, altua_cono)}')