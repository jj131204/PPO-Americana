class Person():
    def __init__(self, nombre, edad):
        
        self.__nombre = nombre
        self.__edad = edad

    def get_nombre(self):
        return self.__nombre
    
    def get_edad(self):
        return self.__edad
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
        

    def set_edad(self, edad):
        if edad > 0:
            self.__edad = edad
        raise ValueError("La edad debe ser un valor positivo")


persona1 = Person("Juan", 16)
persona2 = Person("Maria", 30)

print(persona1.get_nombre())
print(persona1.get_edad())

persona1.set_nombre("pedro")

print(persona1.get_nombre())
