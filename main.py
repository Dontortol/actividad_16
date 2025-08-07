class Book:
    def __init__(self, title, author, date):
        self.title = title
        self.author = author
        self.date = date

    def info(self):
        print(f"El titulo del libro es: {self.title}, del autor: {self.author}, Publicado en el año: {self.date}")

books = []
def add_book():
    if not books:
        print("No hay libros")
    else:

