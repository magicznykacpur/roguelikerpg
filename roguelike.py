import os
import sys


def create_board(width, height):
    '''Creates a board of given width and height'''
    board = []
    outer_row = []
    inner_row = []
    width = int(width)
    height = int(height)
    for item in range(width):
        outer_row.append('#')
    inner_row.append('#')
    for item in range(width - 2):
        inner_row.append('-')
    inner_row.append('#')
    board.append(outer_row)
    for item in range(height - 2):
        board.append(inner_row[:])
    board.append(outer_row)
    return board


def print_board(board):
    '''Prints the given board'''
    board_list = board
    for item in board_list:
        print("".join(item))


def insert_player(board, x, y):
    '''Inserts a player on a given
        position into the board'''
    x = int(x)
    y = int(y)
    karakan = "@"
    board[y][x] = karakan
    return board


def getch():
    import sys
    import tty
    import termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def main():
    global board
    global x
    global y
    width = input("Enter map width: ")
    height = input("Enter map height: ")
    x = input("Enter character x: ")
    y = input("Enter character y: ")
    board = create_board(width, height)
    board = insert_player(board, x, y)
    width = int(width)
    height = int(height)
    print_board(board)
    while True:
        os.system('clear')
        chuj = getch()
        if chuj == "a":
            x = int(x)
            y = int(y)
            if x != 1:
                board = insert_player(board, x-1, y)
                board[y][x] = "-"
                os.system('clear')
                print_board(board)
                x = x - 1
            else:
                pass
        elif chuj == "d":
            x = int(x)
            y = int(y)
            if x != width - 2:
                board = insert_player(board, x+1, y)
                board[y][x] = "-"
                os.system('clear')
                print_board(board)
                x = x + 1
            else:
                pass
        elif chuj == "w":
            x = int(x)
            y = int(y)
            if y != 1:
                board = insert_player(board, x, y-1)
                board[y][x] = "-"
                os.system('clear')
                print_board(board)
                y = y - 1
            else:
                pass
        elif chuj == "s":
            x = int(x)
            y = int(y)
            if y != height - 2:
                board = insert_player(board, x, y+1)
                board[y][x] = "-"
                os.system('clear')
                print_board(board)
                y = y + 1
            else:
                pass
        elif chuj == "q":
            sys.exit()


if __name__ == '__main__':
    main()
