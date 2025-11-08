# Exercise 3 - Guessing Game
# Program guesses a number between 1 and 1000

import random

low = 1
high = 1000
number = random.randint(low, high)
guess = None

print("I'm thinking of a number between 1 and 1000.")

while guess != number:
    guess = int(input("Enter your guess: "))
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("You guessed it!")
