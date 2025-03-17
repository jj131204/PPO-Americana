class Test():
    def __init__(self):
        
        self.publico = "Soy publico"
        self._protegido = "Soy protegido"
        self.__privado = "Soy privado"

    def mostrar(self):
        return f"{self.publico} {self._protegido} {self.__privado}"


ejemplo = Test()

print(ejemplo.mostrar())

print(ejemplo.publico)
print(ejemplo._protegido)

print(ejemplo._Test__privado)
