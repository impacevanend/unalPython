import json

with open("files/monitoria.json", "r") as f:
    archivo = json.load(f)
    
    
print(archivo["cedula"])