import random
import menu

encounter_response = ['GITARA SIEMA!',
                      'Arka Gdynia Kurwa Świnia!',
                      '997 ten numer to kłopoty',
                      'DEUS VULT!',
                      'AVE PAPAY!'
                      ]

easy_questions = {"What is the capital of Italy?": "Rome",
                  "What is the square root of 16?": "4",
                  "Who won the Premier League in 2016?": "Leicester City",
                  "What is the highest mountain on Earth?": "Mount Everest",
                  "What's 17 times 31?": "527",
                  "Who wrote 'Quo Vadis'?": "Henryk Sienkiewicz",
                  "What are Opel cars called in England": "Vauxhall",
                  "How many 'Fast and Furious' movies were made?": "8",
                  "What car brand produces the Golf model?": "Volkswagen",
                  "What is the highest mountain in Europe?": "Mont Blanc",
                  "What is the longest river in the world?": "Amazon",
                  "What time did John Paul II die?": "21:37",
                  "What club does Robert Lewandowski play for?": "Bayern Munich",
                  "What year did the World War II end?": "1945",
                  "Do you like donuts?": "Yes"}
hard_questions = {"What is the height of K2 in meters?": "8611",
                  "What was the first city to be struck by a nuclear bomb?": "Hiroshima",
                  "Who was the first communist leader of China?": "Mao Tse Tung",
                  "Who released an album called 'To Pimp a Butterfly'?": "Kendrick Lamar",
                  "What is the highest mountain in the Solar System?": "Olympus Mons",
                  "What was the Nazi party in Third Reich called?": "NSDAP",
                  "In what year was Constantinople captured by the Turks?": "1453"
                  }


def encounter(char_stats):
    '''Handles enemy encountering'''

    wound_count = 0

    if char_stats['ATK'] >= 7:
        question, answer = easymode()
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
        question, answer = hardmode()
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
                        menu.game_over()
    return wound_count


def easymode():
    '''Picks easy questions'''
    easy = list(easy_questions.keys())
    key = random.choice(easy)
    answer = easy_questions[key]
    return key, answer


def hardmode():
    '''Picks hard questions'''
    hard = list(hard_questions.keys())
    key = random.choice(hard)
    answer = hard_questions[key]
    return key, answer


def delete_cunt(board, x, y):
    '''Deletes enemy after succesful encounter'''
    board[y][x] = "*"
