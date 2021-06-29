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

with open("files/salesJan2009.csv","r")as f:
    lines = f.readlines()
 
total = 0  
for line in lines:
    if "United Kingdowm"  in line:
        registro = line.split(",")
        total += 1
        
    print(total)
        