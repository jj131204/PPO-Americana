class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.__titular = titular
        self.__saldo = saldo
    
    def depositar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a depositar debe ser mayor que cero.")
        self.__saldo += cantidad

    def retirar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a retirar debe ser mayor que cero.")
        if cantidad > self.__saldo:
            raise ValueError("Fondos insuficientes.")
        self.__saldo -= cantidad

    def consultar_saldo(self):
        return self.__saldo

    def consultar_titular(self):
        return self.__titular


class CuentaAhorro(CuentaBancaria):
    def __init__(self, titular, saldo=0, interes_anual=0):
        super().__init__(titular, saldo)
        if interes_anual < 0:
            raise ValueError("El porcentaje de interés no puede ser negativo.")
        self.__interes_anual = interes_anual

    def aplicar_interes(self):
        saldo_actual = self.consultar_saldo()
        interes = saldo_actual * (self.__interes_anual / 100)
        self.depositar(interes)

    def consultar_interes(self):
        return self.__interes_anual


# Ejemplo de uso
cuenta = CuentaAhorro("Juan Pérez", 1000, 5)
print(cuenta.consultar_saldo())
cuenta.aplicar_interes()
print(cuenta.consultar_saldo())
