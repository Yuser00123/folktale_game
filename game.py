#guess the no. game

import random

gameRunning = True
num = random.randint(1, 1000);
ai_moves = []
turns = 0

def get_ai_num():
    num_by_ai = random.randint(1, 1000)
    return num_by_ai

print('Welcome to the number guessing game.')
while gameRunning == True:
    guessedNum = int(input('Guess the no. between 1 and 1000: '))
    ai_num = get_ai_num()
    while True:
        if ai_num in ai_moves:
            ai_num = get_ai_num()
        else:
            ai_moves.append(ai_num)
            break

    if ai_num == num:
        print(f"AI guessed the no. it was {num}")
        gameRunning = False
    else:
        print(f"AI chose {ai_num}.")


    
    if guessedNum > num:
        print('Try again. Hint: guessed number is greater than the actual number.')
        turns += 1
    elif guessedNum < num:
        print('Try again. Hint: guessed number is smaller than the actual number.')
        turns += 1
    else :
        print(f"Congratulations! You guessed the number. It was {num}. You took {turns} turns to guess the number.")
        gameRunning = False
        