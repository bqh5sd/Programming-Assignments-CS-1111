#Omid Akbari
#bqh5sd



def quad(x, y):
    '''
    :param x: X value and sign input into the function
    :param y: Y value input into function 
    :return: 
    '''
    if x > 0 and y > 0:
        print("1")
    elif x < 0 and y > 0:
        print("2")
    elif x < 0 and y < 0:
        print("3")
    elif x > 0 and y < 0:
        print("4")
    else:
        print("0")
