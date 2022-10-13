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
    total_score = 0
    average = 0
    count = len(movies_list)
    for list in movies_list:
        if category == "rating":
            total_score += get_rating(list)
        elif category == "gross":
            total_score += get_gross(list)
        else:
            total_score += get_num_ratings(list)
        average = total_score/count
    return average




