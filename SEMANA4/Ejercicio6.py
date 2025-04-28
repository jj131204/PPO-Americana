class Empleado:
    contador_empleados = 0

    def __init__(self, nombre, salario):
        self.__nombre = nombre
        self.__salario = salario
        Empleado.contador_empleados += 1

    def consultar_nombre(self):
        return self.__nombre

    def consultar_salario(self):
        return self.__salario

    @classmethod
    def cantidad_empleados(cls):
        return cls.contador_empleados


empleado1 = Empleado("Ana Pérez", 3000)
empleado2 = Empleado("Carlos Gómez", 3500)

print(Empleado.cantidad_empleados())
