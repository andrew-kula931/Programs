import random

"""Constant variables"""
SUITS = ['Spades', 'Clubs', 'Diamonds', 'Hearts']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

"""Setting up cards"""
allCards = []

for type in SUITS:
    for rank in RANKS:
        allCards.append(rank + ' of ' + type)

cpu_cards = []
user_cards = []

for i in range(len(allCards)):
    value = random.randint(0, (len(allCards) - 1))
    if (i % 2 == 0):
        cpu_cards.append(allCards[value])
        allCards.pop(value)
    else:
        user_cards.append(allCards[value])
        allCards.pop(value)
