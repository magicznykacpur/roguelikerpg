import csv
import getch
import os
import sys
import tty
import termios
import roguelike


def menu():
    '''Function operates the start menu'''
    menu_board = menu_from_csv()
    print_menu(menu_board)

    while True:

        select = getch()
        os.system('clear')

        if select == "a":
            pass
        elif select == "1":
            board = menu_from_csv("warrior.csv")
            roguelike.print_board(board)
        elif select == "2":
            board = menu_from_csv("knight.csv")
            roguelike.print_board(board)
        elif select == "3":
            board = menu_from_csv("assassin.csv")
            roguelike.print_board(board)
        elif select == "q":
            sys.exit()


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
    for row in menu_board:
        print("".join(row))


def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch
