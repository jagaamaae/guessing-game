"""A number-guessing game."""

# Put your code here


import random

def first_exercise():
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

player=input("Howdy. What is your name?")
print (f"\n{player} I'm thinking of a number between 1 and 5.Try to guess my number")
random_number=random.randrange(1, 6)
guess=0
answer = "Y"
best_score = 100000000
while answer == "Y":
    input_number=int(input("\nYour guess: "))
    guess+=1
    if input_number <random_number:
        print ("\nGuess again. The number is too low.")
    elif input_number>random_number:
        print ("\nGuess again. The number is too high")
    else:
        answer = input(f"\nWell done {player}. You found the number in {guess} tries. Do you want to play another round? Y/N")
        if guess < best_score:
            best_score = guess
        guess=0
        random_number=random.randrange(1, 6)
    if guess>5 and random_number != input_number:
        answer = input(f"\nToo many tries.  Do you want to play another round? Y/N")
        guess=0
        random_number=random.randrange(1, 6)
if best_score < 10000000:
    print(f"Thanks for playing! Your best score was {best_score}.")
else:
    print("Thank for playing! Better luck next time with that guessing.")



