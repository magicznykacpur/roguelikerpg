import csv
import getch
import os
import sys
import tty
import termios
import roguelike
import halloffame


def menu():
    '''Function operates the start menu'''
    menu_board = menu_from_csv()
    print_menu(menu_board)

    while True:

        select = getch.getch()
        os.system('clear')

        while select not in ["a", "1", "2", "3", "q", "y", "s", "h", "m"]:
            os.system('clear')
            print_menu(menu_board)
            select = getch.getch()
            pass

        if select == "a":
            logo_board = menu_from_csv("studio_logo.csv")
            print_menu(logo_board)
        elif select == "s":
            story_board = menu_from_csv("plot.csv")
            print_menu(story_board)
        elif select == "1":
            board = menu_from_csv("warrior.csv")
            roguelike.print_board(board)
            char_class = 1
        elif select == "y":
            break
        elif select == "2":
            board = menu_from_csv("knight.csv")
            roguelike.print_board(board)
            char_class = 3
        elif select == "y":
            break
        elif select == "3":
            board = menu_from_csv("assassin.csv")
            roguelike.print_board(board)
            char_class = 2
        elif select == "y":
            break
        elif select == "h":
            halloffame.show_high_scores()
        elif select == "m":
            print_menu(menu_board)
        elif select == "q":
            sys.exit()

    return char_class


def menu_from_csv(filename="enter_screen.csv"):
    '''Shows a start menu, with game name and class selection'''
    menu_board = []
    with open(filename, newline='') as f:
        r = csv.reader(f)
        for row in f:
            row = row.strip()
            row = list(row)
            menu_board.append(row)
    return menu_board


def print_menu(menu_board):
    '''Prints out the menu'''
    for row in menu_board:
        print("".join(row))


def start_game(char_class):
    '''Starts the game after the class is selected'''
    if char_class:
        filename = "stage_1.csv"
        x = 2
        y = 16
        stage_name = "Stage 1 - The River"
    return x, y, filename, stage_name


def game_over():
    '''Prints out a game over screenn'''

    os.system('clear')
    over_screen = menu_from_csv("game_over.csv")
    print_menu(over_screen)

    select = getch.getch()
    while select not in ["m", "q"]:
        os.system('clear')
        print_menu(over_screen)
        select = getch.getch()

    if select:
        sys.exit()
