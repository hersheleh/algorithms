class Card:

    def __init__(self, rank, suite):
        self.rank = rank
        self.suite = suite

    def __repr__(self):
        # print rank right justified to char size of 'Queen'
        # print suite left justified to char size of 'Diamonds'
        return "[{:>6} | {:<9}]".format(self.rank, self.suite)


class DeckOfCards:
    faces = ('Jack', 'Queen', 'King', 'Ace')
    suites = ('Clubs', 'Diamonds', 'Hearts', 'Spades')
    
    def __init__(self):
        self.deck = []
        for suite in self.suites:
            for i in range(2, 11):
                self.deck.append(Card(i, suite))
            for face in self.faces:
                self.deck.append(Card(face, suite))

    def print_deck(self):
        for card in self.deck:
            print (" {} ".format(card))

    def perfect_shuffle(self):
        




if __name__ == '__main__':
    new_deck = DeckOfCards()
    new_deck.print_deck()
    
