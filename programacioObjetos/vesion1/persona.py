class Persona:
    
    #*inicializa los objetos de la clase
    def __init__(self, nombre):
        self.nombre = nombre
        self.calle = 1
        
    def situacion(self):
        return "{}, estás en la calles {} ".format(self.nombre, self.calle)
        
    def moverse(self, velocidad):
        if velocidad == '1':
            self.calle += 1
        elif velocidad == '2':
            self.calle += 2
        else:
            self.calle += 3


jose = Persona("Jose")
juan = Persona("Juan")

#jose.nombre= "Jose"
#juan.calle = 5

# print(jose.calle)
# jose.moverse("2")
# print(jose.calle)
# jose.moverse("3")
# print(jose.calle)


