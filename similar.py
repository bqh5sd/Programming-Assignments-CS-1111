def compare(list):
    strings_similar = 0
    for string in list:
        first_character = string[0]
        length = len(string)
        if first_character.upper() == string[length-1].upper():
            strings_similar += 1
    return strings_similar



