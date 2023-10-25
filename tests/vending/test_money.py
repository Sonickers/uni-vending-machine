from vending.money import Money

def test_get_change():
    assert Money({}).get_change() == 2
