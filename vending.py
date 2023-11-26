class VendingMachine:
    def __init__(self, items, money):
        self.items = items
        self.money = money

    def vend(self, code, cash):
        print(code, cash)

    def start_app(self):
        code = input("Select product code: ")
        if code == "000":
            print("Starting service mode...")
            self.service_mode()
            return

        if self.check_item_code(code):
            item = self.get_item(code)
            print(f"Items price is: {self.money.format_value(item.price)}")
            coins_change = self.money.get_change(item.price, self.intake_money(item))
            print("Returning the change: ", coins_change)
        else:
            print("Wrong product code. Please try again.")

    def check_item_code(self, code):
        return code in self.items

    def get_item(self, code):
        return self.items.get(code)

    def service_mode(self):
        print("\nAvailable options:\n"
              + "111 - Restock product\n"
              + "222 - Edit product\n"
              + "333 - Update spring cycle\n"
              + "999 - Exit service mode\n")
        service_code = input("Choice: ")

        if service_code == "111":
            print("Restocking product. Select product you want to restock: ")
        elif service_code == "222":
            print("Editing product. Select product you want to edit: ")
        elif service_code == "333":
            print("Choose which spring cycle you want to update: ")
        elif service_code == "999":
            print("Exiting the service mode...")
        else:
            print("\nWrong code. Try again.\n")
            self.service_mode()

    def intake_money(self, item):
        user_coins = []
        coins_value = 0

        while coins_value < item.price:
            print("We only accept 5[zl], 2[zl], 1[zl] and 50[gr].")
            coin = int(input("Add coin: "))

            if self.money.check_coins(coin):
                user_coins.append(coin)
                coins_value = self.money.value_for_coins(user_coins)
                print(f"You've inserted {self.money.format_value(coins_value)}." \
                    f" Items price is: {self.money.format_value(item.price)}")

        return user_coins
