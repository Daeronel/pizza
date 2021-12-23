from typing import Union, Dict


class EmojiMixin:
    emoji = {'Margherita': '🍅', 'Pepperoni': '🍕', 'Hawaiian': '🍍'}

    def __str__(self):
        text = super().__str__()
        return f'{text} {self.emoji[text]}'


class BasePizza:
    """Базовый класс для создания пицц.
    Параметры: словарь с базовыми ингридиентами и порциями
    и размер пиццы.

    Также содержит метод dict, который выводит рецепт пиццы.
    Масса ингридиента зависит от класса.
    """

    SIZE = {'L': 1,
            'XL': 1.5}

    def __init__(self, size: str = 'L') -> None:
        if size not in self.SIZE.keys():
            raise ValueError(f'Укажите один их доступных размеров: {list(self.SIZE)}')
        self._size = size
        ingredients = {'tomato sauce': int(100 * self.SIZE[self._size]),
                       'mozzarella': int(200 * self.SIZE[self._size])}
        self._ingredients = ingredients

    def dict(self) -> Dict[str, int]:
        """Рецепт и размер пиццы
        """
        return self._ingredients

    def __eq__(self, other) -> bool:
        """Сравнение пицц"""
        if isinstance(other, BasePizza):
            return self._ingredients == other._ingredients
        else:
            raise TypeError("Можно сравнить только с пиццей!")

    def __str__(self):
        return self.__class__.__name__


class Margherita(EmojiMixin, BasePizza):
    """Класс для пиццы Маргарита.
    Добавляем к базовому ингридиент tomatoes
    """

    def __init__(self, *args, **kwargs) -> None:
        super(Margherita, self).__init__(*args, **kwargs)
        self._ingredients['tomatoes'] = int(250 * self.SIZE[self._size])


class Pepperoni(EmojiMixin, BasePizza):
    """Класс для пиццы Пепперони.
    Добавляем к базовому ингридиент pepperoni
    """

    def __init__(self, *args, **kwargs) -> None:
        super(Pepperoni, self).__init__(*args, **kwargs)
        self._ingredients['pepperoni'] = int(250 * self.SIZE[self._size])


class Hawaiian(EmojiMixin, BasePizza):
    """Класс для пиццы Гавайская.
    Добавляем к базовому ингридиент pineapples
    """

    def __init__(self, *args, **kwargs) -> None:
        super(Hawaiian, self).__init__(*args, **kwargs)
        self._ingredients['pineapples'] = int(250 * self.SIZE[self._size])
        self._ingredients['chicken'] = int(250 * self.SIZE[self._size])


if __name__ == '__main__':
    pizza_l = Pepperoni(size='L')
    pizza_xl = Pepperoni()
    print(pizza_l.dict())
    print(pizza_xl._size)
    print(pizza_xl == pizza_l)
    print(", ".join(list(BasePizza.SIZE)))
    for pizza_subclass in BasePizza.__subclasses__():
        print(f'- {pizza_subclass()}: {", ".join(list(pizza_subclass().dict()))}')
