from item import Drink, Snack

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

    springs = {}
    items = {}
    coins = {}

    for line in file_lines:
        if line.strip() == "":
            continue
        row = line.strip().split(", ")

        if row[0] == 's':
            springs[row[1]] = row[2]
        elif row[0] == 'i':
            if row[1] == 'd':
                items[row[2]] = Drink(row[3], int(row[4]), int(row[5]))
            else:
                items[row[2]] = Snack(row[3], int(row[4]), int(row[5]), row[6] == '1')
        elif row[0] == 'm':
            coins[int(row[1])] = int(row[2])

    return (coins, items, springs)

def update_data_file(springs, items, coins):
    with open('app_data.txt', 'w', encoding="utf-8") as f:
        for k, v in springs:
            f.write(f"s, {k}, {v}")

        for k, v in items:
            f.write(f"i, d, {k}, {v.name}, {v.price}, {v.quantity}")
            # zapisz items w formie i, d, a1, coca-cola, 500, 10

        for k, v in coins.items():
            f.write(f"m, {k}, {v}")
