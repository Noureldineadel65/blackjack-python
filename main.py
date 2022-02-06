# Game Rules:
# 1 add up your cards to the highest possible without going over 21
# 2 cards from 2 to 10 add to the same value
# 3 jack, queen, and king each count as 10
# 4 ace can be 1 or 11 (you decide)
# 5 if your score equals their score
import random
import os
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""


def get_random_el(provided_list):
    return provided_list[random.randint(0, len(provided_list) - 1)]

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Queen", "King", "Jack", "Ace"]
your_score = 0
computer_score = 0
turn = "user"
continue_game = True


def ace(score):
    if (score + 11) / 21 > (score + 1) / 21 and score + 11 <= 21:
        return 11
    else:
        return 1


def ace_algorithm():
    if turn == "user":
        return ace(your_score)
    else:
        return ace(computer_score)


special_cards = {
    "Queen": 10,
    "King": 10,
    "Jack": 10,
    "Ace": ace_algorithm()
}


def get_random_card():
    card = get_random_el(cards)
    card_inst = {}
    if type(card) == str:
        card_inst[card] = special_cards[card]
    else:
        card_inst[str(card)] = card
    return card_inst


def get_value_of_card(card):
    return list(card.keys())[0]


def add_cards_up(card):
    score = 0

    if card in special_cards.keys():
        score += special_cards[card]
    else:
        score += int(card)
    return score


while continue_game:
    print(logo)
    your_score = 0
    computer_score = 0
    start_cards = [get_value_of_card(get_random_card()), get_value_of_card(get_random_card())]
    for i in start_cards:
        your_score += add_cards_up(i)
    print(f"Your cards: {str(start_cards)}, current score: {your_score}")
    turn = "computer"
    computer_card = get_random_card()
    computer_second_card = get_random_card()
    for i in [get_value_of_card(computer_card), get_value_of_card(computer_second_card)]:
        computer_score += add_cards_up(i)
    print(f"Computer's first card: {get_value_of_card(computer_card)}")

    while your_score < 21 and computer_score < 21:
        another_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if another_card == "y":
            turn = "user"
            another_user_card = get_random_card()
            start_cards.append(get_value_of_card(another_user_card))
            your_score += add_cards_up(get_value_of_card(another_user_card))
            print(f"Your cards: {str(start_cards)}, current score: {your_score}")
        else:
            break

    print(f"Your final hand: {str(start_cards)}, final score: {your_score}")
    print(
        f"Computer's final hand: {str([get_value_of_card(computer_card), get_value_of_card(computer_second_card)])}, final score: {computer_score}")
    if your_score > 21:
        print("Its a BUST. You lose.")
    elif your_score == 21 or (computer_score < 21 and your_score > computer_score):
        print("You WINNN")
    elif computer_score == 21 or computer_score > your_score:
        print("You Lose. Computer Wins.")
    elif computer_score == your_score:
        print("ITS A TIE")

    if input("Do you want to play again? Type 'y' for yes. 'n' for no: ") == 'n':
        continue_game = False
    os.system("cls")