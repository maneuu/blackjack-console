cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
from art import logo
from random import choice

while True:

    jogar = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if jogar.lower() == "n":
        break
    print(logo)

    user_cards = []
    dealer_cards = []
    for _ in range(2):
        user = choice(cards)
        cards.remove(user)
        user_cards.append(user)

    dealer = choice(cards)
    cards.remove(dealer)
    dealer_cards.append(dealer)

    

    perdeu = False
    empate = False
    while True:
        print(f"\tYour cards: {user_cards}, current score: {sum(user_cards)}")
        print(f"\tComputer's first card: {dealer_cards}")
        more_cards = input("Type 'y' to get another card, type 'n' to pass:")
        if more_cards.lower() == "y":
            user = choice(cards)
            cards.remove(user)
            user_cards.append(user)

        else:
            break
        if sum(user_cards) > 21:
            perdeu = True
            break 

        
    print(f"\tYour cards: {user_cards}, current score: {sum(user_cards)}")
    print(f"\tComputer's first card: {dealer_cards}")

    if perdeu: 
        print(f"\tYour final hand:{user_cards}, final score: {sum(user_cards)}")
        print(f"\tComputer's final hand: {dealer_cards}, final score: {sum(dealer_cards)}")
        print("You went over. You lose 😭")
   
    while True:
        dealer = choice(cards)
        cards.remove(dealer)
        dealer_cards.append(dealer)
        if sum(dealer_cards) >= 17:
            break
    if sum(dealer_cards) > 21:
        perdeu = False
    elif sum(dealer_cards) == sum(user_cards):
        empate = True
    else:
        if sum(dealer_cards) > sum(user_cards):
            perdeu = True
        
    print(f"\tYour final hand:{user_cards}, final score: {sum(user_cards)}")
    print(f"\tComputer's final hand: {dealer_cards}, final score: {sum(dealer_cards)}")

    if empate:
        print("Draw")
    elif perdeu:
        print("You lose")
    else:
        print("You won")
