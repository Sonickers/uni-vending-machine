class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def is_cold(self):
        return False

    def subtract_item(self):
        self.quantity = self.quantity - 1

class Drink(Item):
    pass

class Snack(Item):
    def __init__(self, name, price, quantity, cold):
        super().__init__(name, price, quantity)
        self.cold = cold

    def is_cold(self):
        return self.cold
