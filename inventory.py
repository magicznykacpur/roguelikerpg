import csv


def create_inventory(filename="inventory.csv"):
    '''Createas a inventory dictionary from a given csv file'''
    inv = {}
    with open(filename, "r") as f:
        r = csv.reader(f)
        for item in f:
            item = item.split(',')
            inv[item[0]] = int(item[1])
    return inv


def import_inventory(inventory, filename):
    '''Imports loot from a csv file and adds it to current inventory'''
    with open(filename, "r") as f:
        r = csv.reader(f, delimiter=' ')
        for item in f:
            added_items = item.split(',')

    added_items[-1] = added_items[-1].rstrip('\n')

    for item in added_items:
        if item in inventory:
            inventory[item] = inventory[item] + 1
        else:
            inventory[item] = 1

    return inventory


def export_inventory(inventory, filename="inventory.csv"):
    '''Exports the inventory to a csv file'''
    with open(filename, "w") as f:
        w = csv.writer(f)
        for key, value in inventory.items():
            w.writerow((key, value))


def display_inventory(inventory):
    '''Displays all items in inventory'''
    keys = []
    values = []
    for key, value in inventory.items():
        keys.append(key)
        values.append(value)

    return keys, values


def add_to_inventory(inventory, added_items):
    '''Using given item list updates existing inventory'''
    capacity = 0
    for key, value in inventory.items():
        capacity += 1
    if capacity < 5:
        for item in added_items:
            if item in inventory:
                inventory[item] = inventory[item] + 1
            else:
                inventory[item] = 1
    else:
        print("You'r inventory is full.")
    return inventory


def print_inventory_table(inventory):
    '''Prints out a formatted table of inventory items'''
    if not inventory:
        print("Your inventory is empty right now")
    else:
        table = "-"
        space = " "
        keys, values = display_inventory(inventory)
        tup_list = []
        for key, value in inventory.items():
            tup_list.append((key, value))
        longest_key = max(keys, key=len)
        longest_key = len(longest_key)
        longest_value = max(values)
        longest_value = len(str(longest_value))

        print("\nInventory:\n")
        print("  " + "count" + "  " + "item name")
        print(table * (longest_value + 5) + table * (longest_key + 4))

        tup_list = sorted(tup_list, key=lambda value: value[1], reverse=True)
        for i in range(len(tup_list)):
            if len(str(tup_list[i][1])) >= 2:
                print(space * 3 + str(tup_list[i][1]) + space * 4 + str(tup_list[i][0]))
            else:
                print(space * 4 + str(tup_list[i][1]) + space * 4 + str(tup_list[i][0]))

        print(table * (longest_value + 5) + table * (longest_key + 4))
        print("Space left in inventory: " + str(5 - sum(values)))
