import random

#gets dealer score
def get_dealer_score():
    dealer_card_dealt = random.randint(16,20)
    return dealer_card_dealt

#deals a random card
def deal_card():
    card_dealt = random.randint(1,10)
    return card_dealt

#function for drawing a players card
def get_player_score():
    player_hand = deal_card()
    player_hand += deal_card()

    print("Your hand of two cards has a total value of ", player_hand)

    user_response = input("Would you like to take another card? (y/n) ")

    #while loop checking the value of the players hand
    while user_response == "Y" or user_response == "y":
        player_hand += deal_card()

        if player_hand <= 21:
            print("Your hand now has a total of ", player_hand)
            user_response = input("Would you like to take another card? (y/n) ")

        elif player_hand > 21:
            print("You BUSTED with a total value of", player_hand)
            break

    return player_hand

#main function checks if player won the game and asks if they want to play again
def main():

    user_response = "Y"
    while user_response == "Y" or user_response == "y":
        dealer_score = get_dealer_score()
        player_score = get_player_score()

        if player_score > 21:
            print(" ")
            print("*** You lose ***")
            print(" ")
            user_response = input("Would you like to play again? (y/n) ")

        elif player_score <= 21 and player_score > dealer_score:
            print("You have stopped taking more cards with a hand of ", player_score)
            print("The dealer had a hand of ", dealer_score)
            print(" ")
            print("*** YOU WIN! ***")
            print(" ")
            user_response = input("Would you like to play again? (y/n) ")

        elif player_score <= dealer_score and player_score <= 21:
            print("You have stopped taking more cards with a hand of ", player_score)
            print("The dealer had a hand of ", dealer_score)
            print(" ")
            print("*** You lose ***")
            print(" ")
            user_response = input("Would you like to play again? (y/n) ")

main()
# This is a simple program that plays a game of blackjack
# It is not a complete game, but it does have the basic functionality
