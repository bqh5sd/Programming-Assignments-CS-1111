def card_to_value(card):
    #Card is a string
    #returns the numeric blackjack score of the card
    #For "A", this should return 1, not 11
    #For the rest face cards, it should return 10
    print(card)
    if card == "A":
        score = 1
        return 1
    elif card == "J" or "K" or "Q" or "T":
        score = 10 
        return score
    elif card == "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9":
        #print(card)
        score = int(card)
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


print(card_to_value("Q"))

