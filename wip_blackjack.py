# Blackjack Game House Rules
# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def draw_card():
    user_cards.append(random.choice(cards))
    computer_cards.append(random.choice(cards))

def check_card():
    """Return the winner key"""
    # When user decides not to continue
    if if_pass == "n":
        # When computer score is below 17, it needs to draw card until it's above 17
        while sum(computer_cards) < 17:
            computer_cards.append(random.choice(cards))

        # Compare who's closer to 21.
        if 21 - sum(computer_cards) < 21 - sum(user_cards):
            return "You lose.😭"
        elif 21 - sum(computer_cards) > 21 - sum(user_cards):
            return "You win!🥳"

    # When user decides to continue - regular check
    if sum(user_cards) >21:
        return "You went over. You lose!🥺"
    elif sum(computer_cards) >21:
        return "Opponent went over. You win!😃"
    elif sum(user_cards) == 21:
        return "Blackjack! You win!🤑"
    elif sum(computer_cards) == 21:
        return "Opponent had blackjack! You lose...☠️"
    else:
        return f"Your cards: {user_cards}, current score: {sum(user_cards)}\nComputer's first card: {computer_cards[0]}"


# Check if user wants to start game
start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n':").lower()
# In case of unexpected input
while start_game != "y" and start_game != "n":
    start_game = input("Type 'y' or 'n':").lower()

# Start game
if start_game == "y":
    print(art.logo)
    user_cards = []
    computer_cards = []

    # Computer and user draw 2 cards to shart the game
    for drawn in range(2):
        draw_card()
        # print(f"Test: user_cards: {user_cards}")
        # print(f"Test: computer_cards: {computer_cards}")

    # Ask if user wants to continue
    print(f"Your cards: {user_cards}, current score: {sum(user_cards)}\nComputer's first card: {computer_cards[0]}")
    # In case of unexpected input
    if_pass = input("Type 'y' to get another card, type 'n' to pass:").lower()
    while if_pass != 'y' and if_pass != 'n':
        if_pass = input("Type 'y' or 'n':").lower()

    while if_pass == "y":
        draw_card()
        check_card()
        print(user_cards, computer_cards)
        print(check_card())

        if_pass = input("Type 'y' to get another card, type 'n' to pass:").lower()
        while if_pass != 'y' and if_pass != 'n':
            if_pass = input("Type 'y' or 'n':").lower()
else:
    print("Alright. Bye!")
