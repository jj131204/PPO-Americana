class Vehiculo:
    def __init__(self, marca, año):
        self.marca = marca
        self.año = año
    
    def type(self):
        return f"El vehiculo es: {self.marca} del año {self.año}"
    

class Coche(Vehiculo):
    
    def __init__(self, marca, año, modelo):
        super().__init__(marca, año)
        self.modelo = modelo

    def printModelo(self):
        return f"El modelo es: {self.modelo}"
    
firulais = Coche("Renault", "2000", "Sandero")
print(firulais.type())
print(firulais.printModelo())