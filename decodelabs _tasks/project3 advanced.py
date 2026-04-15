import random
import string

def generate_password(length, use_letters, use_digits, use_symbols):
    characters = ""

    if use_letters:
        characters += string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += "@#$%&*!"

    if not characters:
        return "Error: No character set selected!"

    password = []

    # Ensure at least one character from each selected type
    if use_letters:
        password.append(random.choice(string.ascii_letters))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_symbols:
        password.append(random.choice("@#$%&*!"))

    # Fill remaining length
    for _ in range(length - len(password)):
        password.append(random.choice(characters))

    random.shuffle(password)
    return "".join(password)


def password_strength(password):
    strength = 0

    if any(c.islower() for c in password):
        strength += 1
    if any(c.isupper() for c in password):
        strength += 1
    if any(c.isdigit() for c in password):
        strength += 1
    if any(c in "@#$%&*!" for c in password):
        strength += 1

    if len(password) >= 12:
        strength += 1

    if strength <= 2:
        return "Weak"
    elif strength == 3 or strength == 4:
        return "Medium"
    else:
        return "Strong"


# ===== MAIN PROGRAM =====
print("=== Advanced Password Generator ===")

length = int(input("Enter password length: "))
num_passwords = int(input("How many passwords to generate? "))

use_letters = input("Include letters? (y/n): ").lower() == 'y'
use_digits = input("Include digits? (y/n): ").lower() == 'y'
use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

passwords = []

for i in range(num_passwords):
    pwd = generate_password(length, use_letters, use_digits, use_symbols)
    strength = password_strength(pwd)
    passwords.append((pwd, strength))

print("\nGenerated Passwords:")
for i, (pwd, strength) in enumerate(passwords, 1):
    print(f"{i}. {pwd}  --->  {strength}")

# Save option
save = input("\nDo you want to save passwords to file? (y/n): ").lower()

if save == 'y':
    with open("passwords.txt", "w") as file:
        for pwd, strength in passwords:
            file.write(f"{pwd} ---> {strength}\n")
    print("Passwords saved to passwords.txt")
