""" Asking user to input name and age and thereafter displaying
them the year when they will grow to 100"""

name = input("Enter your name")
age = int(input("Enter your age"))
year_turn_100 = (2022 - age) + 100
print(name, " will turn 100 in the year: ", year_turn_100)

