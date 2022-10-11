#Omid Akbari
#bqh5sd


def card_to_value(card):
    '''
    The purpose of this function is to see how much a card is valued/worth in the game
    :param card: This is the input parameter for the type of card being tested
    :return: This function will return the value worth of the card in ordinance with the game
    '''
    #Pre-set card faces and card numbers
    card_faces = ("TJQK")
    card_numbers = ("23456789")
    #If the card is an Ace
    if card == "A":
        points = 1
        return points
    #Checks the type of card numbers with the card input to return the value(points) of that card
    for cards in card_numbers:
        if cards == card:
            points = int(card)
            return points
    #Checks the type of card face with the card input to return the value(points) of that card
    for cards in card_faces:
        if cards == card:
            points = 10
            return points

def hard_score(hand):
    '''
    The purpose of this function is to find the hard score value of a set of cards which is input into the function
    :param hand: The set of cards which will be tested to calculate the total amount of points for those all the cards
    :return: This function will return the total score of the provided cards
    '''
    string_index = 0
    score = 0
    # Pre-set card faces and card numbers
    card_faces = ("TJQK")
    card_values = ("23456789")
    #Runs through to check the input cards against the type of cards avaible in the game to calculate the total amount of points
    #For the Hard score, all aces will be worth 1
    while string_index < (len(hand)):
        for letters in hand[string_index]:
            string_index += 1
            if letters == "A":
                score += 1
            for cards in card_faces:
                if cards == letters:
                    score += 10
            for cards in card_values:
                if cards == letters:
                    score += int(letters)
    return score


def soft_score(hand):
    '''
    The purpose of this function is to find the soft score value of a set of cards which is input into the function
    :param hand: The set of cards which will be tested to calculate the total amount of points for those all the cards
    :return: This function will return the total score of the provided cards
    '''
    string_index = 0
    score = 0
    ace_count = 0
    # Pre-set card faces and card numbers
    card_faces = ("TJQK")
    card_values = ("23456789")
    # Runs through to check the input cards against the type of cards avaible in the game to calculate the total amount of points
    # For the Soft score, all aces will be worth 11, but more than one ace will make the value of the ace 1 after
    while string_index < (len(hand)):
        for letters in hand[string_index]:
            string_index += 1
            # print(letters)
            if letters == "A":
                ace_count += 1
                if ace_count > 1:
                    Ace_value = 1
                else:
                    Ace_value = 11
                score += Ace_value
            for cards in card_faces:
                if cards == letters:
                    score += 10
            for cards in card_values:
                if cards == letters:
                    score += int(letters)

    return score





