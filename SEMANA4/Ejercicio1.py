class Product:
    def __init__(self, name, price):
        
        self.__name = name
        self.__price = price

    def set_price(self, newPrice):
        if newPrice <= 0:
            raise ValueError("El nuevo precio debe ser mayor que cero.")
        self.__price = newPrice

    def get_price(self):
        return self.__price

    def get_name(self) -> str:
        return self.__name

    def set_discount(self, porcentaje):
        if not (0 <= porcentaje <= 100):
            raise ValueError("El porcentaje de descuento debe estar entre 0 y 100.")
        self.__price -= self.__price * (porcentaje / 100)


product = Product("Laptop", 1500)
print(product.get_name())
print(product.get_price())

product.set_price(1200)
print(product.get_price())

product.set_discount(10)
print(product.get_price()) 
