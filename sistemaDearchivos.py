"""
*Leer archivo
with open("files/data.txt") as f:
    data = f.read()
    print(data)
"""
    
"""
*Escribir archivo
with open("files/wdata.txt", "w")as f:
    data = "nuevamente estamos escribiendo en el archivo"
    f.write(data)
    f.write(data)
    f.write(data)

"""

"""
*Agregar nueva información sin sobreescribir
with open("files/wdata.txt", "a")as f:
    data = "mas cosas \n"
    f.write(data)
    f.write(data)
    f.write(data)
"""
"""
with open("files/wdata.txt", "x")as f:
    data = "mas cosas \n"
    f.write(data)
    f.write(data)
    f.write(data)
"""    

"""
*Leer todo el archivo:

with open("files/data1.txt","r", encoding="utf-8") as f:
    print(f.read())
"""

"""
*Leer por cantidad de lineas
with open("files/data1.txt","r", encoding="utf-8") as f:
    linea1 = f.read(10)
    linea2 = f.read(10)
    print(linea1, end=" ")
"""

"""
*Leer una linea
with open("files/data1.txt","r", encoding="utf-8") as f:
    linea1 = f.readline()
    
    print(linea1)
"""
"""
*Recorrer un archivo
with open("files/data1.txt","r", encoding="utf-8") as f:
    for line in f:
        print(line, end=" ")
"""

"""
*Busca caracter y lo rrecorre el archivo
"""
"""
with open("files/data4.txt","r", encoding="utf-8") as f:
    for line in f:
        f.seek(11, 0)
        for line in f:
            print(line, end=" ")
"""

#*Abrir y leer un archivo
"""
with open("files/data.txt", "r") as f:
    data = f.read()
    print(data)

"""

#*Escribir y crear un archivo
"""
Abre el archivo en modo de escritura creando el archivo si no existencia
o sobreescribiendo el archivo si existe.
"""
"""
with open("files/wdata.txt","w") as f:
    data = "Estamos en el archivo 123\n"
    f.write(data)
    f.write(data)
    f.write(data)
"""

#*Agregar contenido a un archivo existente
"""
with open("files/wdata.txt", "a") as f:
    data = "más cosas \n"
    f.write(data)
    f.write(data)
    f.write(data)
"""

#*Otros modos de abrir archivos Python son:
"""
r+ ->(read/write)hace cambios al archivo y a la vez leerlo el punto se ubica
al principio
a+->(append/write)Se abre el archivo para escribir y leer del
archivo. El punto se ubica al final del archivo
-x (exclusive creation ): usado exclusivamente para crear
un archivo. Si existe un archivo con el mismo nombre la
funci ́on fallar ́a.
b : Para leer archivos binarios se agrega la letra b al final del
modificador. Por ejemplo, para leer “rb”, y los otros ser ́ıan
“wb”, “ab”, “r+b” y “a+b”.

"""

#*Lecturas de archivos de texto
"""
with open("files/data1.txt", "r") as f:
    print(f.read())
"""
    
#*Lecturas de un archivo con tíldes
#Agregar parametro encoding="utf-8"
"""
with open("files/data1.txt", "r", encoding="utf-8") as f:
    print(f.read())
"""
    
#* Leer una fracción, de un archivo read("cantidad bytes a leer")
"""
with open("files/data1.txt","r",encoding="utf-8") as f:
    linea1 = f.read(6) #Lee los 6 primero  bytes
    linea2 = f.read(10) #Lee los 10 primero  bytes
    
    print(linea1)
    print(linea2)
"""
    
#*Leer archivo línea por línea
"""
with open("files/data1.txt", "r",encoding="utf-8") as f:
    linea1 = f.readline() #lee la primera linea
    linea2 = f.readline() #lee la segunda linea
    
print(linea1,end=" ")
print(linea2,end=" ")
"""
"""
"""
#*Cargar listas de archivo como una lista
"""
with open("files/data1.txt","r", encoding="utf-8")as f:
    print("Nombre del archivo: ", f.name)
    lista = f.readlines()
    
print(lista)
"""
#Todo Sección del profesor Manuel Gozales (leyendo archivos de texto)#
#*Nota: Mantener datos para sesiones posteriores se designa como "persistencia" 

#archivo = open("files/saludo.txt", "r")

#texto = archivo.read() #*Convierte a string el contenido del archivo

#texto = archivo.readlines()#*Convierte un archivo en lista

#texto = archivo.readline()#*Solo devuleve una sola linea.
"""

while True:
    #*Este bucle lee linea por linea sin cargar todo el archivo a memoria
    linea = archivo.readline().strip()
    if linea == "":
        break
    else:
        print(linea)
"""
    
"""
lista_formateada = []

for elemento in texto:

    linea = elemento.strip("\n")
    lista_formateada.append(linea)
    
    #*Con este for, se puede recorrer el archivo y eliminar los saltos de linea.
print(lista_formateada) 
"""
"""
archivo.close() #*Cerrar el archivo despues de utilizarlo.
"""
"""
todo utf-8
archivo = open("files/saludo.txt", "r", encoding="utf-8")
texto = archivo.read()
archivo.close()
print(texto)
"""
#Todo contando lineas de un archivo 

#archivo = open("files/2000-0.txt", "r", encoding="utf-8")

#*Conando los datos de la lista creada
#lineas = archivo.readlines()
#print(len(lineas))
#*Contando teniendo el texto entero
"""
texto = archivo.read()

n = 0

for i in texto:
    
    
    if i == "\n":
        n +=1
"""
#Todo realizando el conteo linea a linea con readline
"""
n = 0

while True:
    if archivo.readline() != "":
        n += 1
    else:
        break  

print(n)
archivo.close()
"""        
#todo otra forma de contar lineas 
"""
n = 0

for linea in archivo:
    print(linea)
    n +=1
    
    if n == 10: #*Muestra sólo las diez primeras lineas.
        break

print(f"Contador de lineas: {n}")
archivo.close()
"""
#TodoContando palabras II

"""
Mostrar qué cinco palabras de más de 12 letras aparecen más veces en el Quijote, y cuántas veces
paparece cada una.
"""
"""
archivo = open("files/2000-0.txt", "r", encoding="utf-8")

texto = archivo.read()

archivo.close()

lista = texto.split() #*Separa todas las palabras del texto por espacio.

palabras = {}


for elemento in lista:
    palabra = elemento.strip(".").strip(",").strip(";").strip(":")
    if len(palabra)>12:
        palabras.setdefault(palabra,0)
        palabras[palabra] +=1



for i in range(5):
    numero_mayor = 0
    for palabra in palabras:
          if palabras[palabra] > numero_mayor:
              numero_mayor = palabras[palabra]
              palabra_mayor = palabra
    print(palabra_mayor, ":", numero_mayor)
    del palabras[palabra_mayor]
     
"""

#*Métodos Seek y tell


archivo = open("files/2000-0.txt", "r", encoding="utf-8")

texto = archivo.read()
print(texto)

archivo.close()