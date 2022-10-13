#Omid Akbari
#bqh5sd


def get_name(movie):
    '''
    The purpose of this function is to return the name of the movie in a list
    :param movie: A list that includes a movie with its specs
    :return: Returns the name of the movie in the list
    '''
    return movie[0]


def get_gross(movie):
    '''
    The purpose of this function is to return the gross earning of the movie from within a list
    :param movie: This parameters inputs a list which contains specs of a movie
    :return: Returns the gross earnings of the movie
    '''
    return movie[1]


def get_rating(movie):
    '''
    The purpose of this function is to retrieve the rating of the movie out of 10
    :param movie: This includes a list of the movies specs
    :return: Returns the third index of the list which contains the movies rating
    '''
    return movie[3]


def get_num_ratings(movie):
    '''
    The purpose of this function is to retrieve the number of ratings for a movie
    :param movie: This includes a list of the movies specs
    :return: Returns the fourth index of the list which contains the numbers of ratings for the movie
    '''
    return movie[4]


def better_movies(movie_name, movie_list):
    '''
    The purpose of this function is to determine movies which have higher ratings than an identified movie
    from within the list of movies
    :param movie_name: This is the movie within a list of movies which will be used to compares its ratings with
    ratings of other movies in the list
    :param movie_list: This is the list of movies provided by the user
    :return: This function will return list of movies which have ratings higher than the movie of interest
    '''
    better_list_movie = []
    for list in movie_list:
        name_of_movie = get_name(list)
        if name_of_movie == movie_name:
            movie_name_rating = get_rating(list)
            for second_list in movie_list:
                movie_list_rating = get_rating(second_list)
                if movie_list_rating > movie_name_rating:
                    better_list_movie += [second_list]
    return better_list_movie


def average(category, movies_list):
    '''
    The purpose of this function is to find the average ratings, gross earning, or number of ratings from a list 
    of movies depending on which category is of interest
    :param category: This is the category of interest. This has three options, average ratings, gross earning, or 
    number of ratings
    :param movies_list: This is the list of movies provided for the function
    :return: This function will return the average rating, gross earning, or number of ratings from a list of movies
    depending on the category of interest
    '''
    total_value = 0
    average = 0
    list_count = len(movies_list)
    for list in movies_list:
        if category == "rating":
            total_value += get_rating(list)
        elif category == "gross":
            total_value += get_gross(list)
        else:
            total_value += get_num_ratings(list)
        average = total_value/list_count
    return average




