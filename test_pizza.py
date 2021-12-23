import pytest

from pizza import *


@pytest.mark.parametrize(
    'pizza_type, name',
    [
        (Margherita, 'Margherita'),
        (Pepperoni, 'Pepperoni'),
        (Hawaiian, 'Hawaiian'),
    ],
)
def test_pizza_size(pizza_type, name: str):
    assert str(pizza_type.__name__) == name
    assert pizza_type()._size == 'L'
    assert pizza_type(size='XL')._size == 'XL'


def test_wrong_size():
    with pytest.raises(ValueError):
        pizza = Pepperoni(size='S')


def test_wrong_equal():
    with pytest.raises(TypeError):
        assert Margherita() != 'Margherita'


def test_equality():
    assert Pepperoni() == Pepperoni()
    assert Margherita() != Hawaiian()
    assert Margherita(size="L") != Margherita(size="XL")


def test_ingredients():
    ingredients = {'tomato sauce': 100,
                   'mozzarella': 200,
                   'tomatoes': 250}
    assert Margherita()._ingredients == ingredients
