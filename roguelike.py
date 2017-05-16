import os
import sys
import tty
import termios
import getch
import csv
import inventory
import items
import menu
from termcolor import colored, cprint


def csv_into_board(filename):
    '''Opens a board from csv file'''
    board = []
    with open(filename, newline='') as f:
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
            if element.isalpha() or element.isdigit():
                cprint(element, end='')
            if element == " ":
                cprint(element, end='')
            if element == "#":
                cprint(element, 'white', 'on_white', end='')
            if element == '-':
                cprint(element, 'grey', 'on_grey', end='')
            if element == "@":
                cprint(element, 'grey', 'on_white', end='')
            if element == "o":
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


def main():

    char_class = menu.menu()

    x = 4
    y = 17

    board = csv_into_board("stage_1.csv")

    board = insert_player(board, x, y)

    print_board(board)

    inv = inventory.create_inventory()

    set_char_stats = char_stats(char_class, inv)

    while True:

        move = getch.getch()

        if move == "a":
            x = int(x)
            y = int(y)
            if board[y][x - 1] == "*":
                board = insert_player(board, x - 1, y)
                board[y][x] = '*'
                os.system('clear')
                print_board(board)
                x = x - 1
            elif board[y][x - 1] == "o":
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
            elif board[y][x + 1] == "o":
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
            elif board[y - 1][x] == "o":
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
            elif board[y + 1][x] == "o":
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
