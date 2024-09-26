import random

"""Constant variables"""
SUITS = ['Spades', 'Clubs', 'Diamonds', 'Hearts']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
RANK_VALUES = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8,
                '9':9, '10':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

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

"""Game startup"""
print("Welcome to War!\nWould you like to play? (y/n)")
while True: 
    play = input()
    if (play == 'y'):
        break
    elif(play == 'n'):
        exit
    else:
        print("Invalid input")
        print("Would you like to play? (y/n)")

bot_pile = []
user_pile = []
quit = False
while True:
    if (quit == True):
        break

    """Find winner and alter collections"""
    extraPile = []
    while True:
        """Generate Card"""
        bot_index = random.randint(0,(len(cpu_cards) - 1))
        bot_card = cpu_cards[bot_index]
        my_index = random.randint(0,(len(user_cards) - 1))
        my_card = user_cards[my_index]

        """Cards played"""
        print(f'\nBot plays: {bot_card}')
        print(f'You play: {my_card}')

        """Find Value"""
        bot_value_list = bot_card.split(' ')
        bot_value = bot_value_list[0]
        user_value_list = my_card.split(' ')
        user_value = user_value_list[0]

        """Run Value operant"""
        if (RANK_VALUES[bot_value] > RANK_VALUES[user_value]):
            user_cards.remove(my_card)
            bot_pile.append(my_card)
            if (len(extraPile) > 0):
                for i in range(len(extraPile)):
                    bot_pile.append(extraPile[i])
            break
        elif (RANK_VALUES[bot_value] < RANK_VALUES[user_value]):
            cpu_cards.remove(bot_card)
            user_pile.append(bot_card)
            if (len(extraPile) > 0):
                for i in range(len(extraPile)):
                    user_pile.append(extraPile[i])
            break
        elif (RANK_VALUES[bot_value] == RANK_VALUES[user_value]):
            print('War!!! \nSetting down three cards')
            cpu_cards.remove(bot_card)
            user_cards.remove(my_card)
            extraPile.append(my_card)
            extraPile.append(bot_card)
            for i in range(3):
                bot_index = random.randint(0,(len(cpu_cards) - 1))
                bot_card = cpu_cards[bot_index]
                cpu_cards.remove(bot_card)
                my_index = random.randint(0,(len(user_cards) - 1))
                my_card = user_cards[my_index]
                user_cards.remove(my_card)
                extraPile.append(bot_card)
                extraPile.append(my_card)
            
    """Print out scores"""
    print()
    print(f'Bot cards:  {(len(cpu_cards) + len(bot_pile))}')
    print(f'Your cards: {(len(user_cards) + len(user_pile))}')
    print()

    if (len(user_cards) == 0):
        user_cards = user_pile
        user_pile = []
    if (len(cpu_cards) == 0):
        cpu_cards = bot_pile
        bot_pile = []

    """Check for winner"""
    if ((user_cards == [] and user_pile == [])):
        print('Bot wins!')
        quit = True
        break
    if ((cpu_cards == [] and bot_pile == [])):
        print('You win!')
        quit = True
        break

    """Next Card"""
    while True:
        print('Next Card? (y/n)')
        response = input()
        if (response == 'y'):
            break
        elif (response == 'n'):
            while True:
                print('Would you like to quit? (y/n)')
                verification = input()
                if (verification == 'y'):
                    exit()
                elif (verification == 'n'):
                    break
                else:
                    print('Invalid input')
                    continue
        else:
            print('Invalid input')
            continue