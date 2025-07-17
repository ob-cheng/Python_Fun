import art
import random
import game_data

def select_person_index():
    return random.randint(0, len(game_data.data) - 1)

def person_information(person):
    return f"{person['name']}, a {person['description']}, from {person['country']}."

def user_guess():
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    while guess not in ['a', 'b']:
        guess = input("Please type 'A' or 'B': ").lower()
    return guess

def correct_answer(person_A, person_B):
    return 'a' if person_A['follower_count'] > person_B['follower_count'] else 'b'

def transition(person_A, person_B, score):
    guess = user_guess()
    answer = correct_answer(person_A, person_B)

    if guess == answer:
        score += 1
        person_A = person_B
        person_B = game_data.data[select_person_index()]
        print("\n" * 100)
        print(f"{art.logo}\nYou're right! Current score: {score}.")
        return person_A, person_B, score, True
    else:
        print("\n" * 100)
        print(f"{art.logo}\nSorry, that's wrong. Final score: {score}.\n"
              f"{person_A['name']} has {person_A['follower_count']}M followers, "
              f"while {person_B['name']} has {person_B['follower_count']}M followers.")
        return person_A, person_B, score, False

# --- Game Starts Here ---
print(art.logo)
score = 0
game_on = True

person_A = game_data.data[select_person_index()]
person_B = game_data.data[select_person_index()]

while game_on:
    print(f"Compare A: {person_information(person_A)}\n{art.vs}\nAgainst B: {person_information(person_B)}")
    person_A, person_B, score, game_on = transition(person_A, person_B, score)
