#Omid Akbari
#bqh5sd

def add_state(name, votes):
    '''
    The purpose of this function is to determine the winning candidate for each state that is specified within a dictionary and build
    new dictionary with the winning candidates in each state
    :param name: This parameter takes in the name of the State which will be examined to determine winning candidates in that state
    :param votes: This parameter takes in a dictionary with names of the candidates as keys and the number of votes casted as values
    :return: This function does not return anything
    '''
    global dict
    dict = {}
    most_votes = -1
    winner_state = ''
    winner_name = ''
    for candidate, vote_count in votes.items():
        if vote_count > most_votes:
            most_votes = vote_count
            winner_state = name
            winner_name = candidate
    dict[winner_state] = winner_name
    winner_state = ''
    winner_name = ''



def winner(college):
    '''
    The purpose of this function is to read the election results from the global dictionary and determine the nation wide winner
    of the election
    :param college: This parameter takes in a dictionary which contains the different states with their associated electoral votes
    :return: This function will return the nationwide winning candidate of the election who has at least 50% of all electoral votes
    '''
    total_votes_halved = 0
    final_dict = {}
    under_half = 0
    winner = "No Winner"

    if len(college) == 0:
        return winner

    for state, electoral_vote in college.items():
        for candidate_state, candidate in dict.items():
            if state == candidate_state:
                if candidate in final_dict:
                    total_votes_halved += electoral_vote / 2
                    new_value = electoral_vote + final_dict.get(candidate)
                    final_dict[candidate] = new_value
                else:
                    total_votes_halved += electoral_vote / 2
                    final_dict[candidate] = electoral_vote
            else:
                total_votes_halved += 0
            new_value = 0

    for candidate, electoral_votes in final_dict.items():
        if electoral_votes > total_votes_halved:
            winner = candidate
            return winner
        else:
            under_half += 1
            if under_half == len(final_dict):
                return winner

    return winner

def clear():
    '''
    The purpose of this function is to resest the global variable
    :return: This function does not return anything 
    '''
    global dict
    dict = {}









