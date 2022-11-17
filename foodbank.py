#bqh5sd
#Omid Akbari


def maxServed(fptr, year, served):
    '''
    The purpose of this function is to find the locality within virginia that has either the maximum number
    of household served, individuals served or children served depending on the intrest
    :param fptr: This parameter takes in file data that contains various forms of data
    :param year: This parameter takes in the year of interest
    :param served: This parameter takes in the quirey of interest where 1 is households served, 2 is individuals
    served and 3 is the children served
    :return:
    '''
    data = fptr.read().strip().split('\n')

    ref = -1
    max_locality = ""

    for current_data in data[1:]:
        current_data = current_data.split(",")
        for i in range(8):
            if current_data[i] == "":
                current_data[i] = "0"

        if served == 0:
            if int(current_data[0]) == year:
                if int(current_data[3]) > ref:
                    ref = int(current_data[3])
                    max_locality = current_data[2]

        if served == 1:
            if int(current_data[0]) == year:
                if int(current_data[4]) > ref:
                    ref = int(current_data[4])
                    max_locality = current_data[2]
        if served == 2:
            if int(current_data[0]) == year:
                if int(current_data[6]) > ref:
                    ref = int(current_data[6])
                    max_locality = current_data[2]
    return max_locality
