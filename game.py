#guess the no. game

import random

gameRunning = True
num = random.randint(1, 1000);

print('Welcome to the number guessing game.')
while gameRunning == True:
    guessedNum = int(input('Guess the no. between 1 and 1000: '))
    if guessedNum > num:
        print('Try again. Hint: guessed number is greater than the actual number.')
    elif guessedNum < num:
        print('Try again. Hint: guessed number is smaller than the actual number.')
    else :
        print(f"Congratulations! You guessed the number. It was {num}.")
        gameRunning = False