from item import Item

# TODO: delete these commented out values later
# coins = {"5": 10, "2": 10, "1": 10, "50": 20}
# items = {
#     "A1": Item("Coke", 350, 10),
#     "A2": Item("Water", 150, 10),
#     "A3": Item("Sprite", 350, 10),
#     "A4": Item("Fanta", 350, 10),
#     "B1": Item("Coconaut", 450, 10),
#     "B2": Item("Yogurt", 300, 10),
#     "B3": Item("Iced Coffee", 500, 10),
#     "B4": Item("Milk", 250, 10),
# }

def parse_data_file(file_lines):
    """Reads given `file_lines` line by line in a for loop
    - each line starting with 's' is a spring
    - each line starting with 'i' is an item
    - each line starting with 'm' is a coin for the money class

    Args:
        file_lines (list[str]): lines read from data file

    Returns:
        tuple[dict, dict, dict]: tuple with dicts of: coins, items and springs
    """

    # TODO: parse each line and build out the return values
    coins = {}
    items = {}
    springs = {}

    return (coins, items, springs)
