class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}")


if __name__ == '__main__':
    b1 = Book("Python Programming", "someone", 200)
    b2 = Book("Java Programming", "Someone2", 300)
    b1.display_info()
    b2.display_info()

