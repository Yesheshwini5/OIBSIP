import random
import string
def generate_password(length, use_uppercase, use_lowercase, use_numbers, use_symbols):
    """Generate a random password based on the selected character types."""

    character_sets = []

    if use_uppercase:
        character_sets.append(string.ascii_uppercase)

    if use_lowercase:
        character_sets.append(string.ascii_lowercase)

    if use_numbers:
        character_sets.append(string.digits)

    if use_symbols:
        character_sets.append(string.punctuation)

    
    password = []

    for character_set in character_sets:
        password.append(random.choice(character_set))

   
    all_characters = "".join(character_sets)

   
    while len(password) < length:
        password.append(random.choice(all_characters))

     
    random.shuffle(password)

    return "".join(password)


def get_yes_no(prompt):
    """Get a valid yes/no answer from the user."""

    while True:
        answer = input(prompt).strip().lower()

        if answer in ("y", "yes"):
            return True
        elif answer in ("n", "no"):
            return False
        else:
            print("Please enter yes or no.")


def main():
    print("=" * 40)
    print("      RANDOM PASSWORD GENERATOR")
    print("=" * 40)

    while True:

        
        while True:
            try:
                length = int(input("Enter password length (minimum 8): "))

                if length < 8:
                    print("Password length must be at least 8.")
                else:
                    break

            except ValueError:
                print("Please enter a valid number.")

        print("\nChoose character types:")
        print("1. Uppercase letters (A-Z)")
        print("2. Lowercase letters (a-z)")
        print("3. Numbers (0-9)")
        print("4. Symbols (!@#$...)")

        # Get character type choices
        use_uppercase = get_yes_no("Include uppercase letters? (yes/no): ")
        use_lowercase = get_yes_no("Include lowercase letters? (yes/no): ")
        use_numbers = get_yes_no("Include numbers? (yes/no): ")
        use_symbols = get_yes_no("Include symbols? (yes/no): ")

        selected_types = sum([
            use_uppercase,
            use_lowercase,
            use_numbers,
            use_symbols
        ])

        
        if selected_types < 2:
            print("\nError: Please select at least 2 character types.")
            print("Let's try again.\n")
            continue

        
        password = generate_password(
            length,
            use_uppercase,
            use_lowercase,
            use_numbers,
            use_symbols
        )

        print("\n" + "=" * 40)
        print("Generated Password:")
        print(password)
        print("=" * 40)

        
        again = get_yes_no("\nGenerate another password? (yes/no): ")

        if not again:
            print("\nThank you for using the Password Generator!")
            break


if __name__ == "__main__":
    main()

