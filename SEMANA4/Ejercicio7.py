class TarjetaCredito:
    def __init__(self, numero):
        self.__numero = numero

    @staticmethod
    def validar_tarjeta(numero):
        numero = str(numero)[::-1]
        suma = 0
        for i, digito in enumerate(numero):
            n = int(digito)
            if i % 2 == 1:
                n *= 2
                if n > 9:
                    n -= 9
            suma += n
        return suma % 10 == 0


# Ejemplo de uso
tarjeta = TarjetaCredito("4532015112830366")
print(TarjetaCredito.validar_tarjeta("4532015112830366"))  # True
