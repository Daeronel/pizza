from random import randint
from typing import Callable

import click

from pizza import BasePizza, Margherita, Hawaiian, Pepperoni

MENU = {'Margherita': Margherita(), 'Hawaiian': Hawaiian(), 'Pepperoni': Pepperoni()}


def log(text: str):
    """Выводит время выполнения действия:
    генерируется рандомно"""

    def wrapper(func: Callable):
        def decorated(*args, **kwargs):
            print(text.format(randint(5, 15)))
            return func(*args, **kwargs)

        return decorated

    return wrapper


@log('🍳 Приготовили за {} с!')
def bake(pizza: BasePizza) -> None:
    """Готовит пиццу"""
    return None


@log('🚗 Доставили за {} с!')
def deliver(pizza: BasePizza) -> None:
    """Доставляет пиццу"""
    return None


@log('🏠 Забрали за {} с!')
def pickup(pizza: BasePizza) -> None:
    """Самовывоз"""
    return None


@click.group()
def cli() -> None:
    """Инициализация интерфейса"""
    return None


@cli.command()
@click.option(
    '--size',
    type=click.Choice(list(BasePizza.SIZE), case_sensitive=False),
    prompt='Выберите размер пиццы',
    help=f'Доступные размеры: {", ".join(list(BasePizza.SIZE))}')
@click.option(
    '--delivery',
    prompt='Доставка?',
    default=False,
    is_flag=True,
    help='Укажите, если нужна доставка')
@click.argument('pizza', nargs=1)
def order(pizza: str, size: str, delivery: bool) -> None:
    """Готовит и доставляет пиццу"""
    pizza = pizza.capitalize()
    if pizza not in [pizza_subclass.__name__ for pizza_subclass in BasePizza.__subclasses__()]:
        print(f'К сожалению, у нас нет пиццы {pizza} \n' \
              'Посмотреть доступные пиццы можно в разделе menu')
        return None
    print(f'Заказ: пицца {pizza} {size}')
    pizza_to_cook = MENU[pizza]
    bake(pizza_to_cook)
    if delivery:
        deliver(pizza_to_cook)
    else:
        pickup(pizza_to_cook)
    return None


@cli.command()
def menu():
    """Выводит меню"""
    for pizza_subclass in BasePizza.__subclasses__():
        print(f'- {pizza_subclass()}: {", ".join(list(pizza_subclass().dict()))}')


if __name__ == '__main__':
    cli()
