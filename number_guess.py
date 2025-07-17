# import art
import random

# print(art.logo)

def greeting():
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

def choose_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    while difficulty != 'easy' and difficulty != 'hard':
        difficulty =input("Unrecognized input. Choose a difficulty. Type 'easy' or 'hard': ").lower()
    return difficulty

def pick_number():
    number = random.randint(1, 100)
    return number

def attempt_amount():
    if DIFFICULTY == 'easy':
        return 10
    elif DIFFICULTY == 'hard':
        return 5

def user_input():
    input_text = input(f"You have {ATTEMPTS} attempts remaining to guess the number.\nMake a guess: ")
    while input_text.isalpha():
        input_text = input("Give me a number between 1 and 100. A letter or text won't be accepted: ")
    return int(input_text)


greeting()
DIFFICULTY = choose_difficulty()
NUMBER = pick_number()
ATTEMPTS = attempt_amount()


# print(DIFFICULTY)
# print(NUMBER)
# print(ATTEMPTS)


USER_INPUT = 0

# print(type(NUMBER))
# print(type(USER_INPUT))

while ATTEMPTS > 0:
    if USER_INPUT == 0:
        USER_INPUT = user_input()
        ATTEMPTS -= 1
        # print(USER_INPUT)
        # print(NUMBER)
        # print(ATTEMPTS)
    if ATTEMPTS >= 0:
        if USER_INPUT > NUMBER:
            print("Your guess is too high.")
            USER_INPUT = user_input()
            ATTEMPTS -= 1
            # print(USER_INPUT)
            # print(NUMBER)
            # print(ATTEMPTS)
        elif USER_INPUT < NUMBER:
            print("Your guess is too low.")
            USER_INPUT = user_input()
            ATTEMPTS -= 1
            # print(USER_INPUT)
            # print(NUMBER)
            # print(ATTEMPTS)
        elif USER_INPUT == NUMBER:
            print("Congratulations, you guessed the number!")
            ATTEMPTS = -1
            # print(USER_INPUT)
            # print(NUMBER)
            # print(ATTEMPTS)

print("You've run out of guesses. The number was: " + str(NUMBER))
ATTEMPTS = -1
