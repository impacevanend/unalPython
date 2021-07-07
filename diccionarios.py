"""
Estructura de clave:valor.
22:'SSH'
80:'HTTP'
'Color':'Rojo'


Un diccionario es una colección de 
esas parejas; cada una de ellas es
un registro.
{1:2,2:3,...,n:m}
"""
"""
puertos ={22:'SSH',23:'Tenet',88:'HTT',3306:'HTTPS'}

print(puertos)
"""
"""
dic = {1:"g",2:"b",3:"e"}

dic2 ={1:"h",5:"r",3:"f"}
"""

"""
for key, value in dic.items():
    
    if dic in dic2:
     print("verdadero")
    else:
        print("falso") 
"""
"""
for key in dic:
    if key in dic2:
        print(f"No son iguales")
        break
    else:
        print("Son iguales")
"""
"""
votos = ["T","T", "T","A","A","A","C","C","C","C","H","Z","Z","Z","O","O","O","H","M","F","F","F","F","F"]




repetido = []
cuenta = []

for i in votos:
        if votos.count(i) > 1 and i not in repetido:
            repetido.append(i)
            cuenta.append(votos.count(i))
        
        
print(repetido, cuenta)
        
"""

"""
TTTAAACCCCHZZZOOOHMFFFFF
"""

# def rle_encode(data):  
#     encoding = ''
#     prev_char = ''
#     count = 1

#     if not data: return 'vacio'

#     for char in data:
#         # If the prev and current characters/ Si los caracteres anterior y actual
#         # don't match... no coinciden ...
#         if char != prev_char:
#             # ...then add the count and character .../ luego agregue el recuento y el carácter
#             # to our encoding/ a nuestra codificación
#             if prev_char:
#                 encoding += str(count) + prev_char
#             count = 1
#             prev_char = char
#         else:
#             # Or increment our counter /O incrementar nuestro contador
#             # if the characters do match/ si los personajes coinciden
#             count += 1
#     else:
#         # Finish off the encoding /Finish off the encoding
#         encoding += str(count) + prev_char
#         return encoding
    
# print(rle_encode('TTTAAACCCCHZZZOOOHMFFFFF'))

# #*3T3A4C1H3Z3O1H1M5F
# #*3 3 4 1 3 3 1 1 5
# #* T A C H Z O H M F


"""
Un diccionario es una colecci ́on desordenada.
Un diccionario es una colecci ́on de parejas clave-valor donde los valores
pueden ser recuperados principalmente por su clave.

*Método update: agrega ítems de un diccinario
*en otro
"""

# dict_ports = {22:"SSH",
#                80:"HTTP"}

# dict_ports2 = {53:"DNS",
#                443:"HTTPS"}

# print(dict_ports)

# dict_ports.update(dict_ports2)

# print(dict_ports)
    
    
# *Comparadores
"""
Se usan los operadores convencionales (==, !=) para comparar
diccionarios.

"""

# a = {123:"Rojas",87:"Rosas"} == {87:"Rojas",123:"Rojas"}
# b = {"Rosas":123} != {"rosas":123}


#* Accediendo

# from typing import Protocol


# puertos ={22:"SSH", 23:"Telnet", 80:"HTTP", 3306:"MySQL"}
# Protocolo = puertos[22]
# print(Protocolo)


#* Agregando/Modificando
"""
Agrega (si no existe) o modifica (si existe) el
valor de un ítem
"""

# puertos = {80:"HTTP",23:"SMTP", 443:"HTTPS"}
# print(puertos)

# puertos[23] = "Telnet"

# puertos[110] = "POP"

# print(puertos)


# *Eliminando elementos

"""
El comando "del" permite elimintar el 
item con la clave dada
del -> si no se eindica la clave, borra
todo el diccionario
"""

# puertos = {22:"SSH", 
#            23:"Telnet", 
#            80:"HTTP",
#            3306:"MySQL"}

# print(puertos)

# del puertos[23]

#* Consultando un diccionario

"""
Posible determinar si en un diccionario
exite un item.
"""

# puertos = {80:"HTTP", 23:"SMTP", 443:"HTTPS"}
# if 80 in puertos:
#     print("yes")
    
# if 110 not in puertos:
#     print("no")

# *Iterando un diccionario
"""
Es posible iterar un diccioanrio 
usando el ciclo for
"""

# dic_ports ={22:"SSH",
#            23:"Telnet",
#            80:"Http"}

# for key in dic_ports:
#     print(key)

# *Iterando un diccionarioII
"""
Es posible usar el ciclo for y el método items
para obtener los items de un diccionario
"""

# dict_ports = {22:"SSH",
#               23:"Telnet",
#               80:"HTTP"}


# for k,v in dict_ports.items():
#     print(f'Key: {k} value: {v}')


# Todo Métodos:
# *Longitud

"""
Determina el número de items de
un diccionario
"""

# puertos = {80:"HTTP", 23:"SMTP", 443:"HTTPS"}

# print(len(puertos))

# *Oteniendo valores

"""
Se puede obtener el valor de un item
a partir de la llave.
"""

# dict1 ={"a":1, "b":2, "c":3}
# print(dict1.get("a"))
# print(dict1.get("d","clave no encontrada."))


# *Máximo y mínico (max, min)


# puertos = {80:"HTTP", 23:"SMTP", 443:"HTTPS"}
# print(max(puertos))
# print(min(puertos))

#*Listas de claves y valores (keys, values)
"""
Crea una lista con las claves o con los valores
"""
# dict1 = {"a":1,"b":2,"c":3}
# print(list(dict1.keys()))
# print(list(dict1.values()))

# *Convertir a diccionarios
"""
El miso procedimiento también aplica
para tuplas (tener en cueta el par de valores
clave, valor).
"""

# puertos = [[80,"HTTP"],[20,"ftp"],[23,"telnet"]]
# d_port = dict(puertos)
# print(d_port)

# *Clear entradas

"""
El método clear se usa para eliminar todos
item de un diccionario.
"""

# dict_ports = {22:"SSH",23:"tenet",80:"HTTP"}
# print(dict_ports)
# dict_ports.clear()
# print(dict_ports)

# *Copiar diccionarios

port = {80:"HTTP",23:"SMTP",443:"HTTPS"}
copy_port = port.copy()
false_port = port

print(id(copy_port))#todo es diferente
print(id(port))#*Son iguales
print(id(false_port))#*Son iguales
