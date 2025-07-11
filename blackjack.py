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

# logo = r"""
# .------.            _     _            _    _            _    
# |A_  _ |.          | |   | |          | |  (_)          | |   
# |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
# | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
# |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
# `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
#       |  \/ K|                            _/ |                
#       `------'                           |__/           
# """

import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    return random.choice(cards)


def calculate_score(card_list):
    if sum(card_list) == 21:
        return 0
    elif sum(card_list) > 21 and 11 in card_list:
        card_list.remove(11)
        card_list.append(1)
        return sum(card_list)
    else:
        return sum(card_list)


def compare():
    if computer_score == user_score:
        return "It's a draw! 🤝 Nobody wins this round.\n"
    elif computer_score == 0:
        return "Dealer hits Blackjack! 🃏💥 Better luck next time.\n"
    elif user_score == 0:
        return "Blackjack! 🃏🎉 You hit 21 right away!\n"
    elif user_score > 21:
        return "You lose! 💔 The dealer takes this round.\n"
    elif computer_score > 21:
        return "You win! 🥳💰 Great job beating the dealer!\n"
    else:
        if computer_score > user_score:
            return "You lose! 💔 The dealer takes this round.\n"
        else:
            return "You win! 🥳💰 Great job beating the dealer!\n"

def notification():
    print(f"Your cards: {user_card}, current score: {user_score}\n"
          f"Computer's first card: {computer_card[0]}\n"
          # f"DEV MODE: {user_card} {computer_card}\n"
    )

def game_over():
    print(f"Your final hand: {user_card}, final score: {user_score}\n"
          f"Computer's final hand: {computer_card}, final score: {computer_score}\n")

continue_game = "y"

while continue_game == "y":
    print("\n"*100)
    print(art.logo)

    user_card = []
    computer_card = []

    for deal in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())

    draw_card = "y"
    while draw_card == "y":
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)
        notification()
        if user_score == 0 or computer_score == 0 or user_score > 21 or computer_score > 21:
            draw_card = "n"
            game_over()
            print(compare())
            continue_game = input("Do you want to restart game? [y/n]").lower()
            while continue_game != "y" and continue_game != "n":
                continue_game = input("Do you want to restart game? Please enter y or n. [y/n]").lower()
        else:
            draw_card = input("Do you want to draw another card? [y/n]").lower()
            while draw_card != "y" and draw_card != "n":
                draw_card = input("Do you want to draw another card? Please enter y or n.[y/n]").lower()
            if draw_card == "y":
                user_card.append(deal_card())
                computer_card.append(deal_card())
            else:
                while computer_score < 17:                         
                    computer_card.append(deal_card())              
                    computer_score = calculate_score(computer_card)
                game_over()
                print(compare())
                continue_game = input("Do you want to restart game? [y/n]").lower()

