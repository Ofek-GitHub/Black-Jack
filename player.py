from dealer import Dealer

class player(Dealer):
    def __init__(self,balance):
        super().__init__()
        self.balance = balance