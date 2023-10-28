class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def is_cold(self):
        return False

class Drink(Item):
    pass

class Snack(Item):
    def __init__(self, name, price, quantity, cold):
        super().__init__(name, price, quantity)
        self.cold = cold

    def is_cold(self):
        return self.cold

# def use_item(item: Item):
#     print(f"using {item.name} it is {'cold' if item.is_cold() else 'warm'}")

# ice_cream = Snack("Ice Cream", "5zl", 20, True)
# use_item(ice_cream)
