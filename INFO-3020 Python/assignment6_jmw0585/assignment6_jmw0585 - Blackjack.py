"""You should not share this solution with anyone.
   Please remember that you signed an Academic Honesty Agreement."""
import random


class PlayingCard:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def get_suit(self):
        return self.suit

    def get_value(self):
        return self.value

    def get_num_value(self):
        if self.value == "ace":
            return 1
        elif self.value == "jack":
            return 10
        elif self.value == "queen":
            return 10
        elif self.value == "king":
            return 10
        else:
            return self.value

class Deck:
    def __init__(self):
        self.cards = []

    def draw_card(self):
        selected_card = random.choice(self.cards)
        self.cards.remove(selected_card)
        return selected_card

    def init_deck(self):
        suits = ["hearts", "diamonds", "spades", "clubs"]
        values = ["ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king"]
        for suit in suits:
            for value in values:
                self.cards.append(PlayingCard(suit, value))

    def get_self_cards(self):
        hand_value = 0
        for x in self.cards:
            temp = x.value
            hand_value = temp

            hand_value = self.cards[x.value]
            print(x.suit, x.value, sep=' ')

            print('Hand Value is: ', hand_value)


class Person:
    def __init__(self, deck):
        """set hand and get two initial cards from the deck"""
        self.deck = deck


    def play_turn(self, deck):
        """add a card from the deck to hand"""
        add_card(deck)

    def report_score(self):
        player_hand = Hand()
        """report total values of the hand"""
        print(player_hand.get_total_value())


class Dealer(Person):
    def __init__(self, deck):
        """inheirt Person Class and set self.name as 'Dealer'"""
        self.deck = deck

class Player(Person):
    def __init__(self, deck, name):
        """inheirt Person Class and set self.name as what a user typed in"""
        self.name = name
        self.deck = deck

    def get_name(self):
        return self.name


class Hand:
    def __init__(self):
        """set self.cards as an empty list"""
        self.cards = []

    def get_cards(self, deck):
        """draw two initial cards from the deck and append them to self.cards"""
        self.deck = deck
        for x in range (0, 2):
            self.cards.append(self.deck.draw_card())

        return self.cards

    def get_total_value(self):
        """get total value of cards in the hand"""
        hand_value = 0
        for x in self.cards:
            hand_value += x.get_num_value()

        return hand_value

    def add_card(self, deck):
        """draw one card from the deck and append them to self.cards"""
        self.deck = deck

        self.cards.append(self.deck.draw_card())



class BlackjackGame:


    def __init__(self):
        player_name = None
        """initialize deck and player"""
        self.deck = Deck()
        self.player = Player(self.deck,player_name)
        self.dealer = Dealer(self.deck)
        self.player_hand = Hand()
        self.dealer_hand = Hand()
    


    def play_game(self):

        # Prime the loop and start the first game.
        user_response = "Y"
        player_name = input("What's your name?: ")
        self.deck.init_deck()
        self.player_hand.get_cards(self.deck)
        self.dealer_hand.get_cards(self.deck)
        # print(player_name, '(first) was dealt a hand of: ', self.player_hand.get_total_value())

        while user_response == "Y" or user_response == "y":

            # initialize deck
            self.deck.init_deck()
            ## initialize a player amd dealer and get two cards per player
            self.player = Player(self.deck, player_name)
            self.dealer = Dealer(self.deck)

            # self.player_hand.get_cards(self.deck)
            # self.dealer_hand.get_cards(self.deck)
            player_hand = self.player_hand.get_total_value()
            dealer_hand = self.dealer_hand.get_total_value()



            if self.player_hand.get_total_value() > 0:
                del self.player_hand
                del self.dealer_hand
                self.player_hand = Hand()
                self.dealer_hand = Hand()
                self.player_hand.get_cards(self.deck)
                self.dealer_hand.get_cards(self.deck)

                print(player_name, ' was dealt a hand of: ', self.player_hand.get_total_value())

            user_input = 'Y'


            while user_input == 'Y' or user_input == 'y' and player_hand <= 21:
                user_input = input('Would you like to take another card? (Y/N) ')

                if user_input == 'y' or user_input == 'Y':
                    self.player_hand.add_card(self.deck)

                    print(player_name, 'was dealt a hand of:', self.player_hand.get_total_value())
                    player_hand = self.player_hand.get_total_value()
                    # self.player_hand.add_card(self.deck)
                    # player_hand = self.player_hand.get_total_value()
                    if self.player_hand.get_total_value() > 21:
                        print(player_name, 'You Lose!')
                        user_response = input('Would you like to play again? (Y/N)')

                elif user_input == 'n' or user_input == 'N' and self.player_hand.get_total_value() <= 21:
                    user_input = 'N'
                    print(player_name, ' you have stopped taking more cards at:', self.player_hand.get_total_value())
                    print("""Dealer's hand""", self.dealer_hand.get_total_value())
                    print("""Your hand""", self.player_hand.get_total_value())



                    if self.player_hand.get_total_value() < self.dealer_hand.get_total_value() and self.dealer_hand.get_total_value() > 21 and self.player_hand.get_total_value() <= 21:
                        # print('Dealer', self.dealer_hand.get_total_value())
                        # print('Player', player_hand)

                        print(player_name, 'You win!')
                        user_response = input('Would you like to play again? (Y/N) ')
                        print(' ')

                    elif self.player_hand.get_total_value() > self.dealer_hand.get_total_value() and self.player_hand.get_total_value() <= 21:
                        # print('Dealer', self.dealer_hand.get_total_value())
                        # print('Player', player_hand)
                        print(player_name, 'You win!')
                        user_response = input('Would you like to play again? (Y/N) ')
                        print(' ')

                    elif self.dealer_hand.get_total_value() > self.player_hand.get_total_value() and self.dealer_hand.get_total_value() <= 21:
                        # print('Dealer', self.dealer_hand.get_total_value())
                        # print('Player', player_hand)
                        print(player_name, 'You lose!')
                        user_response = input('Would you like to play again? (Y/N) ')
                        print(' ')

                    elif self.dealer_hand.get_total_value() == self.player_hand.get_total_value():
                        print("""You've tied with the dealer. Hand is reset.""")
                        print(' ')










            # print('out of while loop')

        """Al control should take a place here"""


game = BlackjackGame()
game.play_game()
