#Omid Akbari (bqh5sd)


#Estimate the heart rate in bearts per minute (bmp)
def gellish2(age):
    '''
    Use gellish2 equation to calculate estimated heart rate
    return heart rate as a float
    '''
    est_HRmax = 191.5 - (0.007*age**2)
    return float(est_HRmax)

#Tests whether or not the estimated heart rate is in target range between 65% and 85% which is desired range of heart rate
def in_target_range(hr, age):
    '''
    Set a range to test against the estimated heart rate from the gellish2 equation
    return a boolean data type by using logical operators
    '''
    target_range_lower = 0.65*gellish2(age)
    target_range_upper = 0.85*gellish2(age)
    range_result = (target_range_lower < hr < target_range_upper)
    return range_result




