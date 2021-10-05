from persona import Persona
from zombi import Zombi
import os

os.system("cls")

print()
print(" La ciudad se ha llenado de zombis.")
print(" Estás en la calle 1 y has de llegar")
print(" a la calle 40 para poder salvarte")
print()
print(" Los zombis avanzan 1, 2 ó 3 calles.")
print(" Tú puedes avanzar 1, 2 o 3 calles.")
print()

numero = ""
while numero not in ("1","2","3","4"):
    numero = input(" Número de jugadores (1/4): ")
    
jugadores = []
for i in range(1,int(numero)+1):
    nombre = input(" Nombre del "+ str(i) + "° jugador: ").capitalize()
    jugador = Persona(nombre)
    jugadores.append(jugador)
    
horda = []
for i in range(10):
    z=Zombi()
    horda.append(z)


while len(jugadores) > 0:
    os.system("cls")
    
    print(" NOMBRE - CALLE - ENERGÍA")
    print(" ------------------------")
    for jugador in jugadores:
        nom, cal, ene = jugador.situacion()
        print("{:8} -  {:2}      {:2}".format(nom, cal, ene))
    print()
    
    calles = []
    for zombi in horda:
        calles.append(zombi.calle)
    
    calles.sort()
    print(" Hay zombis en las calles: ")
    print()
    print(" ", end="")
    for elemento in calles:
        print(elemento, end=" ")
    print()
    print()
    
    ganadores = []
    for jugador in jugadores:
        if jugador.calle >= 40:
            ganadores.append(jugador)
    if len(ganadores)>0:
        for jugador in ganadores:
            print(" {}, has escapado de los zombis.".format(jugador.nombre))
            print(" Has ganado la partida.")
            print()
            break
    
    for jugador in list(jugadores):
        if jugador.energia <= 0:
            print(" {}, has perdido toda la energía. Estás comido.".format(jugador.nombre))
            jugadores.remove(jugador)
            
    for jugador in list(jugadores):
        for zombi in horda:
            if zombi.calle == jugador.calle:
                if jugador in jugadores:
                    print(" {}, un zombi te ha visto. Has perdido".format(jugador.nombre))
                    jugadores.remove(jugador)
                    
    print()
    for jugador in jugadores:
        velocidad = ""
        while velocidad not in("1","2","3"):
            velocidad = input(" {}, cuánto quieres correr (1/2/3)".format(jugador.nombre))
        jugador.moverse(velocidad)
        
    for z in list(horda):
        z.moverse()
        if z.no_visible():
            horda.remove(z)
else:
    print(" Todos han sido comidos. No hay ganadores.")
    print()