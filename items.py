import random


def encounter_item():
    '''Function responsible for chest encountering behaviour'''

    print("It's a chest. Do yo u want to open it?\n")

    open_chest = input("(y/n): ")
    while open_chest.isdigit() or open_chest in ["", " "]:
        open_chest = input("Try entering y or n. ")

    if open_chest == "y":
        print("\nItem added to inventory")
    if open_chest == "n":
        print("Alright boi.")

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
        loot = ["DildoMocy", "TarczaWiksy", "CzapkaWpierdolu", "OnuceZapierdalania", "RekawiceTrzepania"]
        added_items.append(random.choice(loot))
    else:
        pass
    return added_items
