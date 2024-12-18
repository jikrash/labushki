"""
Модуль с тремя абстрактными классами, описывающими книги
"""


class Book:
    """
    Абстрактный класс, описывающий книгу
    """

    def __init__(self, title: str, author: str):
        if not isinstance(title, str) or not title:
            raise ValueError("Название книги должно быть непустой строкой.")
        if not isinstance(author, str) or not author:
            raise ValueError("Автор книги должен быть непустой строкой.")
        self.title = title
        self.author = author

    def get_title(self) -> str:
        """Возвращает название книги

        >>> book = Book("Война и мир", "Лев Толстой")
        >>> book.get_title()
        'Война и мир'
        """
        return self.title

    def get_author(self) -> str:
        """Возвращает автора книги

        >>> book = Book("Война и мир", "Лев Толстой")
        >>> book.get_author()
        'Лев Толстой'
        """
        return self.author


class Novel(Book):
    """
    Абстрактный класс, описывающий роман
    """

    def __init__(self, title: str, author: str, genre: str):
        super().__init__(title, author)
        if not isinstance(genre, str) or not genre:
            raise ValueError("Жанр романа должен быть непустой строкой.")
        self.genre = genre

    def get_genre(self) -> str:
        """Возвращает жанр романа

        >>> novel = Novel("Преступление и наказание", "Фёдор Достоевский", "психологический роман")
        >>> novel.get_genre()
        'психологический роман'
        """
        return self.genre

    def read_chapter(self, chapter_num: int) -> str:
        """Возвращает текст указанной главы (без реализации)

        >>> novel = Novel("Преступление и наказание", "Фёдор Достоевский", "психологический роман")
        >>> novel.read_chapter(1) #doctest: +ELLIPSIS
        ...
        """
        ...


class Textbook(Book):
    """
    Абстрактный класс, описывающий учебник
    """

    def __init__(self, title: str, author: str, subject: str):
        super().__init__(title, author)
        if not isinstance(subject, str) or not subject:
            raise ValueError("Предмет учебника должен быть непустой строкой.")
        self.subject = subject

    def get_subject(self) -> str:
        """Возвращает предмет учебника

        >>> textbook = Textbook("Алгебра", "А.Н. Колмогоров", "Математика")
        >>> textbook.get_subject()
        'Математика'
        """
        return self.subject

    def solve_exercise(self, exercise_num: int) -> str:
        """Возвращает решение указанного упражнения (реализация отсутствует)

        >>> textbook = Textbook("Алгебра", "А.Н. Колмогоров", "Математика")
        >>> textbook.solve_exercise(1) #doctest: +ELLIPSIS
        ...
        """
        ...


if __name__ == "__main__":
    import doctest

    doctest.testmod()