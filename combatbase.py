import random

encounter_response = ['GITARA SIEMA!',
                      'Arka Gdynia Kurwa Świnia!',
                      '997 ten numer to kłopoty',
                      'DEUS VULT!',
                      'AVE PAPAY!'
                      ]

easy_questions = {"2 + 2 = ?": "4", "16 - 8 = ?": "4"}
hard_questions = {"arka gdynia": "kurwa świnia", "korona kielce": "kurwa widelce"}


def easymode():
    easy = list(easy_questions.keys())
    key = random.choice(easy)
    answer = easy_question[key]
    return key, answer


def hardmode():
    hard = list(hard_questions.keys())
    key = random.choice(hard)
    answer = hard_question[key]
    return key, answer


def delete_cunt(board, x, y):
    board[y][x] == "*"
