class Circulo:
    pi = 3.1416

    @classmethod
    def area(cls, radius):
        return cls.pi * (radius ** 2)
    

print(Circulo.area(10))