class Estudiante():
    def __init__(self, name, lastName, finalGrade):
        
        self.name = name
        self.lastName = lastName
        self.finalGrade = finalGrade
    def verifyNote(self):
        if(self.finalGrade > "3"):
            print(f"El estudiante {self.name} {self.lastName}  Aprobó")
        else:
            print(f"El estudiante {self.name} {self.lastName}  Reprobo")

students = [
    Estudiante("Juan", "Arteta", "5"),
    Estudiante("Pedro", "Arteta", "2"),
    Estudiante("Carlos", "Arteta", "2"),
    Estudiante("Daniel", "Arteta", "1")
]

for student in students:
    student.verifyNote()
