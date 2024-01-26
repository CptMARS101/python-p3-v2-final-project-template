from deck import rank_val
from chips import Chips
class Player:
    def __init__(self, name = 'HOUSE'):
        self.name = name
        self.cards = []
        self.value = 0
        self.aces = 0
        self.chips = Chips()

    def add_card(self, card):
        self.cards.append(card)
        self.value += rank_val[card.rank]
        if card.rank == 'ACE':
            self.aces += 1

    def adj_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
            print('\033[37mAdjusting an ace!\033[37m')