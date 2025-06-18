import random
import string

def generate_password(length=12, use_digits=True, use_symbols=True):
    # Basic character sets
    letters = string.ascii_letters  # a-zA-Z
    digits = string.digits          # 0-9
    symbols = string.punctuation    # Special characters

    # Build character pool based on options
    characters = letters
    if use_digits:
        characters += digits
    if use_symbols:
        characters += symbols

    if not characters:
        return "Error: No characters to choose from."

    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("🔐 Password Generator")

    try:
        length = int(input("Enter desired password length (e.g. 12): "))
        use_digits = input("Include digits? (y/n): ").lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

        password = generate_password(length, use_digits, use_symbols)
        print("\nGenerated password:", password)

    except ValueError:
        print("Invalid input. Please enter numeric values for length.")

if __name__ == "__main__":
    main()
