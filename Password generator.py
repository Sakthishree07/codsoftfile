import random
import string

def generate_password(length=12):
    """Generate a random password."""
    if length < 4:  # Ensure the password length is reasonable
        raise ValueError("Password length should be at least 4")

    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    punctuation = string.punctuation

    # Ensure the password contains at least one character from each character set
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(punctuation)
    ]

    # Fill the rest of the password length with random characters from all sets
    all_characters = lowercase + uppercase + digits + punctuation
    password += random.choices(all_characters, k=length-4)

    # Shuffle the generated password list to ensure randomness
    random.shuffle(password)

    # Join the list to form the final password string
    return ''.join(password)

if __name__ == "__main__":
    try:
        password_length = int(input("Enter the desired password length: "))
        print(f"Generated password: {generate_password(password_length)}")
    except ValueError as e:
        print(f"Error: {e}")
