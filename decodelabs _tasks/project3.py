import random
import string

# Ask user for password length
length = int(input("Enter password length: "))

# Combine letters and digits
characters = string.ascii_letters + string.digits

# Generate password
password = ""
for i in range(length):
    password += random.choice(characters)

print("Generated Password:", password)
