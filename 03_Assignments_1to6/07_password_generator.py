import random
import string

def password_generate(name: str, digit: int) -> str:
    if len(name) < 3:
        return "Error: Name must be at least 3 characters long."
    if digit < 3:
        return "Error: Password length must be at least 3 to include name part."

    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    password = []

    name_part = name[:3]
    password.append(name_part)

    # digit - 3 random characters add karo
    for _ in range(digit - 3):
        password.append(random.choice(characters))

    random.shuffle(password)

    return "".join(password)

# Input
name = input("Enter Your Name: ").strip()
digit = int(input("Enter the number of characters for your password: "))
print(password_generate(name, digit))
