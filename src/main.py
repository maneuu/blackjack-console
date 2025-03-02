import os
import time
from art import logo
from random import choice

def clear_screen():
    """Limpa o terminal, compatível com Windows e Unix."""
    os.system('cls' if os.name == 'nt' else 'clear')

def deal_card():
    """Retorna uma carta aleatória do baralho."""
    return choice([11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10])

def calculate_score(cards):
    """
    Calcula a pontuação total de uma mão.
    
    Ajusta o Ás (11) para 1 se a pontuação ultrapassar 21.
    Retorna 0 se a mão for um Blackjack (dois cartões somando 21).
    """
    score = sum(cards)
    if score == 21 and len(cards) == 2:
        return 0  # Blackjack
    # Ajusta o valor do Ás se necessário
    if 11 in cards and score > 21:
        cards[cards.index(11)] = 1  # Substitui apenas a primeira ocorrência
        score = sum(cards)
    return score

def animate_message(message, delay=1.0):
    """
    Exibe uma mensagem com efeito de animação.
    
    A mensagem é impressa caractere por caractere.
    """
    for char in message:
        print(char, end='', flush=True)
        time.sleep(delay / len(message))
    print()  # Pula linha após a mensagem

def play_game():
    # Limpa a tela e exibe o logo com uma mensagem de boas-vindas animada
    clear_screen()
    print(logo)
    animate_message("Bem-vindo ao Blackjack! Vamos começar a diversão...", delay=1.5)
    
    # Distribui as cartas iniciais para o jogador e o computador
    user_cards = [deal_card(), deal_card()]
    dealer_cards = [deal_card()]
    
    game_over = False
    while not game_over:
        user_score = calculate_score(user_cards)
        dealer_score = calculate_score(dealer_cards)
        
        print(f"\nSuas cartas: {user_cards}, pontuação atual: {user_score}")
        print(f"Carta visível do computador: {dealer_cards[0]}")
        
        # Verifica se o jogo deve encerrar
        if user_score == 0:
            animate_message("Você conseguiu um Blackjack!")
            game_over = True
        elif user_score > 21:
            animate_message("Ops! Você estourou!")
            game_over = True
        else:
            # Pergunta se o jogador deseja outra carta
            escolha = input("Deseja mais uma carta? (y para SIM, n para NÃO): ").lower()
            if escolha == 'y':
                animate_message("Pedindo mais uma carta...")
                time.sleep(0.5)
                user_cards.append(deal_card())
            else:
                game_over = True
    
    # Se o jogador não estourou, o computador compra cartas até alcançar 17 pontos ou mais
    if calculate_score(user_cards) <= 21:
        while calculate_score(dealer_cards) != 0 and calculate_score(dealer_cards) < 17:
            animate_message("O computador está comprando cartas...")
            time.sleep(0.5)
            dealer_cards.append(deal_card())
    
    user_score = calculate_score(user_cards)
    dealer_score = calculate_score(dealer_cards)
    
    print("\n===== Resultado Final =====")
    print(f"Suas cartas: {user_cards}, pontuação final: {user_score}")
    
    # Se o jogador estourou, não exibe as cartas do computador
    if user_score > 21:
        animate_message("Você estourou! Você perdeu 😭")
    else:
        print(f"Cartas do computador: {dealer_cards}, pontuação final: {dealer_score}")
        if dealer_score > 21:
            animate_message("O computador estourou! Você venceu 😃")
        elif dealer_score == user_score:
            animate_message("Empate!")
        elif dealer_score == 0:
            animate_message("O computador tem Blackjack! Você perdeu 😭")
        elif user_score == 0:
            animate_message("Você tem Blackjack! Você venceu 😃")
        elif user_score > dealer_score:
            animate_message("Você venceu! Parabéns 😃")
        else:
            animate_message("Você perdeu! Tente novamente 😭")
    
    # Pausa para o jogador ver o resultado antes de limpar a tela
    input("\nPressione Enter para continuar...")

# Loop principal do jogo com limpeza do terminal a cada nova partida
while True:
    if input("Você deseja jogar uma partida de Blackjack? (y para SIM, n para NÃO): ").lower() != 'y':
        print("Obrigado por jogar! Até a próxima!")
        break
    clear_screen()
    play_game()
