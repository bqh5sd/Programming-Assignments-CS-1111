player = input("What player would you like to calculate statistics for? ")
opponent = input("What team was the opponent in the game you would like to calculate statistics for? ")
three_attempted = int(input("How many 3's did this player attempt? "))
three_made = int(input("How many 3's did this player made? "))
two_attempted = int(input("How many 2's did this player attempt? " ))
two_made = int(input("How many 2's did this player made? " ))
Free_T = int(input("How many free throws did the player attempt? "))
Free_TM = int(input("How many free throws did this player made? "))
field_goal = (three_made + two_made)/(three_attempted + two_attempted)*100
free_throw = (Free_TM/Free_T)*100
total_points = (three_made*3 + two_made*2 + Free_TM)
print(player + " had a " + str(field_goal) + "% field goal percentage and a " + str(free_throw) + "% free throw percentage")
print(player + " scored " + str(total_points) + " points against " + opponent + ". Wahoowa!")
