# Computer will think of a 3 digit number that has no repeating digits.
# You will then guess a 3 digit number. The computer will then give back clues
# Based on these clues you will guess again until you break the code with a match

# clues Close: guessed right number but in wrong position

# match : you guessed a correct number in the correct position

# nope: you haven't guessed any of the numbers correclty

import random

# Get guess    
def get_guess():
    return list(input("What is your guess: "))


# Generate computer code 123
def generate_code():
    digits = [str(num) for num in range(10)]

    # shuffle the digits
    # then grab the first 3
    random.shuffle(digits)
    return digits[:3]

# Generate the clues

def generate_clues(code,user_guess):
    if user_guess == code:
        return "CODE CRACKED!"
    clues = []

    for ind, num in enumerate(user_guess):
        if num == code[ind]:
            clues.append("Match")
        elif num in code:
            clues.append("Close")
        else:
            clues.append("Nope")
    return clues
    
    # if clues == []:
    #     return["Nope"]
    # else:
    #     return clues


# Run the game
print("Welcome Code Breaker!")

secret_code = generate_code()

clue_report = []

while clue_report != "CODE CRACKED!":
    guess = get_guess()

    clue_report = generate_clues( secret_code, guess)
    print("here is the reuslt of your guess: ")
    for clue in clue_report:
        print(clue)