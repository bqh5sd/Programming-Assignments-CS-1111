

def fine(speed_limit, my_speed, zone = "None"):
    amount_due = 0
    speed_limit_difference = my_speed - speed_limit
    if speed_limit_difference > 0 and speed_limit_difference < 20:
        if zone != "residential":
            amount_due = speed_limit_difference*7
        elif "residential" in zone:
            amount_due = (speed_limit_difference*8)+200
        else:
            amount_due = speed_limit_difference*6
    else:
        if speed_limit_difference >= 20:
            amount_due += 350
        elif speed_limit_difference <= -10:
            amount_due += 30
    return amount_due


def demerits(speed_limit, my_speed):
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

