class CarteraCripto:
    def __init__(self, usuario):
        self.__usuario = usuario
        self.__saldo_btc = 0.0

    def consultar_saldo(self):
        return self.__saldo_btc

    def comprar_btc(self, monto_usd, precio_actual_btc):
        if monto_usd <= 0 or precio_actual_btc <= 0:
            raise ValueError("El monto en USD y el precio del BTC deben ser positivos.")
        btc_comprados = monto_usd / precio_actual_btc
        self.__saldo_btc += btc_comprados
        print(f"Compra exitosa: adquiriste {btc_comprados:.8f} BTC.")

    def vender_btc(self, monto_btc, precio_actual_btc):
        if monto_btc <= 0 or precio_actual_btc <= 0:
            raise ValueError("El monto de BTC y el precio del BTC deben ser positivos.")
        if monto_btc > self.__saldo_btc:
            raise ValueError("No puedes vender más BTC de los que tienes.")
        self.__saldo_btc -= monto_btc
        monto_usd = monto_btc * precio_actual_btc
        print(f"Venta exitosa: recibiste ${monto_usd:.2f} USD.")
        return monto_usd
    

cartera = CarteraCripto(usuario="usuario123")


cartera.comprar_btc(monto_usd=1000, precio_actual_btc=20000)


print(f"Saldo después de compra: {cartera.consultar_saldo()} BTC")

