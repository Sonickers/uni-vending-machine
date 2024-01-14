import pytest
from money import Money

test_stocked = {1: 10, 2: 10, 5: 10, 50: 15}


@pytest.mark.parametrize("coins,expected", [(3, False), (2, True)])
def test_change_coins(coins, expected):
    assert Money(test_stocked).check_coins(coins) is expected


@pytest.mark.parametrize(
    "price,input_coins,change", [(150, [1, 2], [1, 50]), (250, [2, 2], [1, 50])]
)
def test_get_change(price, input_coins, change):
    assert Money(test_stocked).get_change(price, input_coins) == change


@pytest.mark.parametrize("coins, expected", [([2], 200)])
def test_value_for_coins(coins, expected):
    assert Money(test_stocked).value_for_coins(coins) is expected


@pytest.mark.parametrize(
    "money, expected", [(150, "1.50 zł"), (300, "3.0 zł"), (600, "6.0 zł")]
)
def test_format_value(money, expected):
    assert Money(test_stocked).format_value(money) == expected


def test_not_enough_change():
    assert Money({1: 1, 2: 5, 5: 0, 50: 0}).get_change(350, [5]) is None


def test_enough_change_with_input():
    assert Money({1: 0, 2: 5, 5: 0, 50: 0}).get_change(550, [1, 50, 50, 2, 2]) == [50]
