from data import parse_data_file
from vending import VendingMachine
from money import Money


# Load data and run the app!
with open("app_data.txt", encoding="utf-8") as f:
    app_data_lines = f.readlines()

coins, items, springs = parse_data_file(app_data_lines)

money = Money(coins)
vending_machine = VendingMachine(items, money, springs)

vending_machine.start_app()
