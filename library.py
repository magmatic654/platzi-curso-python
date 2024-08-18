class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.aviable = True

    def borrow(self):
        if self.aviable: 
            self.aviable = False
            print(f"El libro {self.title} ha sido prestado")
        else:
            print(f"El libro {self.title} no está disponible")

    def return_book(self):
        self.aviable = True
        print(f"El libro {self.title} ha sido devuelto")

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.aviable:
            book.borrow()
            self.borrowed_books.append(book)
        else:
            print(f"El libro {book.title} No está disponible")
    
    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            print(f"El libro {book.title} No está en la lista de prestados")

    def show_borrow_books(self):
        if len(self.borrowed_books) == 0:
            print("No cuentas con libros prestados")
        else:
            print(f"Libros disponibles para {self.name}:")
            for book in self.borrowed_books:
                print(f"{book.title} por {book.author}")
                

class library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)
        print(f"El libro {book.title} ha sido agregado")

    def register_user(self, user):
        self.users.append(user)
        print(f"El usuario {user.name} ha sido registrado")

    def show_aviable_books(self):
        print("Libros disponibles:")
        for book in self.books:
            if book.aviable:
                print(f"{book.title} por {book.author}")

#Crear los libros
book1 = Book("El gato con botas", "Charles Perrault")
book2 = Book("The hunger games", "Suzanne Collins")

#Crear usuario
user1 = User("Harold", "001")

#Crear biblioteca
library = library()
library.add_book(book1)
library.add_book(book2)
library.register_user(user1)

#Realizar prestamo
user1.borrow_book(book1)

#Mostrar libros
library.show_aviable_books()

#Devolver libro
user1.return_book(book1)

#Mostrar libros
library.show_aviable_books()

#Realizar prestamo
user1.borrow_book(book2)
user1.borrow_book(book1)

#Mostrar libros prestados en usuario
user1.show_borrow_books()