disk_size = 1.44 * 1024 * 1024
pages = 100
lines_page = 50
chars_line = 25
bytes_char = 4


book_size = pages * lines_page * chars_line * bytes_char

books_on_disk = disk_size // book_size

print("Количество книг, помещающихся на дискету:", int(books_on_disk))
