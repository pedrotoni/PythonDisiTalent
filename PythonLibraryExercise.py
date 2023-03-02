class Book:
    """This book class represents a book with a title, an author,
    a ISBN code, a price, a number of pages and a publisher.

    Parameters:
    title: string
    author: string
    isbn: string
    price: float
    pages: int
    publisher: string"""
    def __init__(self, title, author, isbn, price, pages, publisher):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.price = price
        self.pages = pages
        self.publisher = publisher

    def get_info(self):
        "This get_info method returns a string containing the listed info about the book object."
        return (f"Title: {self.title}" \
                f"\nAuthor: {self.author}" \
                f"\nISBN: {self.isbn}" \
                f"\nPrice: {self.price}" \
                f"\nPages: {self.pages}" \
                f"\nPublisher: {self.publisher}"
                f"\n--------------------")


class Library:
    """This class represents a library and receives the following parameters
    when instantiating the object:
    name: string
    address: string

    P.S: the self.books = [] in the __init__ constructor
    is initially an empty list that the methods of the Library class use,
    so you don't have to worry about that when instantiating the Library class."""
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.books = []

    def add_book(self, book):
        """the add_book methods receives a book object in the parameter
        and appends it to the empty list I mentioned in the Library class docstring.
        Besides that, shows us a message containing the title and the author of the book we added."""
        self.books.append(book)
        print(f'{book.title} by {book.author} has been added to our Library.')
        print('--------------------')

    def checkout(self, book):
        """the checkout methods receives a book object in the parameters as well,
        but removes it from the booklist, and shows us a message containing the
        title and author of the book we removed.
        If we try to delete a book that is not in our list, we get an ValueError."""
        if book in self.books:
            self.books.remove(book)
            print(f'{book.title} by {book.author} has been deleted of our library.')
            print('--------------------')
        else:
            raise ValueError(f"Cannot delete {book.title} by {book.author} because we don't have it in our library.")

    def search(self, isbn):
        """This search method receives a string parameter of the ISBN code of the book.
        If the ISBN code passed as a parameter is equal to the ISBN of one of the books in our list,
        it returns us the book. If we don't have a book in the list with the same ISBN code
        passed as parameter, it returns us 'None'."""
        for book in self.books:
            if isbn == book.isbn:
                return book
        return None

    def get_catalog(self):
        """this get_catalog takes an empty list representing a booklist.
        If this booklist is empty, it means our library catalog is empty as well.
        If the booklist is not empty, it iterates through the books in our
        self.books list and appends each book info to our initial booklist, and then
        it returns the booklist in the end of the execution"""
        booklist = []
        if len(self.books) == 0:
            print("The library catalog is empty right now.")
        else:
            print("Library Catalog: ")
            for book in self.books:
                booklist.append(book.get_info())
            return booklist

    def stock_worth(self):
        """The stock_worth method has a initial variable called sumBookPrices that
        initiates at zero. Then it iterates through our self.books list and sum each book price
        to our initial variable sumBookPrices, which is returned at the end of the execution."""
        sumBookPrices = 0
        print("Sum of all book prices in library: ")
        for book in self.books:
            sumBookPrices += book.price
        return sumBookPrices


# Creating Book Objects
book1 = Book("Book 1", "Armando Gomes", "AUU", 30.00, 500, "AAA")
book2 = Book("Book 2", "Julia Prado", "BAA", 50.00, 400, "BBB")
book3 = Book("Book 3", "Paulo Sanches", "BOO", 41.30, 300, "CCC")
book4 = Book("Book 4", "Timo Domingues", "IIB", 48.50, 200, "DDD")
book5 = Book("Book 5", "Carla Faria", "QLL", 13.30, 100, "EEE")

# Creating Library Object
lib = Library("Library 1", "Library Street, 101")

# Adding Books to Library with add_book method
lib.add_book(book1)
lib.add_book(book2)
lib.add_book(book3)
lib.add_book(book4)

# Removing books of Library with checkout method
# OBS: trying to delete unregistered book will throw a ValueError
# I'll leave the checkout with unregistered book as comment so it won't break the program.
lib.checkout(book1)
#lib.checkout(book5)

# Searching a book through an ISBN parameter in search method
# Searching an unregistered ISBN will show an error message.
searchedBook = lib.search("IIB")

if searchedBook is not None:
    print(f'Search Result:'
          f'\n{searchedBook.get_info()}')
else:
    print(f"We couldn't find a book with this ISBN.")

# get_catalog method
lib_catalog = lib.get_catalog()

for book in lib_catalog:
    print(book)

# stock_worth method
print(lib.stock_worth())






