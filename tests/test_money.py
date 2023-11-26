import pytest
from money import Money

@pytest.mark.parametrize('coins,expected', [(3, False), (2, True)])
def test_change_coins(coins, expected):
    assert Money({}).check_coins(coins) is expected

@pytest.mark.parametrize('price,input_coins,change', [(150, [1, 2], [1, 50]), (250, [2, 2], [1, 50])])
def test_get_change(price, input_coins, change):
    assert Money({}).get_change(price, input_coins) == change

@pytest.mark.parametrize('coins, expected', [([2], 200)])
def test_value_for_coins(coins, expected):
    assert Money({}).value_for_coins(coins) is expected

@pytest.mark.parametrize('money, expected', [(150, "1.50 zł"), (300, "3.0 zł"), (600, "6.0 zł")])
def test_format_value(money, expected):
    assert Money({}).format_value(money) == expected
