class Estudiante:
    def __init__(self, nombre, codigo):
        self.__nombre = None
        self.__codigo = None
        self.nombre = nombre
        self.codigo = codigo
        self.__notas = []

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor.strip():
            raise ValueError("El nombre no puede estar vacío.")
        self.__nombre = valor

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, valor):
        if not valor.isalnum():
            raise ValueError("El código debe ser alfanumérico.")
        self.__codigo = valor

    def agregar_nota(self, nota):
        if 0.0 <= nota <= 5.0:
            self.__notas.append(nota)
        else:
            raise ValueError("La nota debe estar entre 0.0 y 5.0.")

    def calcular_promedio(self):
        if not self.__notas:
            return 0.0
        return sum(self.__notas) / len(self.__notas)

    def es_aprobado(self):
        return self.calcular_promedio() >= 3.0
    
# Primero, creamos un estudiante
est = Estudiante(nombre="Juan Pérez", codigo="ABC123")

# Agregamos algunas notas válidas
est.agregar_nota(4.5)
est.agregar_nota(3.2)
est.agregar_nota(2.8)


# Calculamos el promedio
promedio = est.calcular_promedio()
print(f"Promedio de {est.nombre} ({est.codigo}): {promedio:.2f}")

# Verificamos si el estudiante está aprobado
if est.es_aprobado():
    print(f"{est.nombre} está aprobado.")
else:
    print(f"{est.nombre} no está aprobado.")
