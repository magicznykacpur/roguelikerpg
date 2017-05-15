import os
import sys
import tty
import termios
import csv
from termcolor import colored, cprint


def board_into_csv(board):
    '''Writes the board into a csv file'''
    with open("stage.csv", "w") as f:
        w = csv.writer(f, delimiter=' ')
        for item in board:
            w.writerow(item)


def csv_into_board():
    '''Opens a board from csv file'''
    board = []
    with open("stage.csv", newline='') as f:
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
        if item.count("#") > 2:
            cprint("".join(item), 'red', 'on_red')
        elif item.count("#") == 2:
            cprint(item[0], 'red', 'on_red', end='')
            cprint("".join(item[1:-1]), end='')
            cprint(item[-1], 'red', 'on_red')


def insert_player(board, x, y):
    '''Inserts a player on a given
        position into the board'''
    x = int(x)
    y = int(y)
    karakan = "@"
    board[y][x] = karakan
    return board


def char_stats(char_class):
    '''Returns a dictionary of charaters stats'''
    char_stats = {}
    char_class = char_class - 1
    # list of tuples with each classes stats
    character_list = [(8, 4, 8, 1), (12, 4, 4, 1), (4, 8, 8, 1)]
    char_stats['ATK'] = character_list[char_class][0]
    char_stats['DEF'] = character_list[char_class][1]
    char_stats['HP'] = character_list[char_class][2]
    char_stats['LVL'] = character_list[char_class][3]
    return char_stats


def character_info(set_char_stats):
    '''Prints characters stats in a neat way'''
    for stat, value in sorted(set_char_stats.items()):
        print(stat, value)


def character_info(set_char_stats):
    '''Prints characters stats in a neat way'''
    for stat, value in sorted(set_char_stats.items()):
        print(stat, value)


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

    x = 5
    y = 5

    char_class = int(input("""Choose your character class:
    1) Warrior - 8 ATK, 4 DEF, 8 HP
    2) Assassin - 12 ATK, 4 DEF, 4 HP
    3) Knight - 4 ATK, 8 DEF, 8 HP
    """))

    board = csv_into_board()

    board = insert_player(board, x, y)

    set_char_stats = char_stats(char_class)
    character_info(set_char_stats)

    print_board(board)

    while True:

        move = getch()

        if move == "a":
            x = int(x)
            y = int(y)
            if board[y][x - 1] == "-":
                board = insert_player(board, x - 1, y)
                board[y][x] = '-'
                os.system('clear')
                print_board(board)
                character_info(set_char_stats)
                x = x - 1
        elif move == "d":
            x = int(x)
            y = int(y)
            if board[y][x + 1] == "-":
                board = insert_player(board, x+1, y)
                board[y][x] = "-"
                os.system('clear')
                print_board(board)
                character_info(set_char_stats)
                x = x + 1
            else:
                pass
        elif move == "w":
            x = int(x)
            y = int(y)
            if board[y - 1][x] == "-":
                board = insert_player(board, x, y-1)
                board[y][x] = "-"
                os.system('clear')
                print_board(board)
                character_info(set_char_stats)
                y = y - 1
            else:
                pass
        elif move == "s":
            x = int(x)
            y = int(y)
            if board[y + 1][x] == "-":
                board = insert_player(board, x, y+1)
                board[y][x] = "-"
                os.system('clear')
                print_board(board)
                character_info(set_char_stats)
                y = y + 1
            else:
                pass
        elif move == "q":
            sys.exit()


if __name__ == '__main__':
    main()
