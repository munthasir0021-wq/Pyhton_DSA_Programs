from enum import member


class book:
    def __init__(self,book_id,title):
        self.book_id = book_id
        self.title = title
        self.available = True

class mamber:
    def __init__(self,member_id,name):
        self.member_id = member_id
        self.name = name

class library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self,book):
        self.books.append(book)
        print(f"Book '{book.title}' added")

    def register_member(self,member):
        self.members.append(member)
        print(f"Member '{member.name}' registered")

    def issue_book(self,book_id,member):
        for book in self.books:
            if  book.book_id == book_id:
                if book.available:
                    book.available = False
                    print(f"Book '{book.title}' issued to member '{member.name}'")
                else:
                    print("book is not available")
                return
        print("book not found")

    def return_book(self,book_id):
        for book in self.books:
            if book.book_id == book_id:
                book.available = True
                print(f"Book '{book.title}' returned")
                return

library = library()
book1 = book(1,"Python Programming")
member1 = member(1,"sai")

library.add_book(book1)
library.register_member(member1)
library.issue_book(101,member1)
library.return_book(101)


    