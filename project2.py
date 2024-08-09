# number guessing game

import random as rand

compVal = rand.randint(1,100)

print("Number guessing game: ")

n = 101

guess = 0

while(n != compVal):
    guess += 1

    n = int(input("Enter the number: "))

    if(n>compVal):
        print("Lower number please")

    elif(n<compVal):
        print("Higher number please")

print(f"You guessed the number in {guess} no. of steps")


