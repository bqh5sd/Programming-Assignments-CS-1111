


def card_to_value(card):
    #Card is a string
    #returns the numeric blackjack score of the card
    #For "A", this should return 1, not 11
    #For the rest face cards, it should return 10
    card_faces = ("TJQK")
    card_values = ("23456789")

    i = 0

    if card == "A":
        score = 1
        return 1

    for cards in card_values[i]:
        i += 1
        if cards == card:
            score = int(card)
            return score

    for cards in card_faces:
        if cards == card:
            score = 10
            return score

def hard_score(hand):
    i = 0
    score = 0

    card_faces = ("TJQK")
    card_values = ("23456789")

    while i < (len(hand)):
        for letters in hand[i]:
            i += 1
            #print(letters)
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
    i = 0
    score = 0
    a_count = 0

    card_faces = ("TJQK")
    card_values = ("23456789")

    while i < (len(hand)):
        for letters in hand[i]:
            i += 1
            # print(letters)
            if letters == "A":
                a_count += 1
                if a_count > 1:
                    Ace_score = 1
                else:
                    Ace_score = 11
                score += Ace_score
            for cards in card_faces:
                if cards == letters:
                    score += 10
            for cards in card_values:
                if cards == letters:
                    score += int(letters)

    return score




