def max_finder(dictionary):
    '''
    The purpose of this function is to find the max value in a dictionary
    :param dictionary: This parameter takes in a dictionary of cities and values
    :return: Return the max value
    '''
    max = -1
    locality = ""

    for key, value in dictionary.items():
        if value > max:
            max = value
            locality = key
    return locality


def maxServed(fptr, year, served):
    '''
    prupose of this function is to find more information about different cities food bank services
    :param fptr: Takes a file data 
    :param year: Takes in the year that is in intrest 
    :param served: Takes in what is of intrest to find the max of in a specific locality 
    :return: Return the city which is of intrest based on the served parameter
    '''
    data = fptr.read().strip().split('\n')

    list_of_served = {}
    list_of_servedIndividuals = {}
    list_of_servedChildren = {}

    for current_data in data:
        current_data = current_data.split(",")
        if current_data[0] == str(year):
            if served == 0:
                if current_data[3] != "":
                    if current_data[2] in list_of_served:
                        if list_of_served[current_data[2]] > int(current_data[3]):
                            list_of_served[current_data[2]] = int(current_data[3])
                    else:
                        list_of_served[current_data[2]] = int(current_data[3])
            if served == 1:
                if current_data[4] != "":
                    if current_data[2] in list_of_servedIndividuals:
                        if list_of_servedIndividuals[current_data[2]] > int(current_data[4]):
                            list_of_servedIndividuals[current_data[2]] = int(current_data[4])
                    else:
                        list_of_servedIndividuals[current_data[2]] = int(current_data[4])
            if served == 2:
                if current_data[6] !="":
                    if current_data[2] in list_of_servedChildren:
                        if list_of_servedChildren[current_data[2]] > int(current_data[6]):
                            list_of_servedChildren[current_data[2]] = int(current_data[6])
                    else:
                        list_of_servedChildren[current_data[2]] = int(current_data[6])

    if served == 0:
        return max_finder(list_of_served)
    elif served == 1:
        return max_finder(list_of_servedIndividuals)
    else:
        return max_finder(list_of_servedChildren)

