from data import update_data_file
from item import Snack, Drink


class VendingMachine:
    def __init__(self, items, money, springs):
        self.items = items
        self.money = money
        self.springs = springs

    def vend(self, code, cash):
        print(code, cash)

    def start_app(self):
        code = input("Select product code: ").lower()
        if code == "000":
            print("Starting service mode...")
            self.service_mode()
            return

        if self.check_item_code(code):
            item = self.get_item(code)

            if item.quantity == 0 or self.springs[code] == 0:
                print("Sorry, this item is out of stock or unable to buy.")
                return

            print(f"Items price is: {self.money.format_value(item.price)}")
            coins_change = self.money.get_change(item.price, self.intake_money(item))

            if coins_change is None:
                print(
                    "Sorry, can't proceed due to lack of change. Try again with other coins."
                )
                return

            print("Returning the change: ", coins_change)
            item.quantity -= 1
            self.springs[code] -= 1
            self.update_data_file()
        else:
            print("Wrong product code. Please try again.")

    def check_item_code(self, code):
        return code in self.items

    def get_item(self, code):
        return self.items.get(code)

    def service_mode(self):
        print(
            "\nAvailable options:\n"
            + "111 - Restock item\n"
            + "222 - Restock cash\n"
            + "333 - Change item price\n"
            + "444 - Update springs\n"
            + "555 - Update item\n"
            + "999 - Exit service mode\n"
        )
        service_code = input("Choice: ")

        if service_code == "111":
            self.service_restock_item()
        elif service_code == "222":
            self.service_restock_cash()
        elif service_code == "333":
            self.service_edit_item()
        elif service_code == "444":
            self.service_springs()
        elif service_code == "555":
            self.service_update_item()
        elif service_code == "999":
            print("Exiting the service mode...")
        else:
            print("\nWrong code. Try again.\n")
            self.service_mode()
        self.update_data_file()

    def intake_money(self, item):
        user_coins = []
        coins_value = 0

        while coins_value < item.price:
            print("We only accept 5[zl], 2[zl], 1[zl] and 50[gr].")
            coin = int(input("Add coin: "))

            if self.money.check_coins(coin):
                user_coins.append(coin)
                coins_value = self.money.value_for_coins(user_coins)
                remaining = max([item.price - coins_value, 0])
                print(
                    f"You've inserted {self.money.format_value(coins_value)}."
                    f" Remaining amount: {self.money.format_value(remaining)}"
                )

        return user_coins

    def service_springs(self):
        spring_code = input("Choose which spring cycle you want to update: ")
        self.springs[spring_code.lower()] = 10
        print("Springs are updated to 10.")

    def service_restock_cash(self):
        nominal = int(input("What nominal you want to restock?"))

        if not self.money.check_coins(nominal):
            print("Invalid coin.")
            return

        restock_amount = int(input("How many coins do you want to add?"))
        self.money.add_coin(nominal, restock_amount)

    def service_restock_item(self):
        item_code = input("Restocking item. Select item you want to restock: ").lower()
        if not self.check_item_code(item_code):
            print("Wrong item code")
            return

        item = self.get_item(item_code)
        restock_quantity = input(
            f"This item quantity is: {item.quantity}. How many do you want to add? "
        )
        item.quantity += int(restock_quantity)
        print("Item quantity is updated.")

    def service_edit_item(self):
        item_code = input(
            "Change item price. Select item you want to change price for: "
        ).lower()
        if not self.check_item_code(item_code):
            print("Wrong item code")
            return

        item = self.get_item(item_code)
        edit_price = input(
            f"This item price is: {item.price}. What price do you want to set for this item? "
        )
        item.price = int(edit_price)
        print("Item price is updated.")

    def service_update_item(self):
        item_code = input("Update item. Select item you want to update: ").lower()
        if not self.check_item_code(item_code):
            print("Wrong item code")
            return

        item = self.get_item(item_code)
        print(f"Current item: {item.name} {item.price}.")

        snack_or_drink = (
            input("Is the new item a Snack or a Drink? [s/d] ").lower().strip()[0]
        )

        new_name = input("New name: ")
        new_price = input("New price: ")

        new_item = (
            Snack(new_name, new_price, item.quantity, item.is_cold())
            if snack_or_drink == "s"
            else Drink(new_name, new_price, item.quantity)
        )

        self.items[item_code] = new_item
        print("Item is updated.")

    def update_data_file(self):
        update_data_file(self.springs, self.items, self.money.get_stocked())
