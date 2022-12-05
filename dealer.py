class Dealer:
    def __init__(self):
        self.hand = None
    
    def get_str_hand(self): #nothing to explain here, mostly making a dealer to compete against, will create a player out of this class.
        return str(self.hand)
    
    def hit(self, card):
        self.hand.add(card) #both player and dealer will be able to hit a card, so might as well put the method here.