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

def rle_encode(data):  
    encoding = ''
    prev_char = ''
    count = 1

    if not data: return 'vacio'

    for char in data:
        # If the prev and current characters/ Si los caracteres anterior y actual
        # don't match... no coinciden ...
        if char != prev_char:
            # ...then add the count and character .../ luego agregue el recuento y el carácter
            # to our encoding/ a nuestra codificación
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            # Or increment our counter /O incrementar nuestro contador
            # if the characters do match/ si los personajes coinciden
            count += 1
    else:
        # Finish off the encoding /Finish off the encoding
        encoding += str(count) + prev_char
        return encoding
    
print(rle_encode('TTTAAACCCCHZZZOOOHMFFFFF'))

#*3T3A4C1H3Z3O1H1M5F
#*3 3 4 1 3 3 1 1 5
#* T A C H Z O H M F


    
