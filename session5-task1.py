class Library:
    def __init__(self):
        self.books=[]
    def add_new_book(self,book):
        if  book not in self.books:
            print(f"Added {book}")
            self.books.append(book)
            return True
        else:
            print(f'This book already exists')
            return False
    def check_out(self,book):
        if  book not in self.books or not self.books[self.books.index(book)].available:
            print("This book isn't available")
            return False
        else:
            self.books[self.books.index(book)].available = False
            print(f'Rented {book}')
            return True
    def check_in(self,book):
        if  book not in self.books or self.books[self.books.index(book)].available:
            print("This book isn't rented")
            return False
        else:
            self.books[self.books.index(book)].available = True
            print(f'Returned {book}')
            return True
        
class Book:
    def __init__(self,title,author,isbn,available=True):
        self.title=title
        self.author=author
        self.__isbn = isbn
        self.available = available
    def get_isbn(self):
        return self.__isbn
    def set_isbn(self,new_val):
        self.__isbn = new_val
    def __str__(self):
        return f"{self.title}#{self.get_isbn()}"
    def display_info(self):
        print(f"ISBN: {self.get_isbn()}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Available: {self.available}")
        
class Member:
    def __init__(self,name,membership_id,borrowed_books=[]):
        self.name=name
        self.__membership_id=membership_id
        self.borrowed_books = borrowed_books
    def get_membership_id(self):
        return self.__membership_id
    def set_membership_id(self,new_val):
        self.__membership_id = new_val
    def borrow_book(self,book,lib):
        if lib.check_out(book):
            self.borrowed_books.append(book)
    def return_book(self,book,lib):
        if lib.check_in(book):
            self.borrowed_books.remove(book)
            
class StaffMember(Member):
    def __init__(self,name,membership_id,staff_id,borrowed_books=[]):
        super().__init__(name,membership_id,borrowed_books)
        self.staff_id = staff_id
    def add_book(self,book,lib):
        lib.add_new_book(book)
        
book1 = Book("1984", "George Orwell", "1234567890")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "0987654321")
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", "1122334455")

lib = Library()

member1 = Member("Alice", "M001")

lib.add_new_book(book1)
lib.add_new_book(book2)
lib.add_new_book(book3)

member1.borrow_book(book1, lib)

member1.borrow_book(book1, lib)

member1.return_book(book1, lib)

member1.return_book(book1, lib)

member1.borrow_book(book1, lib)

book1.display_info()
book2.display_info()
book3.display_info()