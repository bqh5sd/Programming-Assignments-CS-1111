#Omid Akbari
#bqh5sd

def mean_all(table):
    '''
    The purpose of this function is to calculate the mean of all the numbers in the rows and columns of a given table
    :param table: This takes in the table of values 
    :return: This function will return the mean/average as a float value of all the values contained in the table
    '''
    total = 0
    number_of_cells = 0
    for column in table:
        for list_number in column:
            number_of_cells += 1
            total += list_number
    return float(total / number_of_cells)


def mean_by_row(table):
    '''
    The purpose of this function is to calculate the average values in each row from a nxn table
    :param table: This parameters takes in the table provided
    :return: This function will return a list of averages for each row in the table provided
    '''
    row_total = 0
    row_count = len(table[0][:])
    row_mean_list = []
    for row_list in table:
        for list_number in row_list:
            row_total += list_number
        row_mean = float(row_total / row_count)
        row_mean_list += [row_mean]
        row_total = 0
    return row_mean_list


def mean_by_col(table):
    '''
    The purpose of this function is to calculate the average of each column in a given n x n table 
    :param table: This function will take in a table of values as its parameter
    :return: This function will return a list of all the averages in each column of the table
    '''
    column_list_index = 0
    column_total = 0
    length_col = len(table)
    len_row = len(table[0][:])
    col_mean_list = []
    count = 0
    while count < length_col + 1:
        for list in table:
            count += 1
            column_total += list[column_list_index]
            if count == length_col:
                col_mean_list += [column_total / length_col]
                column_list_index += 1
                count = 0
                column_total = 0
                if column_list_index == len_row - 0:
                    return col_mean_list







