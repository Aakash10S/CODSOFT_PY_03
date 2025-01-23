import random
import string

def generate_password(length, use_uppercase=True, use_numbers=True, use_special_chars=True):
    if length < 1:
        raise ValueError("Password length must be at least 1.")

    # Define character pools
    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase if use_uppercase else ''
    number_chars = string.digits if use_numbers else ''
    special_chars = string.punctuation if use_special_chars else ''

    # Combine all selected pools
    all_chars = lowercase_chars + uppercase_chars + number_chars + special_chars

    if not all_chars:
        raise ValueError("No character sets selected to generate a password.")

    # Generate random password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")

    try:
        length = int(input("Enter the desired password length: "))
        if length < 1:
            print("Password length must be a positive integer.")
            return

        use_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
        use_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
        use_special_chars = input("Include special characters? (y/n): ").strip().lower() == 'y'

        password = generate_password(length, use_uppercase, use_numbers, use_special_chars)
        print(f"Generated Password: {password}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
