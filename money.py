import math

class Money:
    def __init__(self, stocked) -> None:
        self.stocked = stocked

    def get_change(self):
        money = 1
        sums = money * 2
        return sums

    def value_for_coins(self, coins):
        return sum(coin if coin > 5 else coin * 100 for coin in coins)

    def format(self, value):
        if value < 100:
            return f"{value} gr"

        gr = value % 100
        zl = math.floor(value / 100)
        return f"{zl}.{gr} zł"
