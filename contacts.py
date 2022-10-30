#Omid Akbari
#bqh5sd

def update(contactDict, list_of_values):
    '''
    The purpose of this function is to update a dictionary filled with contact information from different individuals
    :param contactDict: This parameters takes in the contact dictionary provided with names and emails
    :param list_of_values: This parameter takes in a list of operations that is to be performed by the function to determine what and what not to update 
    in the contact dictionary
    :return: This function will return the number of errors that occur throughout this function
    '''
    error_count = 0
    for operator in list_of_values:
        if operator[0] == "+":
            if operator[1] in contactDict:
                error_count += 1
            else:
                contactDict[operator[1]] = operator[2]
        elif operator[0] == "/":
            if operator[1] in contactDict:
                contactDict[operator[1]] = operator[2]
            else:
                error_count += 1
        elif operator[0] == "-":
            if operator[1] in contactDict:
                del contactDict[operator[1]]
            else:
                error_count += 1
        else:
            error_count += 1
    return error_count


