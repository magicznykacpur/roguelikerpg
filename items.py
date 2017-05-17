import random


def encounter_item():
    '''Function responsible for chest encountering behaviour'''

    print("To je skrzynka. Otwierasz?\n")

    open_chest = input("(y/n): ")
    while open_chest.isdigit() or open_chest in ["", " "]:

        open_chest = input("Wkilkaj y albo n. ")
    if open_chest == "y":
        print("\nDodane do rukzaku")
    if open_chest == "n":
        print("Fuck you then.")

    return open_chest


def loot_item(board, open_chest, x, y):
    '''Function responsible for clearing a chest after looting'''
    if open_chest == "y":
        board[y][x] = "*"
    else:
        pass


def generate_item(open_chest):
    '''Creates an item in current inventory dictionary'''
    added_items = []
    if open_chest == "y":
        loot = ["DildoMocy", "TarczaWiksy", "CzapkaWpierdolu"]
        added_items.append(random.choice(loot))
    else:
        pass
    return added_items
