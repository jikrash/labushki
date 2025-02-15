
"""
реализуем наследование для музыкальных инструментов.
базовый класс - музыкальный инструмент, а дочерние классы - гитара и фортепиано.
"""


class MusicalInstrument:
    """
    базовый класс для музыкальных инструментов.
    """

    def __init__(self, name: str, type: str, material: str) -> None:
        """
        конструктор класса musicalinstrument.

        args:
            name: название инструмента.
            type: тип инструмента (например, струнный, клавишный, духовой).
            material: материал, из которого сделан инструмент.
        """
        self.name = name
        self.type = type
        self.material = material
        self._is_tuned = False  # приватный атрибут, показывающий, настроен ли инструмент. инкапсуляция нужна, чтобы напрямую не менять состояние настройки инструмента, а использовать метод tune().

    def __str__(self) -> str:
        """
        возвращает строковое представление объекта musicalinstrument.
        """
        return f"{self.name} ({self.type}) из {self.material}"

    def __repr__(self) -> str:
        """
        возвращает строковое представление объекта musicalinstrument для отладки.
        """
        return f"MusicalInstrument(name='{self.name}', type='{self.type}', material='{self.material}')"

    def play_sound(self) -> str:
        """
        имитирует звук инструмента.
        """
        if self._is_tuned:
            return "звук инструмента (настроенного)"
        else:
            return "нестройный звук инструмента"

    def tune(self) -> None:
        """
        настраивает инструмент.
        """
        self._is_tuned = True
        print(f"{self.name} настроен.")


class Guitar(MusicalInstrument):
    """
    класс, представляющий гитару, наследник класса musicalinstrument.
    """

    def __init__(self, name: str, material: str, number_of_strings: int) -> None:
        """
        конструктор класса guitar. расширяет конструктор базового класса, добавляя атрибут number_of_strings.

        args:
            name: название гитары.
            material: материал, из которого сделана гитара.
            number_of_strings: количество струн.
        """
        super().__init__(name, "струнный", material)
        self.number_of_strings = number_of_strings

    def __str__(self) -> str:
        """
        возвращает строковое представление объекта guitar. перегружает метод __str__ базового класса, чтобы добавить информацию о количестве струн.
        """
        return f"{super().__str__()} с {self.number_of_strings} струнами"

    def __repr__(self) -> str:
        """
        возвращает строковое представление объекта guitar для отладки. перегружает метод __repr__ базового класса, чтобы добавить информацию о количестве струн.
        """
        return f"Guitar(name='{self.name}', material='{self.material}', number_of_strings={self.number_of_strings})"

    def play_sound(self) -> str:
        """
        имитирует звук гитары. перегружает метод play_sound базового класса, чтобы вернуть специфичный для гитары звук.
        причина перегрузки: у каждого инструмента свой звук.
        """
        if self._is_tuned:
            return "перебор струн гитары (настроенной)"
        else:
            return "дребезжание струн гитары (не настроенной)"

    def strum(self) -> str:
        """
        играет перебором по струнам гитары.
        """
        return "перебор струн"


class Piano(MusicalInstrument):
    """
    класс, представляющий фортепиано, наследник класса musicalinstrument.
    """

    def __init__(self, name: str, material: str, number_of_keys: int) -> None:
        """
        конструктор класса piano. расширяет конструктор базового класса, добавляя атрибут number_of_keys.

        args:
            name: название фортепиано.
            material: материал, из которого сделано фортепиано.
            number_of_keys: количество клавиш.
        """
        super().__init__(name, "клавишный", material)
        self.number_of_keys = number_of_keys

    def __str__(self) -> str:
        """
        возвращает строковое представление объекта piano. перегружает метод __str__ базового класса, чтобы добавить информацию о количестве клавиш.
        """
        return f"{super().__str__()} с {self.number_of_keys} клавишами"

    def __repr__(self) -> str:
        """
        возвращает строковое представление объекта piano для отладки. перегружает метод __repr__ базового класса, чтобы добавить информацию о количестве клавиш.
        """
        return f"Piano(name='{self.name}', material='{self.material}', number_of_keys={self.number_of_keys})"

    def play_sound(self) -> str:
        """
        имитирует звук фортепиано. перегружает метод play_sound базового класса, чтобы вернуть специфичный для фортепиано звук.
        причина перегрузки: у каждого инструмента свой звук.
        """
        if self._is_tuned:
            return "звуки клавиш фортепиано (настроенного)"
        else:
            return "фальшивые звуки клавиш фортепиано (не настроенного)"

    def press_key(self, key_number: int) -> str:
        """
        нажимает на клавишу фортепиано.
        """
        if 1 <= key_number <= self.number_of_keys:
            return f"нажата клавиша номер {key_number}"
        else:
            return "неверный номер клавиши"


if __name__ == "__main__":
    # создаем объекты классов
    instrument = MusicalInstrument("скрипка", "струнный", "дерево")
    guitar = Guitar("fender stratocaster", "ольха", 6)
    piano = Piano("yamaha grand", "клен", 88)

    # выводим информацию об инструментах
    print(instrument)
    print(repr(instrument))
    print(guitar)
    print(repr(guitar))
    print(piano)
    print(repr(piano))

    # играем на инструментах (пока не настроены)
    print(instrument.play_sound())
    print(guitar.play_sound())
    print(piano.play_sound())

    # настраиваем гитару и фортепиано
    guitar.tune()
    piano.tune()

    # играем на инструментах (после настройки)
    print(instrument.play_sound())
    print(guitar.play_sound())
    print(piano.play_sound())

    # используем специфичные методы для гитары и фортепиано
    print(guitar.strum())
    print(piano.press_key(42))
