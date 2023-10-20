# You are going to write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

# Important: You are not allowed to use the choice() function.

# Line 1 splits the string names_string into individual names and puts them inside a List called names. For this to work, you must enter all the names as names followed by comma then space. e.g. name, name, name

# NOTE: Don't worry about getting hold of the input(), we've done the work behind the scenes to import everything.

# HINT: Assume that names looks like this: input: x, y, z, names = ["x", "y", "z"]

# Example Input
# Angela, Ben, Jenny, Michael, Chloe
# Note: notice that there is a space between the comma and the next name.

# Example Output
# Michael is going to buy the meal today!
import random

names_string = "Angela, Ben, Jenny, Michael, Chloe"

names = names_string.split(", ")
# The code above converts the input into an array seperating
#each name in the input by a comma and space.
# 🚨 Don't change the code above 👆

number_of_names = len(names)
random_name_index = random.randint(0, number_of_names - 1)
random_name = names[random_name_index]

print(f"{random_name} is going to buy the meal today!")
