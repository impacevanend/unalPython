"""
cadena = "El sol sale por el este. Se pone por el oeste."
"""

#* print(cadena.split()) crea una lista cortando por espacio, si no se le indica el separador
"""
lista = cadena.split()  

print(lista)

nueva_lista= "".join(lista)#*Join junta una lista y la convierte en una cadena

print(nueva_lista)
"""
"""
telefonos = {"José":1234,
             "Maria":3456,
            "Andrés":5678,
             "Lucia":9876}
"""

#*Las claves no deben ser reptidas (contrae errores) .Los valores si pueden ser pedidos
#*Son elemento no ordenados, se accede por su clave.

#print(telefonos["Maria"])#*Accediendo al valor.
#print("Julia" in telefonos)#*Resultado valor lógico.

#*Condicional con diccionarios.
"""
if "Julia" in telefonos:
    print(telefonos["Julia"])
else:
    print("Esa clave no existe")
"""

#*Asignación de nuevo valor a una clave
"""
telefonos["Jorge"] = 6543
telefonos["Maria"] = 7890

#*Eliminar un elemento de un diccionario.(Si no se indica la clave en especifico, puede borrar todos los elementos del diccionario)
del telefonos["Andrés"]
"""

#*Crear agenda teleonica
"""
telefonos = {"José":1234,
             "Maria":3456,
             "Lucia":7890,
             "Andrés":6543}

consultando = True

while  consultando:
    print()
    print("MIS TELEFONOS")
    print("-------------")
    print("1. Consultar")
    print("2. Añadir")
    print("3. Modificar")
    print("4. borrar")
    print("5. Salir")
          
    opcion = ""
    while opcion not in ("1","2","3","4","5"):
        opcion = input("->")
    
    if opcion == "1":
        nombre = input("Nombre: ")
        if nombre not in telefonos:
            print("Ese nombre no existe.")
        else:
            telf = telefonos[nombre]
            print(f"{nombre}: {telf}")
            consultando = False
            
    elif opcion == 2:
        nombre = input("Nombre: ")
        if nombre not in telefonos:
            print("Ese nombre ya está en la agenda.")
        else:
            telf = int(input("Teléfono: "))
            telefonos[nombre] = telf
            print("El teléfono se ha añadido correctamente")


"""

#*Método get

mi_agenda = {
    
    "Alicia":2222,
    "Roberto":1111,
    "Lucia":3333,
    "Andrés":5555
    
}

print(mi_agenda.get("Jorge"))#*Si está el valor que corresponde a la clave lo muestra, de lo contrario muesta el resultado none