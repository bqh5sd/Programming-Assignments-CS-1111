def gellish2(age):
    est_HRmax = 191.5 - (0.007*age**2)
    return float(est_HRmax)

def in_target_range(hr, age):
    target_range_lower = 0.65*gellish2(age)
    target_range_upper = 0.85*gellish2(age)
    range_result = (target_range_lower < hr < target_range_upper)
    return range_result
