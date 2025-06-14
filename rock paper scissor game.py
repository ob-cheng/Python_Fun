rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

user_choice = int(input("Hey! Welcome to the rock paper scissor game!\n"
                    "What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors."))

computer_choice = random.choice([0, 1, 2])

choices = [rock, paper, scissors]

print(f"You chose:\n{choices[user_choice]}\nComputer chose:\n{choices[computer_choice]}")

if user_choice == computer_choice:
    print("Tie!")
elif computer_choice == 0 or user_choice == 0:
    if computer_choice == 2:
        print("You won!")
    else: print("You lose.")
elif user_choice > computer_choice:
    print("You won!")
else:print("You lose.")
