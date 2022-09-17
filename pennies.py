# Omid Akbari
# bqh5sd
# This is your starter code for At-Home Coding Exercise 1
# file must be named pennies.py
# The purpose is to write a function that returns the number of pennies (cents) required for change

# Write the num_pennies function here, including docstring:

def num_pennies (cost,paid):
    """"
    This function will find the reminder of pennies needed to give change to customer
    given the price of the item and how much they have paid up front

    parameters:
        cost {int}
        paid {int}

    Returns:
        the difference in the cost vs paid and then taking the module for each currency type
    """
    change_difference_in_pennies = abs((float(cost) - float(paid)))*100
    check_for_dollar_bill = change_difference_in_pennies%100
    check_for_quarters = check_for_dollar_bill%25
    check_for_nickles = check_for_quarters%5
    total_pennies = round(check_for_nickles)
    return str(total_pennies)




# main program
# DO NOT EDIT anything after this point
print("This program will calculate the number of pennies required for change.")
itemCost = input("Enter the cost of the item: ")
amtPaid = input("Enter the amount paid: ")
pennies = num_pennies(itemCost, amtPaid)
print("If you paid $" + amtPaid + " for something that costs $" + itemCost + " you will need " + pennies + " pennies." )
