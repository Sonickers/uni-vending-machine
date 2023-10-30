from item import Item
from vending import VendingMachine
from money import Money

coins = {
    "5": 10,
    "2": 10,
    "1": 10,
    "50": 20
}
money = Money(coins)

items = {
    "A1": Item("Coke", 350, 10),
    "A2": Item("Water", 150, 10),
    "A3": Item("Sprite", 350, 10),
    "A4": Item("Fanta", 350, 10),
    "B1": Item("Coconaut", 450, 10),
    "B2": Item("Yogurt", 300, 10),
    "B3": Item("Iced Coffee", 500, 10),
    "B4": Item("Milk", 250, 10),
}

vending_machine = VendingMachine(items, money)
vending_machine.start_app()
