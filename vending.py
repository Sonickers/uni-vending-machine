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
            print(f"Items price is: {item.price}")
        else:
            print("Wrong product code. Please try again.")

    def check_item_code(self, code):
        return code in self.items

    def get_item(self, code):
        return self.items.get(code)

    def service_mode(self):
        print("\nAvailable options:\n"
              + "111 - restock product\n"
              + "222 - edit product\n"
              + "333 - update spring cycle\n"
              + "999 - Exit service mode\n")
        service_code = input("Choice: ")

        if service_code == "111":
            print("Restocking...")
        elif service_code == "222":
            print("Editing")
        elif service_code == "333":
            print("Spring cycles...")
        elif service_code == "999":
            print("Exiting the service mode...")
        else:
            print("\nWrong code. Try again.\n")
            self.service_mode()

    def restock_product(self):
        pass
