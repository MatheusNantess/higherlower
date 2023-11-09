from black_art import logo
should_continue = True
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
import random
#obs: all this inside a loop
#Step 1 -ask player input if he want to play black jack  

#step 2 - condicional if answer == 'yes', than show the logo and beggin the game (try to clear the terminal)

#step 3 - player beggins with two cards from the list choose randomly and show the sum of them as current score.
#outro: shows computer's card aswell but only one from the list (choose randomly)

#step 4 - ask players input if they want to take in another card or if they want to pass to the computer.
#outro: if you type 'no' it will be revealed the other computer's card (and compare the sums of the cards).
#outro2: whoever gets closer to 21 as current score wins

#step 5 - if you type yes to take another card it will be sum the result to your current score and it will be revealed the rest of computers card
#final it will be compare both final sums and be declared the winner

def play_game():

    inicial_cards_player = 2
    inicial_cards_computer = 2

    player_cards = random.sample(cards, inicial_cards_player)

    computer_cards = random.sample(cards, inicial_cards_computer )

    current_player_score = sum(player_cards)

    print(f"""Your cards are: {player_cards}. Your current score is: {current_player_score}
    Computer's first card: {computer_cards[0]}""")
    if current_player_score == 21:
            print("You have a blackjack, you won!")

    another_card_player = input("Type 'y' to get another card or 'n' to pass: ").lower()
    if another_card_player == 'y':
        another_card_add = random.choice(cards)
        player_cards.append(another_card_add)
        current_player_score = sum(player_cards)
        another_card_computer_add = random.choice(cards)
        computer_cards.append(another_card_computer_add)
        current_computer_score = sum(computer_cards)
            

        print(f"""Your final cards are: {player_cards}. Current score: {current_player_score}
    Computer's finals cards: {computer_cards}. And scores {current_computer_score}""")
        if current_player_score == 21 or current_computer_score> 21:
            print("You won!")
        elif current_computer_score == 21 or current_player_score > 21:
            print("You lose!")
        elif current_player_score == current_computer_score:
            print("Draw!")
        elif current_computer_score < current_player_score <21:
            print("You won!")
        elif current_player_score < current_computer_score <21:
            print("You lose!")
        elif current_computer_score > 21 and current_player_score >21:
            print("Draw!")
            

            
    if another_card_player == 'n':
        current_computer_score = sum(computer_cards)
        if current_player_score < 17:
            another_card_add = random.choice(cards)
            player_cards.append(another_card_add)
            current_player_score = sum(player_cards)
            another_card_computer_add = random.choice(cards)
            computer_cards.append(another_card_computer_add)
            current_computer_score = sum(computer_cards)
        print(f"""Your hand is {player_cards}. Score: {current_player_score}
    Computer's hand: {computer_cards}. Score {current_computer_score}""")
        if  current_computer_score < current_player_score and current_player_score <21:
            print("You won!")  
        elif current_computer_score > current_player_score and current_computer_score <21:
            print("You lose!")
        elif current_player_score == current_computer_score:
            print("Draw!")
        elif current_computer_score > 21 and current_player_score >21:
            print("Draw!")
        elif current_player_score == 21  or current_computer_score > 21:
            print("You won!")
        elif current_computer_score == 21 or current_player_score > 21:
            print("You lose!")
    
while input("Do you want to play blackjack (y/n)?: ") == 'y':
    print(logo)
    play_game()