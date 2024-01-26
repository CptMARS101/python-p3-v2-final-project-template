# lib/blackjack.py

from deck import Deck
from player import Player

playing = True
#MAIN MENU functionality
def main():
    global playing
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            print("\033[37mSo long, loser!\033[37m")
            exit()
        elif choice == "1":
            play_bj()
            playing = True
        else:
            print("Invalid choice")

#Menu Text
def menu():
    print("\033[37mYou feelin' lucky? Make a bet, play some Blackjack!!:\033[37m")
    print("\033[31m0. I'm too scared to play!\033[31m")
    print("\033[33m1. Shut up and take my chips!\033[33m")

#BlackJack GAME
def play_bj(): 
#Take a bet method
    def take_bet(chips):
        while True:
            try:
                chips.bet = int(input(f'\033[33mHow many chips you bettin?(You have {chips.total}): \033[33m'))
            except ValueError:
                print('Needs to be a number!')
            else:
                if chips.bet > chips.total:
                    print(f'\033[33mYou only have {chips.total} chips!\033[33m')
                else:
                    print('Woops!')
                    break

#Hit/Hit-Stand Logic
    def hit_me(deck, hand):
        hand.add_card(deck.deal_card())
        hand.adj_ace()

    def hit_stand(deck, hand):
        ##remove global?
        global playing
        while True:
            x = input('\033[33mHit or Stand? Enter `h` or `s`: \033[33m')
            if x[0].lower() == 'h':
                hit_me(deck, hand)
            elif x[0].lower() == 's':
                playing = False
            elif x[0].lower() is None:
                print('Try Again!')
                continue
            else:
                print('Try Again!')
                continue
            break
#Card Display
    def show_cards(player, house):
        print('\033[31m House Cards>>> \033[31m')
        print('<hidden>')
        print(house.cards[0])
        print('\033[36m Player Cards>>>>>> \033[36m')
        print(*player.cards, sep= '\n')
        print('\033[36m Your card value is: \033[36m', player.value)

    def show_all(player, house):
        print('\033[31mHouse Cards>>>\033[31m')
        print(*house.cards, sep= '\n')
        print('\033[31mHouse card value is:\033[31m', house.value)
        print('\033[36m Player Cards>>>>>> \033[36m')
        print(*player.cards, sep= '\n')
        print('\033[36m Your card value is: \033[36m', player.value)

#More game functions
    def player_lose(player, house, chips):
        print('\033[31mDang you lost!!!\033[31m')
        chips.lose_bet()
    def player_win(player, house, chips):
        print('\033[32mWell arent you lucky??\033[32m')
        chips.win_bet()
    def player_bj_win(player, house, chips):
        print('\033[32mWHOAAAA What are the odds??\033[32m')
        chips.bj_bonus()
    def house_lose(player, house, chips):
        print('\033[32mAh, House busted\033[32m')
        chips.win_bet()
    def house_win(player, house, chips):
        print('\033[31mHouse always wins baby!!!\033[31m')
        chips.lose_bet()
    def tie(player, dealer):
        print('TIED!')

#Game Start  
    deck = Deck()
    deck.shuffle()

    player = Player('Player 1')
    house = Player()

    player_chips = player.chips
#Deal Cards to player & house
    player.add_card(deck.deal_card())
    player.add_card(deck.deal_card())

    house.add_card(deck.deal_card())
    house.add_card(deck.deal_card())

    take_bet(player_chips)

    show_cards(player, house)
    global playing
    while playing:
        if player.value < 21:
            hit_stand(deck, player)
            show_cards(player, house)
            if player.value == 21:
                player_bj_win(player, house, player_chips)
            elif player.value > 21:
                player_lose(player, house, player_chips)
            while house.value < 17:
                if player.value == 21:
                    player_bj_win(player, house, player_chips)
                elif player.value > 21:
                    player_lose(player, house, player_chips)
                else:
                    hit_me(deck, house)
            show_all(player, house)
            if house.value > 21:
                house_lose(player, house, player_chips)
            elif house.value > player.value:
                house_win(player, house, player_chips)
            elif house.value < player.value:
                player_win(player, house, player_chips)
            else:
                tie(player, house)
        elif player.value > 21 and player.aces:
            player.adj_ace()
        elif player.value > 21:
            player_lose(player, house, player_chips)
        elif player.value == 21:
            player_bj_win(player, house, player_chips) 
        else:
            print('SOMETHING WENT WRONG! SORRY!!!')
            
            
        print(f'\033[33mPlayers current chips:{player_chips.total} \033[33m')
        if player_chips.total == 0:
            print('Come back when you have more chips')
            break
        else:
            start_game = input('\033[37mPlay again? Enter `y` or `n`\033[37m')
            if start_game[0].lower() == 'y':
                playing = True
                player.cards = []
                player.value = 0
                player.aces = 0
                house.cards= []
                house.value = 0
                house.aces = 0
                card_count = 0
                for card in deck.deck:
                    card_count += 1
                if card_count > 8:
                    deck.shuffle()
                    player.add_card(deck.deal_card())
                    player.add_card(deck.deal_card())

                    house.add_card(deck.deal_card())
                    house.add_card(deck.deal_card())

                    take_bet(player_chips)

                    show_cards(player, house)
                    continue
                else:
                    deck.__init__()
                    deck.shuffle()
                    player.add_card(deck.deal_card())
                    player.add_card(deck.deal_card())

                    house.add_card(deck.deal_card())
                    house.add_card(deck.deal_card())

                    take_bet(player_chips)

                    show_cards(player, house)
                    continue    
            else:
                print('Later!')
                break
        
        

                

if __name__ == "__main__":
    main()
