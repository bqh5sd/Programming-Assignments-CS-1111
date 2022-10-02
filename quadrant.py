#Omid Akbari
#bqh5sd



def quad(x, y):
    '''
    :param x: input of x coordinate with magnitude and sign
    :param y: input of y coordinate with magnitude and sign
    :return: Returns the quadrant where x and y coordinate of a single point lies on the xy plane

    '''
    # Check conditions of x and y using logic, where a specific quadrant must contain certain x and y values
    # if x or y are 0, or both are zero, then a quadrant DNE and will return 0
    if x > 0 and y > 0:
        quadrant = 1
    elif x < 0 and y > 0:
        quadrant = 2
    elif x < 0 and y < 0:
        quadrant = 3
    elif x > 0 and y < 0:
        quadrant = 4
    else:
        quadrant = 0

    return quadrant


