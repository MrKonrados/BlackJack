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

    def get_card(self):
        return self.cards.pop()


class Player(object):
    hand = []

    def __init__(self, name, bankroll=1000):
        self.name = name
        self.bankroll = bankroll

    def take_card(self, card):
        self.hand.append(card)

    def show_cards(self):
        return self.hand

    def add_bankroll(self, value):
        self.bankroll += value

    def remove_bankroll(self, value):
        self.bankroll -= value

    def hand_value(self):
        return sum(card.value for card in self.hand)

    def __str__(self):
        return self.name


ds = DealingShoe()

p = Player("Konrad")
d = Player("Dealer")
p.take_card(ds.get_card())
p.take_card(ds.get_card())

while d.hand_value() <= 16:
    print(d.hand_value())
    d.take_card(ds.get_card())

print(d.hand_value())

# print(p.show_cards())
# print(p.hand_value())
