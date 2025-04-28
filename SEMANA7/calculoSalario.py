class Transporte():
    def tipo_transporte(self):
        pass

class Coche(Transporte):
    def tipo_transporte(self):
        return "Es un transporte terrestre"
    
class Avion(Transporte):
    def tipo_transporte(self):
        return "Es un transporte aereo"
    
    
class Barco(Transporte):
    def tipo_transporte(self):
        return "Es un transporte maritimo"
        

coche = Coche()
avion = Avion()

print(coche.tipo_transporte())
print(avion.tipo_transporte())