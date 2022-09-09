number = int(input("Pick a number between 1 and 10: "))
year_born0 = int(input("If you've already had a birthday this year, enter 1772. Otherwise, enter 1771: "))
new_number = (number*2 + 5)*50

def subtract(born):
    year_born1 = int(input("Enter the year that you were born: "))
    i = born-year_born1
    i_converted = str(i)
    print("The magic number is \"" + i_converted + "\". That means you are " + i_converted[1:3] + "!")


if year_born0 == 1772:
    new_number += 1772
    subtract(new_number)
else:
    new_number += 1771
    subtract(new_number)





