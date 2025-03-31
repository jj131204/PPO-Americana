class Book:
    def __init__(self, title, author, total_pages):
        if total_pages <= 0:
            raise ValueError("El número total de páginas debe ser mayor que cero.")
        self.__title = title
        self.__author = author
        self.__total_pages = total_pages
        self.__current_page = 1

    def advance_pages(self, pages):
        if pages <= 0:
            raise ValueError("El número de páginas a avanzar debe ser mayor que cero.")
        if self.__current_page + pages > self.__total_pages:
            raise ValueError("No se puede avanzar más allá del número total de páginas.")
        self.__current_page += pages

    def go_back_pages(self, pages):
        if pages <= 0:
            raise ValueError("El número de páginas a retroceder debe ser mayor que cero.")
        if self.__current_page - pages < 1:
            raise ValueError("No se puede retroceder más allá de la página 1.")
        self.__current_page -= pages

    def get_current_page(self):
        return self.__current_page

    def get_book_info(self):
        return f"Título: {self.__title}, Autor: {self.__author}, Páginas Totales: {self.__total_pages}, Página Actual: {self.__current_page}"


book = Book("1984", "George Orwell", 328)
print(book.get_book_info()) 

book.advance_pages(50)
print(book.get_current_page()) 

book.go_back_pages(10)
print(book.get_current_page())
