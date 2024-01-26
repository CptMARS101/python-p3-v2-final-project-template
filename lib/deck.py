from card import Card
import random

suits = ('♠SPADE','♡HEART','♣CLUB','♢DIAMOND')
ranks = ('TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE', 'TEN', 'JACK', 'QUEEN', 'KING', 'ACE')
rank_val = {'TWO':2, 'THREE':3, 'FOUR':4, 'FIVE':5, 'SIX':6, 'SEVEN':7, 'EIGHT':8, 'NINE':9, 'TEN':10, 'JACK':10, 'QUEEN':10, 'KING':10, 'ACE':11}

class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                #build and add card class to deck[]
                self.deck.append(Card(suit,rank))

    def shuffle(self):
        random.shuffle(self.deck)
        print('Shuffling the deck!')

    def deal_card(self):
        delt_card = self.deck.pop()
        return delt_card