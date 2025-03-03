import os
import time
from art import logo
from random import choice

def clear_screen():
    """Limpa o terminal de forma compatível."""
    os.system('cls' if os.name == 'nt' else 'clear')

def deal_card():
    """Retorna uma carta aleatória do baralho."""
    return choice([11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10])

def calculate_score(cards):
    """Calcula a pontuação com tratamento para Ases."""
    score = sum(cards)
    if score == 21 and len(cards) == 2:
        return 0  # Blackjack
    if 11 in cards and score > 21:
        cards[cards.index(11)] = 1
        score = sum(cards)
    return score

def animate_message(message, delay=0.4):
    """Exibe uma mensagem com efeito de animação mais fluida."""
    for char in message:
        print(char, end='', flush=True)
        time.sleep(delay / len(message))
    print()

def play_game():
    """Executa uma partida completa de Blackjack."""
    clear_screen()
    print(logo)
    print("\n" + "=" * 40 + "\n")
    
    user_cards = [deal_card(), deal_card()]
    dealer_cards = [deal_card()]
    user_score = 0

    while True:
        user_score = calculate_score(user_cards)
        dealer_score = calculate_score(dealer_cards)
        
        animate_message(f"▶ Suas cartas: {user_cards} | Pontuação: {user_score}")
        animate_message(f"▼ Carta visível do computador: {dealer_cards[0]}\n")

        if user_score == 0:
            animate_message("★ BLACKJACK! Você ganhou automaticamente! ★", 0.8)
            break
        
        if user_score > 21:
            break
            
        escolha = input("▼ Pressione Enter para mais uma carta ou qualquer tecla para parar: ")
        if escolha == "":
            user_cards.append(deal_card())
            animate_message("▼ Adicionando nova carta...", 0.3)
        else:
            break

    # Lógica do dealer
    if user_score <= 21:
        while calculate_score(dealer_cards) < 17 and calculate_score(dealer_cards) != 0:
            animate_message("▼ Computador está comprando cartas...", 0.3)
            dealer_cards.append(deal_card())

    # Resultado final
    user_score = calculate_score(user_cards)
    dealer_score = calculate_score(dealer_cards)
    
    print("\n" + "=" * 40)
    animate_message(f"▶ Suas cartas: {user_cards} | Pontuação Final: {user_score}")
    animate_message(f"▼ Cartas do Computador: {dealer_cards} | Pontuação Final: {dealer_score}\n")

    # Determinar resultado
    if user_score > 21:
        result = 'dealer'
        animate_message("✖ Você estourou! Derrota!", 0.6)
    elif dealer_score > 21 or user_score == 0:
        result = 'user'
        animate_message("✔ Vitória! Você venceu!", 0.6)
    elif dealer_score == 0 or dealer_score > user_score:
        result = 'dealer'
        animate_message("✖ O computador venceu!", 0.6)
    elif user_score == dealer_score:
        result = 'empate'
        animate_message("➖ Empate!", 0.6)
    else:
        result = 'user'
        animate_message("✔ Você tem a maior pontuação!", 0.6)

    input("\n▼ Pressione Enter para continuar...")
    return result

# Configuração inicial
clear_screen()
print(logo)
animate_message("★ Bem-vindo ao Blackjack! ★", 0.8)

# Contadores de vitórias
user_wins = 0
dealer_wins = 0

# Loop principal
while True:
    user_choice = input("\n▼ Pressione Enter para jogar ou qualquer tecla para sair: ")
    if user_choice != "":
        clear_screen()
        animate_message(f"\n★ Placar Final ★\nJogador: {user_wins}\nComputador: {dealer_wins}")
        animate_message("\nObrigado por jogar! Até a próxima!\n")
        break
    
    result = play_game()
    
    if result == 'user':
        user_wins += 1
    elif result == 'dealer':
        dealer_wins += 1
        
    print(f"\n★ Placar Atual ★\nJogador: {user_wins}\nComputador: {dealer_wins}\n")
