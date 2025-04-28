class Empleado:
    def __init__(self, nombre, rol, clave_acceso):
        self.__nombre = nombre
        self.__rol = rol
        self.__clave_acceso = self.__cifrar_clave(clave_acceso)

    @property
    def nombre(self):
        return self.__nombre

    @property
    def rol(self):
        return self.__rol

    def __cifrar_clave(self, clave):
        return clave[::-1]

    def __descifrar_clave(self):
        return self.__clave_acceso[::-1]

    def verificar_clave(self, clave_ingresada):
        return self.__clave_acceso == self.__cifrar_clave(clave_ingresada)

    def cambiar_clave(self, clave_antigua, nueva_clave):
        if self.verificar_clave(clave_antigua):
            self.__clave_acceso = self.__cifrar_clave(nueva_clave)
            print("Clave cambiada exitosamente.")
        else:
            raise ValueError("La clave antigua no es correcta.")

# Crear un empleado
emp = Empleado(nombre="Laura Gómez", rol="Administrador", clave_acceso="clave123")

print(f"Empleado: {emp.nombre}, Rol: {emp.rol}")


if emp.verificar_clave("clave123"):
    print("Acceso permitido.")
else:
    print("Acceso denegado.")

emp.cambiar_clave("clave123", "nuevaClave456")

if emp.verificar_clave("nuevaClave456"):
    print("Acceso permitido con nueva clave.")
else:
    print("Acceso denegado con nueva clave.")

