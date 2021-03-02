"""A number-guessing game."""

# Put your code here

import random
player=input("Howdy. What is your name?")
print (f"\n{player} I'm thinking of a number between 1 and 100.Try to guess my number")
random_number=random.randrange(1, 101)
guess=0
while True:
    input_number=int(input("\nYour guess: "))
    guess+=1
    if input_number <random_number:
        print ("\nGuess again. The number is too low.")
    elif input_number>random_number:
        print ("\nGuess again. The number is too high")
    else:
        print(f"\nWell done {player}. You found the number in {guess} tries")
        break
