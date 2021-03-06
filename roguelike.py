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
import moving
import player_stats
import stages
import halloffame
import time
from termcolor import colored, cprint


def count_game_time(start, stop, character_info):
    '''Counts the game time, and returns it in a dictionary'''
    time_count = stop - start
    time_count = int(time_count) / 60

    return time_count, character_info


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


def main():

    char_class = menu.menu()

    x, y, filename, stage_name = menu.start_game(char_class)

    board = csv_into_board(filename)

    board = insert_player(board, x, y)

    print_board(board)

    inv = inventory.create_inventory()

    set_char_stats = player_stats.char_stats(char_class, inv, wound_count=0)

    timer_start = time.time()
    while True:

        move = getch.getch()

        x, y, set_char_stats = moving.walk(board, x, y, move, set_char_stats, char_class, inv)

        filename, board, x, y, stage_name = stages.control_stage(x, y, filename, board, stage_name)

        moving.inv_stat_quit(inv, set_char_stats, move, stage_name)

    timer_stop = time.time()

    time_count, game_info = count_game_time(timer_start, timer_stop, char_class)

    halloffame.save_current_score(game_info, time_count)


if __name__ == '__main__':
    main()
