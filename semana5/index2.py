class Persona:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def saludar(self):
        return f"Mi nombre es: {self.name} y tengo {self.age} años"
    

class Estudiante(Persona):
    def __init__(self, name, age, grade):
        super().__init__(name, age)    
        self.grade = grade

    def edad(self):
        return f"Estoy cursando: {self.grade} grado"
    
juan = Estudiante("Juan", "20", "septimo")
print(juan.saludar())
print(juan.edad())