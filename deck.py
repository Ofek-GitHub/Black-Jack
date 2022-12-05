import random
from card import Card

class Deck:
    def __init__(self):
        self.cards = []
        self.create_deck()          # this is the deck constructor and the constructor attributes.
        self.shuffle()
        
    def shuffle(self):
        random.shuffle(self.cards)  # shuffle the cards from the random library.
    
    def create_deck(self):
        for suit in range(4):
            for card in range(1,14):
                new_card = Card(suit,card)  # the new card in order to create the deck.
                self.cards.append(new_card) #   creating a deck that contains 52 cards, meaning it will go 4 loops of suits and then 13 kinds of cards.
    def deal(self, num_of_cards):
        
        dealt_cards = [] # the number of cards to deal. # num of cards is equal to 52, obviously.
        
        for i in range(num_of_cards):
            top_card = self.cards.pop() # the top card is the last in the array, we will pop since we dont want him in the deck no more.
            dealt_cards.append(top_card) # adding the top card to the dealt hand.
        
        return dealt_cards