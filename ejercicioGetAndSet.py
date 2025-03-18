class CuentaBancaria():
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
        result = self.__ajustar_saldo(cantidad)

        if result:
            self.__saldo -= cantidad
            return self.__saldo

    def  __ajustar_saldo(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            return True 
        raise ValueError("Debe ser un valor negativo y no puede superar el valor acutal de tu cuenta")

cuenta1 = CuentaBancaria(200000, "Juan")
cuenta2 = CuentaBancaria(300000, "Maria")

cuenta1.set_retirar(100)

print(cuenta1.get_saldo())