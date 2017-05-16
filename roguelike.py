import os
import sys
import tty
import termios
import csv
import inventory
import items
from termcolor import colored, cprint


def board_into_csv(board):
    '''Writes the board into a csv file'''
    with open("stage_1.csv", "w") as f:
        w = csv.writer(f, delimiter=' ')
        for item in board:
            w.writerow(item)


def csv_into_board():
    '''Opens a board from csv file'''
    board = []
    with open("stage_2.csv", newline='') as f:
        r = csv.reader(f)
        for row in f:
            row = row.strip()
            row = list(row)
            board.append(row)
    return board


def print_board(board):
    '''Prints the given board'''
    board_list = board
    for item in board_list:
        for element in item:
            if element == "#":
                cprint(element, 'white', 'on_white', end='')
            if element == '-':
                cprint(element, 'grey', 'on_grey', end='')
            if element == "@":
                cprint(element, 'grey', 'on_white', end='')
            if element == "O":
                cprint(element, 'magenta', 'on_magenta', end='')
            if element == "^":
                cprint(element, 'grey', 'on_grey', end='')
            if element == "]":
                cprint(element, 'green', 'on_green', end='')
            if element == "|":
                cprint(element, 'red', 'on_red', end='')
            if element == "*":
                cprint(element, 'yellow', 'on_yellow', end='')
            if element == ">":
                cprint(element, 'blue', 'on_blue', end='')
            if element == "<":
                cprint(element, 'magenta', 'on_magenta', end='')
            if element == "/":
                cprint(element, 'cyan', 'on_cyan', end='')
        print("")


def insert_player(board, x, y):
    '''Inserts a player on a given
        position into the board'''
    x = int(x)
    y = int(y)
    karakan = "@"
    board[y][x] = karakan
    return board


def char_stats(char_class, inventory):
    '''Returns a dictionary of charaters stats'''
    char_stats = {}
    char_class = char_class - 1
    # list of tuples with each classes stats
    character_list = [(8, 4, 8, 1), (12, 4, 4, 1), (4, 8, 8, 1)]
    char_stats['ATK'] = character_list[char_class][0]
    char_stats['DEF'] = character_list[char_class][1]
    char_stats['HP'] = character_list[char_class][2]
    char_stats['LVL'] = character_list[char_class][3]
    if "DildoMocy" in inventory:
        char_stats['ATK'] += 2
    if "TarczaWiksy" in inventory:
        char_stats['DEF'] += 3
    if "CzapkaWpierdolu" in inventory:
        char_stats['HP'] += 1
    return char_stats


def character_info(set_char_stats):
    '''Prints characters stats in a neat way'''
    for stat, value in sorted(set_char_stats.items()):
        print(stat + " " + str(value) + "  ")


def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def main():

    x = 4
    y = 19

    char_class = 3
    # int(input("""Choose your character class:
    # 1) Warrior - 8 ATK, 4 DEF, 8 HP
    # 2) Assassin - 12 ATK, 4 DEF, 4 HP
    # 3) Knight - 4 ATK, 8 DEF, 8 HP
    # """))

    board = csv_into_board()

    board = insert_player(board, x, y)

    print_board(board)

    inv = inventory.create_inventory()

    set_char_stats = char_stats(char_class, inv)

    while True:

        move = getch()

        if move == "a":
            x = int(x)
            y = int(y)
            if board[y][x - 1] == "*":
                board = insert_player(board, x - 1, y)
                board[y][x] = '*'
                os.system('clear')
                print_board(board)
                x = x - 1
            elif board[y][x - 1] == "O":
                open_chest = items.encounter_item()
                items.loot_item(board, open_chest, x-1, y)
                loot = items.generate_item(open_chest)
                inventory.add_to_inventory(inv, loot)
                set_char_stats = char_stats(char_class, inv)
        elif move == "d":
            x = int(x)
            y = int(y)
            if board[y][x + 1] == "*":
                board = insert_player(board, x+1, y)
                board[y][x] = "*"
                os.system('clear')
                print_board(board)
                x = x + 1
            elif board[y][x + 1] == "O":
                open_chest = items.encounter_item()
                items.loot_item(board, open_chest, x+1, y)
                loot = items.generate_item(open_chest)
                inventory.add_to_inventory(inv, loot)
                set_char_stats = char_stats(char_class, inv)
        elif move == "w":
            x = int(x)
            y = int(y)
            if board[y - 1][x] == "*":
                board = insert_player(board, x, y-1)
                board[y][x] = "*"
                os.system('clear')
                print_board(board)
                y = y - 1
            elif board[y - 1][x] == "O":
                open_chest = items.encounter_item()
                items.loot_item(board, open_chest, x, y-1)
                loot = items.generate_item(open_chest)
                inventory.add_to_inventory(inv, loot)
                set_char_stats = char_stats(char_class, inv)
        elif move == "s":
            x = int(x)
            y = int(y)
            if board[y + 1][x] == "*":
                board = insert_player(board, x, y+1)
                board[y][x] = "*"
                os.system('clear')
                print_board(board)
                y = y + 1
            elif board[y + 1][x] == "O":
                open_chest = items.encounter_item()
                items.loot_item(board, open_chest, x, y+1)
                loot = items.generate_item(open_chest)
                inventory.add_to_inventory(inv, loot)
                set_char_stats = char_stats(char_class, inv)
        elif move == "i":
            inventory.print_inventory_table(inv)
        elif move == "c":
            character_info(set_char_stats)
        elif move == "q":
            sys.exit()


if __name__ == '__main__':
    main()
