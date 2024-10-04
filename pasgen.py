import random
import string

def generate_password(length):
    # Define the characters you want to include in the password
    letters = string.ascii_letters  # Includes both uppercase and lowercase letters
    digits = string.digits          # Numbers 0-9
    symbols = string.punctuation    # Special characters (!, @, #, etc.)

    # Combine all character sets
    all_characters = letters + digits + symbols

    # Generate a password by randomly choosing characters
    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password

while True:
    # Get the desired password length from the user
    password_length = input("Enter the password length (or type 'exit' to quit): ")

    # Allow the user to exit the loop
    if password_length.lower() == 'exit':
        print("Exiting password generator...")
        break  # Exits the while loop

    # Check if the input is a valid number
    if password_length.isdigit():
        password_length = int(password_length)
        # Generate and display the password
        password = generate_password(password_length)
        print(f"Your generated password is: {password}")
    else:
        print("Please enter a valid number or type 'exit' to quit.")
