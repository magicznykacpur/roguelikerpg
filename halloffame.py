import menu


def save_current_score(game_info, time_count):
    '''Saves current games score to the file'''
    score = (game_info["character_class"], time_count["time"])
    formatted_score = []
    for item in score:
        item = str(item)
        formatted_score.append(item)
    formatted_score = ' | '.join(score_formated)
    highscore_file = open("./high_score.csv", "a")
    highscore_file.write(formatted_score + "\n")


def show_high_scores():
    try:
        highscore_file = open("./high_score.csv", "a")
        highscore_list = []
        for line in highscore_file:
            line = line.strip()
            line = line.split(' | ')
            for item in line:
                item.split()
            highscore_list.append(line)
        highscore_list = sorted(highscore_list, key=lambda record: int(record[2]),
                                reverse=True)
        print("\nHIGHSCORES:\n")
        if len(highscore_list) < 10:
            for i in range(len(highscore_list)):
                print(' | '.join(highscore_list[i]))
        else:
            for i in range(10):
                print(' | '.join(highscore_lsit[i]))
    except (ValueError, IndexError):
        print("Error occured while reading high scores file\n")
