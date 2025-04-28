class Animal:
    def __init__(self, name, specie):
        self.name = name
        self.specie = specie
    
    def type(self):
        return f"el animal es un: {self.name} de la espcie {self.specie}"
    

class Perro(Animal):
    
    def __init__(self, name, specie, raza):
        super().__init__(name, specie)
        self.raza = raza

    def razaPrint(self):
        return f"La raza es: {self.raza}"
    
firulais = Perro("firulais", "Perro", "pincher")
print(firulais.type())
print(firulais.razaPrint())