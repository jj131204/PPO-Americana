# Clase base Persona
class Persona:
    def __init__(self, nombre, edad, documento):
        self.__nombre = nombre
        self.__edad = edad
        self.__documento = documento

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, nueva_edad):
        if nueva_edad >= 0:
            self.__edad = nueva_edad
        else:
            raise ValueError("La edad no puede ser negativa.")

    @property
    def documento(self):
        return self.__documento

    @documento.setter
    def documento(self, nuevo_documento):
        self.__documento = nuevo_documento

class Paciente(Persona):
    def __init__(self, nombre, edad, documento, diagnostico):
        super().__init__(nombre, edad, documento)
        self.__diagnostico = diagnostico
        self.__historial = []

    def agregar_historial(self, entrada):
        self.__historial.append(entrada)

    def ver_historial(self):
        return self.__historial

    def ver_diagnostico(self):
        return self.__diagnostico

    def actualizar_diagnostico(self, nuevo_diagnostico):
        self.__diagnostico = nuevo_diagnostico

class Doctor(Persona):
    def __init__(self, nombre, edad, documento, especialidad):
        super().__init__(nombre, edad, documento)
        self.__especialidad = especialidad

    def ver_especialidad(self):
        return self.__especialidad

    def modificar_diagnostico(self, paciente, nuevo_diagnostico):
        if isinstance(paciente, Paciente):
            paciente.actualizar_diagnostico(nuevo_diagnostico)
        else:
            raise TypeError("El objeto no es un Paciente.")


paciente1 = Paciente(nombre="Juan", edad=30, documento="123456789", diagnostico="Gripe")


doctor1 = Doctor(nombre="Dr. Luis", edad=45, documento="987654321", especialidad="Medicina General")


print(f"Paciente: {paciente1.nombre}, Diagnóstico: {paciente1.ver_diagnostico()}")
print(f"Doctor: {doctor1.nombre}, Especialidad: {doctor1.ver_especialidad()}")

# Agregar historial al paciente
paciente1.agregar_historial("Consulta inicial: Fiebre y tos.")
paciente1.agregar_historial("Recetado paracetamol.")

# Ver historial
print("Historial del paciente:", paciente1.ver_historial())

# Doctor modifica el diagnóstico
doctor1.modificar_diagnostico(paciente1, "Bronquitis")

# Ver nuevo diagnóstico
print("Nuevo diagnóstico del paciente:", paciente1.ver_diagnostico())
