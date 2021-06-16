"""

if 2 < 3:
    print("Hola")
    

while 2 < 3:
    
    print("Hola")
"""

"""
*Programa que muestre en pantalla una secuencia de números del 1 al 10
"""
"""
i = 1

while i <= 10:
    print(i)
    i +=1
"""
"""
*Programa que muestre en pantalla una secuencia de número del 20 al 0
"""
"""
i = 20

while i >= 0:

    print(i)
    i -= 1
"""   
"""
*Programa que pregunte al usuario si quiere seguir jugando
"""

"""
decision = True

while decision:

    ingresoValor = input("desea seguir jugando")
    
    if ingresoValor == "no":
        decision = False
"""
"""
print("Vamos a jugar.")

jugando = "s"

while jugando == "s":
    print("Seguimos jugando.")
    jugando = input("¿Quieres seguir jugando (s/n)")
    
print("Fin del programa")
"""

"""
*Programa que te pide que introduzcas un número que esté entre el 10 y el 20. Si es correcto
*te diga que estás en el rango, y te pidad otro. Hasta que le des un número fuera del rango y 
*se acabe el programa.
"""
"""

n = int(input("Dime un número entre el 10 y el 20: "))


while n >= 10 and n <= 20:  # 10 <= n <= 20
    print("Correcto estás en el rango")
numero = 10

disparador = True

while disparador:
    
    
    
    if numero >= 10 and numero <= 20:

        numero = int(input("Por favor, ingrese un número que este entre el 10 y el 20.: "))
        print("Estás en el rango.")
    else:
        disparador = False
        print("No estás en el rango.")
    
        
    

print("Fin del progrma.")
"""
"""


n = int(input("Dime un número entre el 10 y el 20: "))


while n >= 10 and n <= 20:  # 10 <= n <= 20
    
    print("Correcto. Estás en el rango.")
    n = int(input("Dime otro número: "))
    
else:
    print("Te has salido del rango.")
"""
#*Cuántas veces se ejecuta el bucle
"""

#*Programa que te pide que adivines un número del 1 al 10 y te pida
#*números constantemente hasta que lo adivines.
print("Vamos a jugar.")

jugando = "s"
veces = 0

while jugando == "s":
    
    veces +=1
    
    print("Seguimos jugando.")
    print(f"Hemos jugado {veces} veces.")
    jugando = input("¿Quieres seguir jugando (s/n)")
    
print("Fin del programa")

"""

#*Programa que te pide que adivines un número del 1 al 10 y te pida
#*números constantemente hasta que lo adivines.
#*Añade un contador que te diga los intentos que necesitado.
"""

numero = int(input("Ingrese un número del 1 al 10."))

contador = 0

adivinar = 3

while numero != adivinar:
    contador += 1
    numero = int(input("Intenta nuevamente"))
    print(f"número de intentos {contador}")
    
    
else:
    print("¡Adivinaste!")
    
"""
intento = input("Dime un número del 1 al 10: ")
numero = "5"
veces = 1

while intento != numero:
    intento = input("No es correcto. Inténtalo otra vez: ")
    veces =+ 1
else:
    print(f"Has acertado. Has necesitado {veces} veces.")
