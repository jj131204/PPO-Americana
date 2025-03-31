class Student:
    def __init__(self, name, age):

        self.__name = name
        self.__age = age
        self.__grades = []

    def add_grade(self, grade):
        if not (0 <= grade <= 100):
            raise ValueError("El numbero debe estar en 0 y 100")
        self.__grades.append(grade)

    def get_average(self):
        if not self.__grades:
            return 0.0
        return sum(self.__grades) / len(self.__grades)

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

# Example usage
student = Student("Alice", 20)
print(student.get_name())
print(student.get_age())

student.add_grade(85)
student.add_grade(90)
student.add_grade(78)
print(student.get_average())
