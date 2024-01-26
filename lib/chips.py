class Chips:
    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def bj_bonus(self):
        bonus_win = self.bet * 2
        self.total += bonus_win

    def lose_bet(self):
        self.total -= self.bet