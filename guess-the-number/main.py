import random

max_number = int(input("Please enter the maximum number: "))
guessing_number = random.randint(1, max_number)

while True:
    user_number = input(f"Please enter a number between 1 and {max_number} or type e to exit the game: ")
    if user_number.lower() == "e":
        print("You have exited the game.")
        break

    user_number = int(user_number)
    if user_number == guessing_number:
        print("You have guessed the correct number.")
        break
    elif user_number > guessing_number:
        print("Your number is bigger")

    elif user_number < guessing_number:
        print("Your number is smaller.")

    else:
        print("Please enter a valid number.")
        continue
