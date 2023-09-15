import string
import random

letters_and_numbers = list(string.ascii_letters + string.digits)

all_characters = list(string.ascii_letters + string.digits + string.punctuation)

def generate_password():
    while True:
        characters = int(input("How many characters: "))

        if characters > 999:
            print("Too Long")
        else:
            break

    while True:
        check = input("Will your password contain symbols? yes/no: ").lower()
        if check == "yes":
            password = ''.join(random.choice(all_characters) for _ in range(characters))
            break
        elif check == "no":
            password = ''.join(random.choice(letters_and_numbers) for _ in range(characters))
            break
        else:
            print("You must enter 'yes' or 'no'.")

    return characters, password

characters, password = generate_password()
print(f"Your {characters} character password is: {password}")
