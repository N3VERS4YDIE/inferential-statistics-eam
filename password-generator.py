import random
import string


def generate_password(letters=0, numbers=0, specials=0) -> str:
    lower_chars = random.choices(string.ascii_lowercase, k=letters // 2)
    upper_chars = random.choices(string.ascii_uppercase, k=letters - letters // 2)
    number_chars = random.choices(string.digits, k=numbers)
    special_chars = random.choices(string.punctuation, k=specials)

    chars = lower_chars + upper_chars + number_chars + special_chars
    random.shuffle(chars)
    return "".join(chars)


if __name__ == "__main__":
    print("--- Welcome to the Password Generator 3000! ---\n")

    char_counts = {"letters": 0, "numbers": 0, "specials": 0}

    for key in char_counts:
        while True:
            count = input(f"How many {key} do you want to include? ")

            if count.isdigit() and int(count) >= 0:
                char_counts[key] = int(count)
                break

            print("Please enter a valid number.\n")

    password = generate_password(**char_counts)
    print(f"Generated password: {password}")
