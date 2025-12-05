import random

print("Password Generator")

length = int(input("Enter password length: "))

password = ""

for i in range(length):
    number = random.randint(33, 126)  # ASCII range for symbols/numbers/letters
    password += chr(number)

print("Your password is:", password)
