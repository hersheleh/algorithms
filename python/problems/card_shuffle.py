"""Card shuffling Algorithm."""
from random import randint, random


class Card:
    """Class defines a single playing card."""

    def __init__(self, rank, suite):
        """Create new playing card with rank and suite."""
        self.rank = rank
        self.suite = suite

    def __repr__(self):
        """Return string representation of playing Card.

        Print rank right justified to char size of Queen.
        print suite left justified to char size of 'Diamonds'
        """
        return "[{:>6} | {:<9}]".format(self.rank, self.suite)


class DeckOfCards:
    """Class to manage a Deck(list) of card objects."""

    faces = ('Jack', 'Queen', 'King', 'Ace')
    suites = ('Clubs', 'Diamonds', 'Hearts', 'Spades')

    def __init__(self):
        """On instantiate instantiate deck of 52 playing cards in a list."""
        self.deck = []

        for suite in self.suites:
            for i in range(2, 11):
                self.deck.append(Card(i, suite))
            for face in self.faces:
                self.deck.append(Card(face, suite))

    def print_deck(self):
        """Print a deck of cards."""
        print("-------------------------")
        for card in self.deck:
            print(" {} ".format(card))
        print("-------------------------")

    def perfect_shuffle(self):
        """Suffle deck of cards."""
        split_point = len(self.deck)//2  # integer division
        trailing_half = self.deck[split_point:]
        del self.deck[split_point:]

        j = 0
        for i in range(0, len(trailing_half)):
            self.deck.insert(j+1, trailing_half[i])
            j += 2

    def stack_shuffle(self, fudge=0, error_prob=0.4):
        """Shuffle a deck of cards using a stack data structure."""
        # split deck in half + or - 10
        fudge_factor = randint(-fudge, fudge)
        split_point = len(self.deck)//2 + fudge_factor
        # determine bigger half

        trailing_half = self.deck[split_point:]
        table = []
        del self.deck[split_point:]

        while (len(self.deck) > 0 or len(trailing_half) > 0):
            deck_not_empty = len(self.deck) != 0
            trail_not_empty = len(trailing_half) != 0
            if (deck_not_empty and random() > error_prob):
                table.append(self.deck.pop())
            if (trail_not_empty and random() > error_prob):
                table.append(trailing_half.pop())

        self.deck = table


def test_perfect_shuffle():
    """Test perfect shuffle method in DeckOfCards class."""
    new_deck = DeckOfCards()
    new_deck.print_deck()
    # breakpoint()
    for i in range(0, 20):
        new_deck.perfect_shuffle()
    new_deck.print_deck()
    print(len(new_deck.deck))


def test_stack_shuffle():
    """Test the stack shuffle method in DeckOfCards class."""
    new_deck = DeckOfCards()
    new_deck.print_deck()
    for _ in range(0, 38571):
        new_deck.stack_shuffle(fudge=10, error_prob=0.3)
    new_deck.print_deck()
    print(len(new_deck.deck))


if __name__ == '__main__':
    # test_perfect_shuffle()
    test_stack_shuffle()
