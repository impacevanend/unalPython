producto = 20

if producto > 5 and producto< 10:
    producto *=0.95
elif producto > 10  and producto<= 20:
    producto *=0.90
elif producto > 20:
    producto *=0.80
else:
    producto

print(f'El valor final es {producto}')    
