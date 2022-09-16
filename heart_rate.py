#Omid Akbari (bqh5sd)


#Estimate the heart rate in bearts per minute (bmp)
def gellish2(age):
    #Gellish2 equation
    est_HRmax = 191.5 - (0.007*age**2)
    return float(est_HRmax)

#Tests whether or not the estimated heart rate is in target range between 65% and 85% which is desired range of heart rate
def in_target_range(hr, age):
    target_range_lower = 0.65*gellish2(age)
    target_range_upper = 0.85*gellish2(age)
    #Set range to test against hr 
    range_result = (target_range_lower < hr < target_range_upper)
    return range_result




