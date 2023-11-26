from money import Money


def test_get_change():
    assert Money({}).get_change(100, [2]) == [1]
    assert Money({}).get_change(400, [5]) == [1]

def test_change_coins():
    assert Money({}).check_coins(3) is False
    assert Money({}).check_coins(2) is True

def test_value_for_coins():
    assert Money({}).value_for_coins([2]) == 200
    assert Money({}).value_for_coins([5]) == 500

def test_format_value():
    assert Money({}).format_value(150) == "1.50 zł"
    assert Money({}).format_value(300) == "3.0 zł"
