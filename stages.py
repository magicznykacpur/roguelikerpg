import roguelike
import janpawel


def stage_switch(current_stage):
    '''Switches the stage if player is in the right position'''
    filenames = ["stage_2.csv", "stage_3.csv", "stage_4.csv", "papaj.csv"]
    if current_stage == "stage_1.csv":
        filename = filenames[0]
        x = 4
        y = 19
        stage_name = "Stage 2 - Cave Labirynth"
        return filename, x, y, stage_name

    if current_stage == "stage_2.csv":
        filename = filenames[1]
        x = 2
        y = 12
        stage_name = "Stage 3 - Secret Altar"
        return filename, x, y, stage_name

    if current_stage == "stage_3.csv":
        filename = filenames[2]
        x = 1
        y = 12
        stage_name = "Stage 4 - Papal Cathedral"
        return filename, x, y, stage_name

    if current_stage == "stage_4.csv":
        filename = filenames[-1]
        x = 0
        y = 0
        stage_name = "Final battle - Jan Paweu Czeci"
        return filename, x, y, stage_name


def control_stage(x, y, filename, board, stage_name):
    '''Controls the current stage and going through the stages'''
    if x > 47 and y < 6 and filename == "stage_1.csv":
        filename, x, y, stage_name = stage_switch(filename)
        board = roguelike.csv_into_board(filename)
        return filename, board, x, y, stage_name

    elif x >= 57 and filename == "stage_2.csv":
        filename, x, y, stage_name = stage_switch(filename)
        board = roguelike.csv_into_board(filename)
        return filename, board, x, y, stage_name

    elif x == 24 and y == 12 and filename == "stage_3.csv":
        filename, x, y, stage_name = stage_switch(filename)
        board = roguelike.csv_into_board(filename)
        return filename, board, x, y, stage_name

    elif x == 41 and y == 12 and filename == "stage_4.csv":
        filename, x, y, stage_name = stage_switch(filename)
        board = roguelike.csv_into_board(filename)
        janpawel.main()
        return filename, board, x, y, stage_name
    else:
        return filename, board, x, y, stage_name
