class Estudiante():
    def __init__(self, name, calificacion):
        
        self.name = name
        self.calificacion = calificacion

    def verificar_calificacion(self):
        if self.calificacion < 50:
            return
        print(f"{self.name} ha aprobado con una calificación de {self.calificacion}")


estudiante1 = Estudiante("Ana", 45)
estudiante2 = Estudiante("Luis", 75)

estudiante1.verificar_calificacion()
estudiante2.verificar_calificacion()