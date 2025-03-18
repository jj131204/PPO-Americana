class cuentaBancaria():
    def __init__(self, saldo, titular):
        
        self.__saldo = saldo
        self.__titular = titular

    def get_saldo(self):
        return self.__saldo
    
    def get_titular(self):
        return self.__titular
    
    def set_depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            return self.__saldo
        else:
            raise ValueError("Debe ser un valor positivo")
    
    def set_retirar(self, cantidad):
        saldoAnterio = self.__saldo
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"Retiro realizado con exito")
            print(f"Saldo anterior = {saldoAnterio} -  Nuevo saldo {self.__saldo}")
            return self.__saldo
        raise ValueError("Debe ser un valor negativo y no puede superar el valor acutal de tu cuenta")


cuenta1 = cuentaBancaria(200000, "Juan")
cuenta2 = cuentaBancaria(300000, "Maria")

print(cuenta1.get_titular())
print(cuenta1.get_saldo())
print(cuenta2.get_titular())
print(cuenta2.get_saldo())

cuenta1.set_depositar(100000)
cuenta2.set_depositar(100000)

print(cuenta1.get_titular())
print(cuenta1.get_saldo())
print(cuenta2.get_titular())
print(cuenta2.get_saldo())

cuenta1.set_retirar(100000)
cuenta2.set_retirar(100000)

print(cuenta1.get_titular())
print(cuenta1.get_saldo())
print(cuenta2.get_titular())
print(cuenta2.get_saldo())
