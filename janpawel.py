import random
import sys
import menu
import os
from termcolor import colored, cprint


def generate_number():
    '''Generates a random 3-digit number,
    if chars repeat in the number, the number is generated again'''

    number = random.randint(100, 999)
    for char in str(number):
        if str(number).count(char) > 1:
            number = random.randint(100, 999)

    return number


def guess_number():
    '''Takes user input for the guessed number'''
    guessed_number = input("Enter a number\n")

    while len(str(guessed_number)) != 3 or str(guessed_number).isalpha():
        guessed_number = input("\nTry entering a 3-digit number BOI: ")

    guessed_number = int(guessed_number)
    return guessed_number


def main():

    os.system('clear')
    filename = "papaj.csv"
    papaj_board = menu.menu_from_csv(filename)
    menu.print_menu(papaj_board)

    while True:

        try_number = 10
        guessed_number = 0
        number = generate_number()
        number = str(number)
        while guessed_number != number:
            os.system('clear')
            menu.print_menu(papaj_board)
            print("Hello child, prepare to be baptized.")
            print("I am thinking of a 3-digit number. Try to guess what it is.\n")
            while try_number != 0:
                print("\nGuesses left:" + str(try_number))
                try_number -= 1

                guessed_number = guess_number()
                guessed_number = str(guessed_number)

                for char in range(len(number)):
                    if guessed_number[char] == number[char]:
                        cprint('\nHot\n', 'red')
                    elif guessed_number[char] in number:
                        cprint('Warm\n', 'yellow')
                    else:
                        cprint('Cold\n', 'blue')

                if guessed_number == number:
                    print("\nAaa, to ten numer! Jak najbardziej, jeszcze jak.")
                    break
            break
        break


if __name__ == '__main__':
    main()
