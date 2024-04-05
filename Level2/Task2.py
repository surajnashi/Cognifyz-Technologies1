#Task2: Number Guesser
import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("=====================================")
    print("I have selected a random number between a specified range.")
    print("Try to guess it!")

    # Specify the range for the random number
    lower_bound = int(input("Enter the lower bound of the range: "))
    upper_bound = int(input("Enter the upper bound of the range: "))
    number = random.randint(lower_bound, upper_bound)

    while True:
        guess = int(input(f"Guess the number between {lower_bound} and {upper_bound}: "))
        if guess < number:
            print("Too low. Try again.")
        elif guess > number:
            print("Too high. Try again.")
        else:
            print(f"Congratulations! You guessed the number {number}.")
            break

if __name__ == "__main__":
    number_guessing_game()
