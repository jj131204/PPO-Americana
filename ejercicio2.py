class Products():
    def __init__(self, name, price, stock):
        
        self.name = name
        self.price = price
        self.stock = stock
    def verifyStock(self, numberProducts):
        if(numberProducts <= self.stock):
            print(f"Hay stock suficiente del producto: {self.name}")
            
        else:
            print("No hay stock suficiente")
    
    def sellProduct(self, numberProducts):
        actualStock = int(self.stock)
        number = int(numberProducts)

        if(actualStock >= number):
            newStock = actualStock - number
            
            self.stock = newStock
            print(f"Producto vendido correctamente")
            print(f"Nuevo stock del producto {self.name}: {self.stock}")
        else:
            print("No hay stock suficiente")

    def updateStock(self, newStock):
        self.stock = newStock
        print(f"El nuevo stock del producto {self.name} es: {self.stock}")


laptop = Products("Laptop", "1200", "5")

laptop.verifyStock('3')
laptop.sellProduct("5")
laptop.updateStock('100')
