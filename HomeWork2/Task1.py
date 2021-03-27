first_book_name = "The Knight in the Panther's Skin"
first_book_authot = "Shota Rustaveli"
first_book_year = "XII century"
first_book_pages = "222"
second_book_name = "The Right Hand of the Grand Master"
second_book_author = "Konstantine Gamsakhurdia"
second_book_year = "1939"
second_book_pages = "397"
third_book_name = "Antonio and David"
third_book_author = "Jemal Karchkhadze"
third_book_year = "1987"
third_book_pages = "134"

class Book:
    def __init__(self, name, author, year, pages):
        self.name = name
        self.author = author
        self.year = year
        self.pages = pages
    def info(self):
        return f"Name - {self.name} , Author - {self.author}, Year - {self.year}, Pages - {self.pages}"

print("1) The Knight in the Panther's Skin \n2) The Right Hand of the Grand Master \n3) Antonio and David")
user_input = int(input("Choose book: "))

if user_input == 1:
    b = Book(first_book_name, first_book_authot, first_book_year, first_book_pages)
    print(b.info())
elif user_input == 2:
    b = Book(second_book_name, second_book_author, second_book_year, second_book_pages)
    print(b.info())

elif user_input == 3:
    b = Book(third_book_name, third_book_author, third_book_year, third_book_pages)
    print(b.info())
else:
    print("Book didn't find")