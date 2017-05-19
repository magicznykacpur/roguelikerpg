import items
import inventory
import combatbase
import roguelike
import player_stats
import os
import sys


def go_left(x, y, board):
    '''Moves the player right'''
    board = roguelike.insert_player(board, x - 1, y)
    board[y][x] = '*'
    os.system('clear')
    roguelike.print_board(board)
    x = x - 1
    return x, y, board


def encounter_chest_left(x, y, board, inv, char_class):
    '''Handles encountering a chest on the right of player'''
    open_chest = items.encounter_item()
    items.loot_item(board, open_chest, x - 1, y)
    loot = items.generate_item(open_chest)
    inventory.add_to_inventory(inv, loot)
    set_char_stats = player_stats.char_stats(char_class, inv, wound_count=0)
    return x, y, board, set_char_stats


def encounter_enemy_left(x, y, board, inv, char_class, set_char_stats):
    '''Handles encountering an enemy on the right of player'''
    wound_count = combatbase.encounter(set_char_stats)
    combatbase.delete_cunt(board, x - 1, y)
    set_char_stats = player_stats.char_stats(char_class, inv, wound_count)
    return x, y, board, set_char_stats


def move_left(x, y, board, inv, char_class, set_char_stats):
    '''Handles moving the player left with all encounters'''
    x = int(x)
    y = int(y)
    if board[y][x - 1] == "*":
        x, y, board = go_left(x, y, board)
    elif board[y][x - 1] == ".":
        x, y, board, set_char_stats = encounter_chest_left(x, y, board, inv, char_class)
    elif board[y][x - 1] == "†":
        x, y, board, set_char_stats = encounter_enemy_left(x, y, board, inv, char_class, set_char_stats)
    return x, y, board, set_char_stats


def go_right(x, y, board):
    '''Moves the player right'''
    board = roguelike.insert_player(board, x + 1, y)
    board[y][x] = '*'
    os.system('clear')
    roguelike.print_board(board)
    x = x + 1
    return x, y, board


def encounter_chest_right(x, y, board, inv, char_class):
    '''Handles encountering a chest on the right of player'''
    open_chest = items.encounter_item()
    items.loot_item(board, open_chest, x + 1, y)
    loot = items.generate_item(open_chest)
    inventory.add_to_inventory(inv, loot)
    set_char_stats = player_stats.char_stats(char_class, inv, wound_count=0)
    return x, y, board, set_char_stats


def encounter_enemy_right(x, y, board, inv, char_class, set_char_stats):
    '''Handles encountering an enemy on the right of player'''
    wound_count = combatbase.encounter(set_char_stats)
    combatbase.delete_cunt(board, x + 1, y)
    set_char_stats = player_stats.char_stats(char_class, inv, wound_count)
    return x, y, board, set_char_stats


def move_right(x, y, board, inv, char_class, set_char_stats):
    '''Handles moving the player left with all encounters'''
    x = int(x)
    y = int(y)
    if board[y][x + 1] == "*":
        x, y, board = go_right(x, y, board)
    elif board[y][x + 1] == ".":
        x, y, board, set_char_stats = encounter_chest_right(x, y, board, inv, char_class)
    elif board[y][x + 1] == "†":
        x, y, board, set_char_stats = encounter_enemy_right(x, y, board, inv, char_class, set_char_stats)
    return x, y, board, set_char_stats


def go_up(x, y, board):
    '''Moves the player right'''
    board = roguelike.insert_player(board, x, y - 1)
    board[y][x] = '*'
    os.system('clear')
    roguelike.print_board(board)
    y = y - 1
    return x, y, board


def encounter_chest_up(x, y, board, inv, char_class):
    '''Handles encountering a chest on the right of player'''
    open_chest = items.encounter_item()
    items.loot_item(board, open_chest, x, y - 1)
    loot = items.generate_item(open_chest)
    inventory.add_to_inventory(inv, loot)
    set_char_stats = player_stats.char_stats(char_class, inv, wound_count=0)
    return x, y, board, set_char_stats


def encounter_enemy_up(x, y, board, inv, char_class, set_char_stats):
    '''Handles encountering an enemy on the right of player'''
    wound_count = combatbase.encounter(set_char_stats)
    combatbase.delete_cunt(board, x, y - 1)
    set_char_stats = player_stats.char_stats(char_class, inv, wound_count)
    return x, y, board, set_char_stats


def move_up(x, y, board, inv, char_class, set_char_stats):
    '''Handles moving the player left with all encounters'''
    x = int(x)
    y = int(y)
    if board[y - 1][x] == "*":
        x, y, board = go_up(x, y, board)
    elif board[y - 1][x] == ".":
        x, y, board, set_char_stats = encounter_chest_up(x, y, board, inv, char_class)
    elif board[y - 1][x] == "†":
        x, y, board, set_char_stats = encounter_enemy_up(x, y, board, inv, char_class, set_char_stats)
    return x, y, board, set_char_stats


def go_down(x, y, board):
    '''Moves the player right'''
    board = roguelike.insert_player(board, x, y + 1)
    board[y][x] = '*'
    os.system('clear')
    roguelike.print_board(board)
    y = y + 1
    return x, y, board


def encounter_chest_down(x, y, board, inv, char_class):
    '''Handles encountering a chest on the right of player'''
    open_chest = items.encounter_item()
    items.loot_item(board, open_chest, x, y + 1)
    loot = items.generate_item(open_chest)
    inventory.add_to_inventory(inv, loot)
    set_char_stats = player_stats.char_stats(char_class, inv, wound_count=0)
    return x, y, board, set_char_stats


def encounter_enemy_down(x, y, board, inv, char_class, set_char_stats):
    '''Handles encountering an enemy on the right of player'''
    wound_count = combatbase.encounter(set_char_stats)
    combatbase.delete_cunt(board, x, y + 1)
    set_char_stats = player_stats.char_stats(char_class, inv, wound_count)
    return x, y, board, set_char_stats


def move_down(x, y, board, inv, char_class, set_char_stats):
    '''Handles moving the player left with all encounters'''
    x = int(x)
    y = int(y)
    if board[y + 1][x] == "*":
        x, y, board = go_down(x, y, board)
    elif board[y + 1][x] == ".":
        x, y, board, set_char_stats = encounter_chest_down(x, y, board, inv, char_class)
    elif board[y + 1][x] == "†":
        x, y, board, set_char_stats = encounter_enemy_down(x, y, board, inv, char_class, set_char_stats)
    return x, y, board, set_char_stats


def walk(board, x, y, move, set_char_stats, char_class, inv):
    '''Main movement function. Takes all the needed arguments
        and returns new player position'''

    if move == "a":
        x, y, board, set_char_stats = move_left(x, y, board, inv, char_class, set_char_stats)

    elif move == "d":
        x, y, board, set_char_stats = move_right(x, y, board, inv, char_class, set_char_stats)

    elif move == "w":
        x, y, board, set_char_stats = move_up(x, y, board, inv, char_class, set_char_stats)

    elif move == "s":
        x, y, board, set_char_stats = move_down(x, y, board, inv, char_class, set_char_stats)

    return x, y, set_char_stats


def inv_stat_quit(inv, set_char_stats, move, stage_name):
    '''Inventory, stats checking. Quiting the game'''
    if move == "i":
        inventory.print_inventory_table(inv)
    elif move == "c":
        player_stats.character_info(set_char_stats, stage_name)
    elif move == "q":
        sys.exit()
