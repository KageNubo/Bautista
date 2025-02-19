class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

    def describe(self):
        print(f"Book: '{self.title}' by {self.author}, Published in {self.year_published}")


book1 = Book("48 Laws of Power", "Robert Greene", 2000)
book2 = Book("Noli me Tangere", "Jose Rizal", 1887)
book3 = Book("El filibusterismo", "Jose Rizal", 1891)


book1.describe()
book2.describe()
book3.describe()
