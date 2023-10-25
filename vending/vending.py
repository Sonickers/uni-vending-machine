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
            return

        if self.check_item_code(code):
            item = self.get_item(code)
            print("Items price is: ", item.price)
        else:
            print("Wrong product code. Please try again.")

    def check_item_code(self, code):
        return code in self.items

    def get_item(self, code):
        return self.items.get(code)
