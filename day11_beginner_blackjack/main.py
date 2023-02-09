############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.



import os
import random
from art import logo
from typing import List


def deal_card():
    """Return a random card from the deck"""
    deck = [11,1,2,3,4,5,6,7,8,9,10]
    return random.choice(deck)


def calculate_score(cards: List[int]):
    """Take a list of cards and return its score"""
    if sum(cards)==21 and len(cards) == 2:
        return 0
    
    if sum(cards)>21 and (11 in cards):
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)
    
    
def result(dealer_score:int, player_score: int):
    if player_score>21 and dealer_score>21:
        return "You went over. You lose 😤"
    elif dealer_score == player_score:
        return "Draw!"
    elif player_score == 0:
        return "Win with a Blackjack 😎"
    elif dealer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif player_score>21:
        return "You went over. You lose 😤"
    elif player_score>dealer_score:
        return "You win 😃"
    elif dealer_score>21:
        return "Opponent went over. You win 😁"
    else:
        return "You lose 😤"
    
    
def play_game():
    print(logo)
    
    dealer, player = [],[]
    for _ in range(2):
        dealer.append(deal_card())
        player.append(deal_card())
        
    while True:
        dealer_score= calculate_score(dealer)
        player_score= calculate_score(player)
        if player_score>=21 or player_score==0 or dealer_score==0:
            break
        
        print("Dealer's first card :", dealer[0])
        print("Your cards :         ", *player)
        print("Current Score:       ", player_score)
        
        if input("Type 'y' to get another card, type 'n' to pass: ").lower() == 'y':
            player.append(deal_card())
            print()
        else:
            print()
            break
    
    while dealer_score!=0 and dealer_score<17:
        dealer.append(deal_card())
        dealer_score= calculate_score(dealer)
        
    print()
    print("Dealer's final hand :", *dealer)
    print("Dealer's Score:      ", dealer_score)
    print("Your final cards :   ", *player)
    print("Current Score:       ", player_score)
    
    print(result(dealer_score, player_score))
    print()
    


def start_game():
    while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
        os.system('cls')
        play_game()


if __name__ == "__main__":
    start_game()





# import os
# import random
# from art import logo


# # print(logo)

# def deal_card():
#     """Returns a random card from the deck"""
#     cards = [11,10]#[11,1,2,3,4,5,6,7,8,9,10,10,10,10]
#     return random.choice(cards)

# def end_score(dealer, player):
#     print(f"Dealer's final hand :   {dealer}")
#     print(f"Dealer's Score:         {sum(dealer)}")
#     print(f"Your final cards :      {player}")
#     print(f"Current Score:          {sum(player)}")

# def blackjack():
#     os.system('cls')
#     print(logo)
    
#     dealer, player = [], []
#     for _ in range(2): 
#         dealer.append(deal_card())
#         player.append(deal_card())
        
#     if sum(player) == 21 or sum(dealer) == 21:
#         end_score(dealer, player)
#         if sum(dealer)<sum(player): print("You got a BLACKJACK! You win! 🎉")
#         elif sum(dealer)>sum(player): print("Dealer got a BLACKJACK! You Loose! 😭")
#         else: print("Draw! ")
#         return
    
#     response = 'y'
#     while response == 'y':
#         if sum(player)>21 and (11 in player):
#             print(player)
#             player.remove(11)
#             player.append(1)
#         print('\n')
#         print(f"Dealer's first card :   {dealer[0]}")
#         print(f"Your cards :            {player}")
#         print(f"Current Score:          {sum(player)}")
#         if sum(player)>21:
#             print("\nYou have went over...")
#             end_score(dealer, player)
#             print('You went over! You Loose! 😭')
#             return
#         if sum(player) == 21:
#             break
#         else:
#             response = input("Type 'y' to get another card, press any other key to pass: ").lower()
#             if response == 'y': player.append(deal_card())
    
#     print("\nYou have chose to pass...")
#     while sum(dealer)<17: 
#         dealer.append(deal_card())
#         if sum(dealer)>21 and (11 in dealer):
#             dealer.remove(11)
#             dealer.add(1)
#     end_score(dealer, player)
#     if sum(dealer)>21:
#         print("Dealer went over! You WIN! 🎉")
#     elif sum(dealer)<sum(player): print("You win! 🎉")
#     elif sum(dealer)>sum(player): print("You Loose! 😭")
#     else: print("Draw! ")
    
    



# if __name__ == "__main__":
#     while True:
#         response = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ")
#         if response.lower() == 'y':
#             blackjack()
#         else:
#             break