#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password = []

# Generate random letters
number_of_letters = len(letters)
for _ in range(nr_letters):
    index = random.randint(0, number_of_letters - 1)
    password.append(letters[index])

# Generate random numbers
number_of_numbers = len(numbers)
for _ in range(nr_numbers):
    index = random.randint(0, number_of_numbers - 1)
    password.append(numbers[index])

# Generate random symbols
number_of_symbols = len(symbols)
for _ in range(nr_numbers):
    index = random.randint(0, number_of_symbols - 1)
    password.append(symbols[index])

# Randomize order
password_length = len(password)
for index in range(password_length):
    swap_index = random.randint(0, password_length - 1)
    if not swap_index == index:
        temp = password[index]
        password[index] = password[swap_index]
        password[swap_index] = temp

print(''.join(password))