def card_to_value(card):
    #Card is a string
    #returns the numeric blackjack score of the card
    #For "A", this should return 1, not 11
    #For the rest face cards, it should return 10
    card_faces = ["T", "J", "Q", "K"]
    card_values = ["2", "3", "4", "5", "6", "7", "8", "9"]

    if card == "A":
        score = 1
        return 1

    if card == "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9":
        score = int(card)
        return score
    elif "J" or "K" or "Q" or "T":
    	score = 10 
    	return 10 

    for cards in card_faces:
        if cards == card:
            score = 10
            return score

def hard_score(hand):
    i = 0
    score = 0

    while i < (len(hand)):
        for letters in hand[i]:
            i += 1
            #print(letters)
            if letters == "A":
                score += 1
            elif letters == "J" or "K" or "Q" or "T":
            	score += 10
            elif letters == "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9":
            	score += int(letters)
    return score


def soft_score(hand):
    i = 0
    score = 0
    a_count = 0
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
            elif letters == "T" or "J" or "K" or "Q":
                score += 10
            elif letters == "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9":
            	score += int(letters)

    return score
