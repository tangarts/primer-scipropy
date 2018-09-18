import random as rnd

def make_deck():
    ranks = ['A', '2', '3', '4', '5', '6', '7',
             '8', '9', '10', 'J', 'Q', 'K']
    suits = ['C', 'D', 'H', 'S']
    deck = [s+r for s in suits for r in ranks]
    return deck
deck = make_deck()

card = deck[0]
card = deck.pop()

def deal_hand(n,deck):
    hand = [deck[i] for i in range(n)]
    del deck[:n]
    return hand, deck

def deal(cards_per_hand, no_of_players):
    deck = make_deck()
    hands = []
    for i in range(no_of_players):
        hand, deck = deal_hand(cards_per_hand, deck)
        hands.append(hand)
    return hands
players = deal(5,4)

import pprint; pprint.pprint(players)

