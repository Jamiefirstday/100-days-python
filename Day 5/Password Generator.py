#Password Generator Project

#import module
import random

#content
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#generator start
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#pick random char and combine to a list
password_list = []
for char in range(1, nr_letters + 1):
  password_list += random.choice(letters)
for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)
for char in range(1, nr_symbols + 1):
  password_list += random.choice(numbers)

#suffle the list
random.shuffle(password_list)

#chage the list to string with loop method
password = ""
for char in password_list:
  password += char

#print the result
print(f"Your password could be {password}")