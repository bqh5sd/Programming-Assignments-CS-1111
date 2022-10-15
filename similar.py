#Omid Akbari
#bqh5sd

def compare(list):
    '''
    This function compares the first and last character of a string in a list of strings to test if they are the same character
    :param list: This is the list being tested with various string within
    :return: Returns the total number of strings which have their first and last character the same
    '''
    strings_similar = 0
    for string in list:
        first_character = string[0]
        length = len(string)
        if first_character.upper() == string[length-1].upper():
            strings_similar += 1
    return strings_similar



