class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def set_dimensions(self, new_length, new_width):
        if new_length <= 0 or new_width <= 0:
            raise ValueError("El largo y ancho no pueden ser menores o iguales a 0")
        self.__length = new_length
        self.__width = new_width

    def get_area(self):
        return self.__length * self.__width

    def get_perimeter(self):
        return 2 * (self.__length + self.__width)

    def get_dimensions(self):
        return self.__length, self.__width


rectangle = Rectangle(10, 5)
print(rectangle.get_dimensions())
print(rectangle.get_area())
print(rectangle.get_perimeter())

rectangle.set_dimensions(8, 4)
print(rectangle.get_dimensions())
