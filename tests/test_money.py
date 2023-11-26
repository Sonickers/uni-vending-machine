import pytest
from money import Money

@pytest.mark.parametrize('coins,expected', [(3, False), (2, True)])
def test_change_coins (coins, expected):
    assert Money({}).check_coins(coins) is expected

@pytest.mark.parametrize('price,input_coins,change', [(150, 300, 150), (200, 250, 50)])
def test_get_change(price, input_coins, change):
    assert Money({}).get_change(price, input_coins) == change

# @pytest.mark.parametrize('', [])
# def test_value_for_coins():
#     assert Money({}).value_for_coins([2]) == 200
#     assert Money({}).value_for_coins([5]) == 500

# @pytest.mark.parametrize('', [])
# def test_format_value():
#     assert Money({}).format_value(150) == "1.50 zł"
#     assert Money({}).format_value(300) == "3.0 zł"
#     assert Money({}).format_value(600) == "6.0 zł"
