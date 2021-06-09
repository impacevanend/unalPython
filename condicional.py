"""
*Condicional if

resultado = 50

# resultado = resultado > 10

if resultado > 10 and resultado <20:
    print('La varialbe cumple con la condiciòn.')
else:
    print(f'error la condición no se cumplió: {resultado}')"""

"""
* Condiciola elif
calificacion = 5

if calificacion == 10:
    print('Felicidades, aprobaste la materia con una calificaciòn perfecta.')
elif calificacion == 9 or calificacion == 8:
    print('Felicidades, aprobaste la materia.')
elif calificacion == 7 or calificacion == 6:
    print('Aprobaste')
else:
    print('Reprobaste la materia.')
"""

#*condicional terniario
#calificacion = 10
"""
color = None

if calificacion >= 7:
    color = 'Verde'
else:
    color = 'Rojo'

print(f'La calificación es: {calificacion} {color}')
"""
#color = 'Verde' if calificacion >= 7 else 'Rojo'
#print(f'La calificación es: {calificacion} {color}')

#*Ingresar el primer valor verdadero a la varible utilizando "or"

variable = 'Cody' or 'Código Facilito'#*guardará "Cody".
variable2 = '' or 'Código Facilito'#*guardará "Código Facilito", porque el primer valor es falso.
variable3 = '' or 0 or [] or True #*guardará "True", porque los otros valores son falsos.
print(f'Evaluando primera variable: {variable}. segunda variable: {variable2} \ntercera variable: {variable3}')

listado = []
nombre = 'Cody'
"""
if listado:
    variable = listado
else:
    variable = nombre
"""
#*Refactorizando código con "or"

variable = listado or nombre

print(f'Este es el resultado de la evaluación de "or": {variable}. Porque es el unico valor verdadero.')