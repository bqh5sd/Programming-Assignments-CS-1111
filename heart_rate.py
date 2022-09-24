#Omid Akbari (bqh5sd)

#Calculate fine for speeding
def fine(speed_limit, my_speed, zone = "None"):
    '''
    This function calculates the fine for speeding given the speed limit that is set and the speed
    that is being recorded for an individual. This function also consider the city zone in which this
    calculation is based off of.
    :param speed_limit: The integer speed limit that is set by the city
    :param my_speed: Integer speed which is being recorded by yourself 
    :param zone: A string which denotes the type of zone you are in for the given calculation
    :return: Returns the total dollar integer amount of money that you owe
    '''
    amount_due = 0
    speed_limit_difference = my_speed - speed_limit
    if speed_limit_difference > 0 and speed_limit_difference < 20:
        if "residential" in zone:
            print(zone)
            amount_due = (speed_limit_difference*8)+200
        elif zone == "school" or zone == "work":
            amount_due = speed_limit_difference*7
        else:
            amount_due = speed_limit_difference*6
    else:
        if speed_limit_difference >= 20:
            amount_due += 350
        elif speed_limit_difference < -10:
            amount_due += 30
    return amount_due

#Calculate demerits points for speeding
def demerits(speed_limit, my_speed):
    '''
    The function calculates the total demerit points earned for speeding under some 
    pre-determined ranges
    
    :param speed_limit: The integer speed limit that is set by the city
    :param my_speed: Integer speed which is being recorded by yourself
    :return: Returns the total integer demerit point earned for speeding violations
    '''
    speed_limit_difference = my_speed - speed_limit
    demerits_points = 0
    if speed_limit_difference >= 1 and speed_limit_difference <=9:
        demerits_points += 3
    elif speed_limit_difference >= 10 and speed_limit_difference <= 19:
        demerits_points += 4
    elif speed_limit_difference >= 20:
        demerits_points += 6
    else:
        demerits_points = 0
    return demerits_points

