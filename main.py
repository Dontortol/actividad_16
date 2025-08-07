class Book:
    def __init__(self, title, author, date):
        self.title = title
        self.author = author
        self.date = date

    def info(self):
        print(f"El titulo del libro es: {self.title}, del autor: {self.author}, Publicado en el año: {self.date}")

books = []
def add_book():
    print("--Ingresar libros--")
    name = input("Ingrese el nombre del libro: ").lower()
    autor = input("Ingrese el nombre del autor: ").capitalize()
    while True:
        try:
            date = int(input("Ingrese el año de publicacion del libro: "))
            break
        except ValueError:
            print("Debe ser un valor entero ")
        except Exception as e:
            print("Hubo un error inesperado ", e)
    boo = Book(name, autor, date)
    books.append(boo)

def print_books():
    if not books:
        print("No hay libros")
    else:
        print("--Libros Registrados--")
        i = 1
        for book in books:
            print(f"Libro {i}.", end = "")
            book.info()
            i += 1
        print()

def delete_books():
    if not books:
        print("No hay libros")
    else:
        search = input("Ingrese el nombre del libro que quiera eliminar: ").lower()
        for boo in books:
            if boo.title == search:
                books.remove(boo)
                print("Libro eliminado exitosamente")
                break

while True:
    print("--Bienvenido al menu de la biblioteca\n"
          "1. Agregar libro\n"
          "2. Mostrar libros registrados\n"
          "3. Eliminar libro\n"
          "4. Salir")
    select = input("Ingrese la opcion deseada: ")
    match select:
        case "1":
            add_book()
        case "2":
            print_books()
        case "3":
            delete_books()
        case "4":
            print("Saliendo del sistema")
            break
        case _:
            print("No se puede introducir esa opcion")
