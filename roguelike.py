import os
import sys
import tty
import termios
import getch
import csv
import inventory
import items
import combatbase
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
            if element == "†":
                cprint(element, 'red', 'on_white', end='')
            if element == "#":
                cprint(element, 'white', 'on_white', end='')
            if element == '-':
                cprint(element, 'grey', 'on_grey', end='')
            if element == "@":
                cprint(element, 'white', 'on_yellow', end='')
            if element == ".":
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


def char_stats(char_class, inventory, wound_count):
    '''Returns a dictionary of characters stats'''
    char_stats_dict = {}
    char_class = char_class - 1
    # list of tuples with each classes stats
    character_list = [(8, 4, 8, 1), (12, 4, 4, 1), (4, 8, 8, 1)]
    char_stats_dict['ATK'] = character_list[char_class][0]
    char_stats_dict['DEF'] = character_list[char_class][1]
    char_stats_dict['HP'] = character_list[char_class][2]
    char_stats_dict['LVL'] = character_list[char_class][3]
    if "DildoMocy" in inventory:
        char_stats_dict['ATK'] += 2
    if "TarczaWiksy" in inventory:
        char_stats_dict['DEF'] += 3
    if "CzapkaWpierdolu" in inventory:
        char_stats_dict['HP'] += 1
    char_stats_dict['HP'] -= wound_count
    return char_stats_dict


def encounter(char_stats):

    wound_count = 0

    if char_stats['ATK'] >= 7:
        question, answer = combatbase.easymode()
        print(question)
        attac = input("Give me your answer!: ")

        while True:

            if attac == answer:
                print("NON NOBIS DOMINE! You may pass.")
                break

            elif attac != answer:
                print("You're mine now!")

                if char_stats['DEF'] >= 7:
                    wound_count += 1
                else:
                    wound_count += 2

                    if wound_count < char_stats['HP']:
                        attac = input("Try again, mortal, before I end you. ")
                    else:
                        game_over()
    else:
        question, answer = combatbase.hardmode()
        print(question)
        attac = input("Give me your answer! Be quick about it, MORTAL!: ")
        while True:
            if attac == answer:
                print("You slimy little peasant! NON NOBIS DOMINE! DEUS VULT!")
                break
            elif attac != answer:
                print("You're mine now!")
                if char_stats['DEF'] >= 7:
                    wound_count += 1
                else:
                    wound_count += 2
                    if wound_count < char_stats['HP']:
                        attac = input("Try again, mortal, before I end you. ")
                    else:
                        game_over()
    return wound_count


def character_info(set_char_stats):
    '''Prints characters stats in a neat way'''
    for stat, value in sorted(set_char_stats.items()):
        print(stat + " " + str(value) + "  ")


def stage_swtich(current_stage):
    '''Switches the stage if player is in the right position'''
    filenames = ["stage_2.csv", "stage_3.csv", "stage_4.csv", "boss.csv"]
    if current_stage == "stage_1.csv":
        filename = filenames[0]
        x = 4
        y = 19
    if current_stage == "stage_2.csv":
        filename = filenames[1]
        x = 2
        y = 12
    if current_stage == "stage_3.csv":
        filename = filenames[2]
        x = 4
        y = 14
    if current_stage == "stage_4.csv":
        filename = filenames[-1]
    return filename, x, y


def main():

    char_class = menu.menu()

    if char_class:
        filename = "stage_1.csv"
        x = 2
        y = 16

    board = csv_into_board(filename)

    board = insert_player(board, x, y)

    print_board(board)

    inv = inventory.create_inventory()

    set_char_stats = char_stats(char_class, inv, wound_count=0)

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
            elif board[y][x - 1] == ".":
                open_chest = items.encounter_item()
                items.loot_item(board, open_chest, x-1, y)
                loot = items.generate_item(open_chest)
                inventory.add_to_inventory(inv, loot)
                set_char_stats = char_stats(char_class, inv, wound_count=0)
            elif board[y][x - 1] == "†":
                wound_count = encounter(set_char_stats)
                combatbase.delete_cunt(board, x-1, y)
                set_char_stats = char_stats(char_class, inv, wound_count)
        elif move == "d":
            x = int(x)
            y = int(y)
            if board[y][x + 1] == "*":
                board = insert_player(board, x + 1, y)
                board[y][x] = "*"
                os.system('clear')
                print_board(board)
                x = x + 1
            elif board[y][x + 1] == ".":
                open_chest = items.encounter_item()
                items.loot_item(board, open_chest, x + 1, y)
                loot = items.generate_item(open_chest)
                inventory.add_to_inventory(inv, loot)
                set_char_stats = char_stats(char_class, inv, wound_count=0)
            elif board[y][x + 1] == "†":
                wound_count = encounter(set_char_stats)
                board[y][x + 1] = "*"
                set_char_stats = char_stats(char_class, inv, wound_count)
        elif move == "w":
            x = int(x)
            y = int(y)
            if board[y - 1][x] == "*":
                board = insert_player(board, x, y - 1)
                board[y][x] = "*"
                os.system('clear')
                print_board(board)
                y = y - 1
            elif board[y - 1][x] == ".":
                open_chest = items.encounter_item()
                items.loot_item(board, open_chest, x, y - 1)
                loot = items.generate_item(open_chest)
                inventory.add_to_inventory(inv, loot)
                set_char_stats = char_stats(char_class, inv, wound_count=0)
            elif board[y - 1][x] == "†":
                wound_count = encounter(set_char_stats)
                combatbase.delete_cunt(board, x, y - 1)
                set_char_stats = char_stats(char_class, inv, wound_count)
        elif move == "s":
            x = int(x)
            y = int(y)
            if board[y + 1][x] == "*":
                board = insert_player(board, x, y+1)
                board[y][x] = "*"
                os.system('clear')
                print_board(board)
                y = y + 1
            elif board[y + 1][x] == ".":
                open_chest = items.encounter_item()
                items.loot_item(board, open_chest, x, y+1)
                loot = items.generate_item(open_chest)
                inventory.add_to_inventory(inv, loot)
                set_char_stats = char_stats(char_class, inv, wound_count=0)
            elif board[y + 1][x] == "†":
                wound_count = encounter(set_char_stats)
                combatbase.delete_cunt(board, x, y + 1)
                set_char_stats = char_stats(char_class, inv, wound_count)
        elif move == "i":
            inventory.print_inventory_table(inv)
        elif move == "c":
            character_info(set_char_stats)
        elif move == "q":
            sys.exit()

        if x > 47 and y < 6 and filename == "stage_1.csv":
            filename, x, y = stage_swtich(filename)
            board = csv_into_board(filename)
        if x >= 57 and filename == "stage_2.csv":
            filename, x, y = stage_swtich(filename)
            board = csv_into_board(filename)
        if x == 24 and y == 12 and filename == "stage_3.csv":
            filename, x, y = stage_swtich(filename)
            board = csv_into_board(filename)


if __name__ == '__main__':
    main()
