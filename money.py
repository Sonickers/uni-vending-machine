import math

class Money:
    def __init__(self, stocked) -> None:
        self.stocked = stocked

    def check_coins(self, coin):
        return coin in [5, 2, 1, 50]

    def get_change(self, price, input_coins):
        input_value = self.value_for_coins(input_coins)
        change = input_value - price
        cash_change = []

        while change > 0:
            if change >= 500:
                change = change - 500
                cash_change.append(5)
            elif change >= 200:
                change = change - 200
                cash_change.append(2)
            elif change >= 100:
                change = change - 100
                cash_change.append(1)
            elif change >= 50:
                change = change - 50
                cash_change.append(50)
            else:
                break

        return cash_change

    def value_for_coins(self, coins):
        return sum(coin if coin > 5 else coin * 100 for coin in coins)

    def format_value(self, value):
        if value < 100:
            return f"{value} gr"

        gr = value % 100
        zl = math.floor(value / 100)
        return f"{zl}.{gr} zł"
