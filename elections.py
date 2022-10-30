dict = {}

def add_state(name,votes):
	global dict
	most_votes = -1
	winner_state = ''
	winner_name = ''
	for canadidate, vote_count in votes.items():
		if vote_count > most_votes:
			most_votes = vote_count
			winner_state = name
			winner_name = canadidate
	dict[winner_state] = winner_name
	most_votes = -1
	winner_name = ''
	winner_state = ''



	
	
def winner(college):
	total_votes_halved = 0
	final_winner =''
	#dictinoary with the name of the candidate and the total number of votes casted 
	final_dict = {}
	under_half = 0
	winner = "No Winner"
	
	if len(college) == 0:
		return winner
	
	for state, electoral_vote in college.items():
		for candidate_state, candidate in dict.items():
			if state == candidate_state:
				if candidate in final_dict:
					total_votes_halved += electoral_vote/2
					new_value = electoral_vote + final_dict.get(candidate)
					final_dict[candidate] = new_value
				else:
					total_votes_halved += electoral_vote/2
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
	global dict
	dict = {}
	

college = {'Virginia': 13, "Ohio" : 18, "Alabama" : 9}
	
	
add_state('Virginia', {'Turing' : 15, 'Lovelace' : 20, 'Dijkstra' : 10})

add_state('Ohio', {'Turing' : 1, 'Dijkstra' : 15})

add_state("Alabama", {'Turing' : 10, 'Lovelace' : 5, 'Dijkstra' : 15})

print(winner(college))







