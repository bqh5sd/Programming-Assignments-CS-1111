def get_name(movie):
	return movie[0]

def get_gross(movie):
	return movie[1]

def get_rating(movie):
	return movie[3]
	
def get_num_ratings(movie):
	return movie[4]
	
def better_movies(movie_name, movie_list):
	better_list_movie = []
	for list in movie_list:
		name = get_name(list)
		if name == movie_name:
			movie_name_rating = get_rating(list)
			for second_list in movie_list:
				movie_list_rating = get_rating(second_list)
				if movie_list_rating > movie_name_rating:
					better_list_movie += [second_list]
	return better_list_movie
	
def average(category, movies_list):
	total_rating_score = 0 
	average = 0 
	for list in movies_list:
		if category == "rating":
			total_rating_score += get_rating(list)
			average = total_rating_score/len(list)
		elif category == "gross":
			total_gross += get_gross(list)
			average = total_gross/len(list)
		else:
			total_ratings = get_num_ratings(list)
			average = total_ratings/len(list)
	return average
					

			

