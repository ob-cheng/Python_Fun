# import the libraries
import art
import random
import game_data

# Random select person's index
def select_person_index():
    """Return selected person index"""
    return random.randint(1,50)

# print selected person information
def person_information(person):
    """Return string information about person"""
    return f"{person['name']}, a {person['description']}, from {person['country']}."



# Ask user's guess
def user_guess():
    guess = input("How has more followers? Type 'A' or 'B':").lower()
    while guess not in ['a', 'b']:
        guess = input("Please type 'A' or 'B':").lower()
    return guess

# Judging the correct answer
def correct_answer():
    if person_A['follower_count'] > person_B['follower_count']:
        return 'a'
    elif person_A['follower_count'] < person_B['follower_count']:
        return 'b'

# Round transition
def transition():
    global SCORE
    global person_A
    global person_B
    if user_guess() == correct_answer():
        SCORE += 1
        person_A = person_B
        person_B = game_data.data[select_person_index()]
        print("\n"*100)
        print(f"{art.logo}\nYou're right! Current score: {SCORE}.")
    else:
        print("\n" * 100)
        print(f"{art.logo}\nSorry, that's wrong. Final score: {SCORE}.\n"
              f"{person_A['name']} has {person_A['follower_count']} followers, "
              f"while {person_B['name']} has {person_B['follower_count']} followers.")
        global GAME
        GAME = False


SCORE = 0
GAME = True
print(art.logo)
# Define person_A and person_B
person_A = game_data.data[select_person_index()]
person_B = game_data.data[select_person_index()]

while GAME:
    print(f"Compare A: {person_information(person_A)}\n{art.vs}\nAgainst B: {person_information(person_B)}")
    transition()
