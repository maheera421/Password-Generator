import data
import random

print(data.logo)
print("Welcome to the Password Generator!\n")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_list = []

for char in range(1, nr_letters + 1):
  password_list.append(random.choice(data.letters))

for char in range(1, nr_symbols + 1):
  password_list += random.choice(data.symbols)

for char in range(1, nr_numbers + 1):
  password_list += random.choice(data.numbers)

# print(password_list)
random.shuffle(password_list)
# print(password_list)

password = ""
for char in password_list:
  password += char

print(f"\nYour password is: {password}")