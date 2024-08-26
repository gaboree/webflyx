import random

SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]

RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]


class Card:
    def __init__(self, rank, suit):
        pass

    def __eq__(self, other):
        pass

    def __lt__(self, other):
        pass

    def __gt__(self, other):
        pass

    # don't touch below this line

    def __str__(self):
        return f"{self.rank} of {self.suit}"
