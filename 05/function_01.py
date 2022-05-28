def my_books(books):
    x = print(input('Napisz tytuł książki ->'))
    y = print(input('Napisz jej ocenę w skali od 0 do 10 ->'))
    books.append((x, y))
books = []
my_books(books)

print(books)
