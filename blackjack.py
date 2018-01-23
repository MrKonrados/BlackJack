from random import shuffle


class Card(object):

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return self.name


class CardDeck(object):

    def __init__(self):
        self.cards = []
        for i in ['C', 'D', 'H', 'S']:
            for j in range(2, 11):
                self.cards.append(Card(str(j) + i, j))

            for j in ['J', 'Q', 'K']:
                self.cards.append(Card(str(j) + i, 10))

            self.cards.append(Card("A" + i, (1, 11)))


class DealingShoe(object):

    def __init__(self, decks_cout=1):
        self.cards = CardDeck().cards * decks_cout
        shuffle(self.cards)

    def pop_card(self):
        return self.cards.pop()


class Player(object):

    def __init__(self, name, bankroll=1000):
        self.name = name
        self.bankroll = bankroll
        self.hand = []

    def show_cards(self):
        return self.hand

    def add_bankroll(self, value):
        self.bankroll += value

    def bet(self, value):
        if (value > self.bankroll):
            bankroll = self.bankroll
            self.bankroll = 0
            return bankroll
        self.bankroll -= value
        return value

    def hand_value(self):
        return sum(card.value for card in self.hand)

    # def bet(self):
    #
    #     while True:
    #         try:
    #             print("BANK: %s" % p.bankroll)
    #             print("[1]=5$ [2]=10$ [3]=25$ [4]=100$")
    #             bet_value = chips[int(input("Wybierz między 1-4: ")) - 1]
    #         except:
    #             print("Błąd, spróbuj jeszcze raz")
    #             continue
    #         break
    #     self.remove_bankroll(bet_value)

    def __str__(self):
        return self.name


def take_bet(player):
    chips = (5, 25, 50, 100)
    while True:
        try:
            print("BANK:", player.bankroll)
            print("Wysokość zakładu [1]=5$ [2]=25$ [3]=50$ [4]=100$")
            choice = int(input("Wybierz 1 - 4: "))
            value = chips[choice - 1]

        except:
            print("Błąd! Spróbuj jeszcze raz")
            continue
        break
    return player.bet(value)


# class Game(object):
#     def __init__(self):
#         self.ds = DealingShoe()
#         self.player = Player("Konrad")
#         self.dealer = Player("Dealer")
#         self.bet = 0
#         self.run()
#
#     def bet(self, player):
#         chips = (5, 25, 50, 100)
#         while True:
#             try:
#                 print("Bank: " + player.bankroll)
#                 print("[1]=5$ [2]=25$ [3]=50% [4]=100$")
#                 choice = int(input("Wybierz między 1-4: "))
#                 value = chips[choice]
#             except:
#                 print("Błąd!!!! Spróbuj jeszcze raz")
#                 continue
#             break
#         self.bet += player.take_bet(value)
#
#     def give_card(self, player):
#         player.take_card(self.ds.pop_card())
#
#     def run(self):
#         running = True
#         while running:
#             # daj po 2 karty każdemu z graczy
#             for i in range(2):
#                 self.give_card(self.player)
#                 self.give_card(self.dealer)
#
#             self.bet(self.player)
# Game().run()
# while game_running:
#     print("%s: %s" % (d.name, str(d.hand[0])))
#     print("%s: %s" % (p.name, str(p.hand)))

# while d.hand_value() <= 16:
#     print(d.hand_value())
#     d.take_card(ds.pop_card())
#
# print(d.hand_value())
ds = DealingShoe()
k = Player("Konrad")
d = Player("Dealer")

k.hand = [ds.pop_card(), ds.pop_card()]
d.hand = [ds.pop_card(), ds.pop_card()]

print("Dealer: ", d.hand[0])
print("Konrad: ", k.hand, k.hand_value())

bet = take_bet(k)
print(bet)
print(k.bankroll)
