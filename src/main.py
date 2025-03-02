from art import logo
from random import choice

def deal_card():
    """Retorna uma carta aleatória do baralho."""
    return choice([11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10])

def calculate_score(cards):
    """Retorna a soma das cartas e ajusta o Ás (11) para 1 se necessário."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Blackjack
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def play_game():
    print(logo)
    user_cards = [deal_card(), deal_card()]
    dealer_cards = [deal_card()]

    game_over = False
    while not game_over:
        user_score = calculate_score(user_cards)
        dealer_score = calculate_score(dealer_cards)
        print(f"\tYour cards: {user_cards}, current score: {user_score}")
        print(f"\tComputer's first card: {dealer_cards[0]}")
        
        if user_score == 0 or dealer_score == 0 or user_score > 21:
            game_over = True
        else:
            if input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
                user_cards.append(deal_card())
            else:
                game_over = True

    while calculate_score(dealer_cards) < 17:
        dealer_cards.append(deal_card())

    user_score = calculate_score(user_cards)
    dealer_score = calculate_score(dealer_cards)
    print(f"\tYour final hand: {user_cards}, final score: {user_score}")
    print(f"\tComputer's final hand: {dealer_cards}, final score: {dealer_score}")

    if user_score > 21:
        print("You went over. You lose 😭")
    elif dealer_score > 21:
        print("Opponent went over. You win! 😃")
    elif user_score == dealer_score:
        print("Draw")
    elif user_score == 0:
        print("Blackjack! You win! 😃")
    elif dealer_score == 0:
        print("Opponent got Blackjack! You lose 😭")
    elif user_score > dealer_score:
        print("You won! 😃")
    else:
        print("You lose 😭")

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    play_game()
