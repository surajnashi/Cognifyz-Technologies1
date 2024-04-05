#Task1: Guessing Game
import random

def guess_the_number():
    number = random.randint(1, 100)
    print("Guess the number between 1 and 100.")

    while True:
        guess = int(input("Enter your guess: "))
        if guess < number:
            print("Too low. Try again.")
        elif guess > number:
            print("Too high. Try again.")
        else:
            print(f"Congratulations! You guessed the number {number}.")
            break

if __name__ == "__main__":
    guess_the_number()

