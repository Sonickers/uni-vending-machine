from item import Item
from vending import VendingMachine
from money import Money

stocked_money = {
    "10g": 10,
    "20g": 10,
    "50g": 10,
    "1zl": 10,
    "2zl": 10,
    "5zl": 5,
}
money = Money(stocked_money)

items = {
    "A1": Item("Coke", 340, 10),
    "A2": Item("Water", 150, 10),
    "A3": Item("Sprite", 350, 10),
    "A4": Item("Fanta", 320, 10),
    "B1": Item("Coconaut", 420, 10),
    "B2": Item("Yogurt", 320, 10),
    "B3": Item("Iced Coffee", 500, 10),
    "B4": Item("Milk", 220, 10),
}

vending_machine = VendingMachine(items, money)
vending_machine.start_app()
