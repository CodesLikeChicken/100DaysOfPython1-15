#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator.")
total_bill = input("What was the total bill? ")
tip_percent = input(
    "What percentage tip would you like ot give? 10, 12, or 15? ")
split_size = input("How many people to split the bill? ")

tip_percent = float(tip_percent) / 100
total_bill = float(total_bill) * (1 + tip_percent) / int(split_size)

print(f"Each person should pay ${total_bill:.2f}.")
