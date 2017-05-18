def char_stats(char_class, inventory, wound_count):
    '''Returns a dictionary of characters stats'''
    char_stats_dict = {}
    char_class = char_class - 1

    character_list = [(8, 4, 8), (12, 4, 4), (4, 8, 8)]
    char_stats_dict['ATK'] = character_list[char_class][0]
    char_stats_dict['DEF'] = character_list[char_class][1]
    char_stats_dict['HP'] = character_list[char_class][2]

    if "DildoMocy" in inventory:
        char_stats_dict['ATK'] += 2
    if "TarczaWiksy" in inventory:
        char_stats_dict['DEF'] += 3
    if "CzapkaWpierdolu" in inventory:
        char_stats_dict['HP'] += 1
    if "OnuceZapierdalania" in inventory:
        char_stats_dict['DEF'] += 1
    if "RekawiceTrzepania" in inventory:
        char_stats_dict['HP'] += 1
    char_stats_dict['HP'] -= wound_count
    return char_stats_dict


def character_info(set_char_stats, stage_name):
    '''Prints characters stats in a neat way'''
    print(stage_name)
    for stat, value in sorted(set_char_stats.items()):
        print(stat + " " + str(value) + "  ")
