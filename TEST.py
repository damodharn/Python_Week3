import itertools                             # importing itertools module
import random                                # importing random module

arr = [[]*9]*4
cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
suits = ['Spades', 'Clubs', 'Hearts', 'Diamonds']
deck = list(itertools.product(cards, suits))  # it's a List of Tuples containing card and suits combination.


def distribution():                              # Function to randomly distribute the cards to 4 players
    for i in range(4):
        random.shuffle(deck)  # random shuffle to deck cards
        for j in range(9):
            ls = 9*[]
            ls.append(deck[j])
            arr[i].append(ls)

    for i in range(4):
        print('\nPlayer', i+1, 'Cards :')
        for j in range(9):
            print(f"{j+1}) {arr[i][j][0]} of {arr[i][j][1]},", end=' ')
            # print(j+1,':',arr[i][j][0], 'of', arr[i][j][1], end=', ')
    print()
    print(arr,"\n\n")
    print('array:', arr[1][3])

distribution()