stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["lovebird", "cuddle", "whisper", "laptop"]

import random

chosen_word = random.choice(word_list)

# print(f"Computer has chosen {chosen_word}")

placeholder = "_"*len(chosen_word)
print("_"*len(chosen_word))
lives = 6
correct_letter = []
print("It's Hangman time! Save your husband from swinging by solving the puzzle—no pressure.")
print('''  Tianen: (╯°□°）╯︵ ┻━┻  (*screaming internally*)

  +---+
  |   |
      |
      |
      |
      |
=========
''')

while "_" in placeholder and lives>0:
    display = ""
    user_input = input("Guess a letter.\n").lower()
    if user_input not in correct_letter:
        correct_letter.append(user_input)
        if user_input in chosen_word:
            for letter in chosen_word:
                if letter == user_input:
                    display += letter
                elif letter in correct_letter:
                    display += letter
                else:
                    display += "_"
            print(f"\nYou guessed CORRECTLY!\n{display}\n{stages[lives]}")
            placeholder = display
        else:
            lives -= 1
            print(f"\nOops, you've made WRONG guess.\n{placeholder}\n{stages[lives]}")
    else:
        print("\nYou have guessed this letter already.")
        print(placeholder)

if lives == 0:
    print(f"Game Over, you LOSE...\nThe correct answer is {chosen_word}.")
else:
    print("Game Over. You WON!")
