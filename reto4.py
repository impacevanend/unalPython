import json
productos_existentes = '{"aguardiente": 9168, "platos": 11867, "papas": 19532, "tomate": 18868, "arepas": 10818, "res": 8198, "pollo": 12832}'


data = json.loads(productos_existentes)

ingredientes_tienda = "tenedores papas costillas platos pollo tomate res ron"
ingredientes_tienda = ingredientes_tienda.split()

total = 0

resultado = []

for i in range(len(ingredientes_tienda)):
    for key in data:
        if ingredientes_tienda[i] == key:
            resultado.append(key)
            total += data[key]
            
print(total)
print(" ".join(resultado))

    
    