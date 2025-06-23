import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Check if user wants to start game
start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n':").lower()
if start_game == "y":
    print(art.logo)
    user_cards = []
    computer_cards = []

    # Computer and user draw 2 cards
    for drawn in range(2):
        user_cards.append(random.choice(cards))
        print(f"Test: user_cards: {user_cards}")
        computer_cards.append(random.choice(cards))
        print(f"Test: computer_cards: {computer_cards}")

    print(f"Your cards: {user_cards}, current score: {sum(user_cards)}\nComputer's first card: {computer_cards[0]}")

    if_pass = input("Type 'y' to get another card, type 'n' to pass:")
    if if_pass == "y":
        user_cards.append(random.choice(cards))
        print(f"Test: user_cards: {user_cards}")
        computer_cards.append(random.choice(cards))
        print(f"Test: computer_cards: {computer_cards}")
        print(f"Your cards: {user_cards}, current score: {sum(user_cards)}\nComputer's first card: {computer_cards[0]}")
