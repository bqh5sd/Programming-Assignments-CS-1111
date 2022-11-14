def max_finder(dictionary):
    max = -1
    locality = ""

    for key, value in dictionary.items():
        if value > max:
            max = value
            locality = key
    return locality


def maxServed(fptr, year, served):
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

    return max_finder(list_of_servedIndividuals)
