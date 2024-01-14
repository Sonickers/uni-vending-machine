import math


class Money:
    def __init__(self, stocked) -> None:
        self.stocked = stocked

    def check_coins(self, coin):
        if type(coin) is list:
            return all(self.check_coins(c) for c in coin)
        return coin in [5, 2, 1, 50]

    def get_change(self, price, input_coins):
        input_value = self.value_for_coins(input_coins)
        change = input_value - price
        cash_change = []

        for coin in input_coins:
            self.stocked[coin] += 1

        while change > 0:
            if change >= 500 and self.stocked[5] > 0:
                change = change - 500
                cash_change.append(5)
                self.stocked[5] -= 1
            elif change >= 200 and self.stocked[2] > 0:
                change = change - 200
                cash_change.append(2)
                self.stocked[2] -= 1
            elif change >= 100 and self.stocked[1] > 0:
                change = change - 100
                cash_change.append(1)
                self.stocked[1] -= 1
            elif change >= 50 and self.stocked[50] > 0:
                change = change - 50
                cash_change.append(50)
                self.stocked[50] -= 1
            else:
                # not enough coins for change
                return None

        return cash_change

    def value_for_coins(self, coins):
        if not self.check_coins(coins):
            raise ValueError("Invalid input")
        return sum(coin if coin > 5 else coin * 100 for coin in coins)

    def format_value(self, value):
        if value < 100:
            return f"{value} gr"

        gr = value % 100
        zl = math.floor(value / 100)
        return f"{zl}.{gr} zł"

    def add_coin(self, coin, amount):
        self.stocked[coin] += amount

    def get_stocked(self):
        return self.stocked
