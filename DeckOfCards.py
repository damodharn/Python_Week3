# *********************************************************************************************
# Purpose: To write a program to create Deck Of Cards to shuffle 9 cards to four players (2D array method).
# Author:  Damodhar D. Nirgude.
# *********************************************************************************************
import itertools                             # importing itertools module
import random                                # importing random module


class DeckOfCards:
    def __init__(self):
        self.arr = []
        self.cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        self.suits = ['Spades', 'Clubs', 'Hearts', 'Diamonds']
        self.deck = list(itertools.product(self.cards, self.suits))  # it's a List of Tuples containing card
        # and suits combination.

    def distribution(self):                              # Function to randomly distribute the cards to 4 players.
        for i in range(4):  # Using for loop for inserting cards into 2D array.
            random.shuffle(self.deck)  # random shuffle to deck cards.
            ls = list()
            for j in range(9):
                ls.append(self.deck[j])
            self.arr.append(ls)
        for i in range(4):  # Printing cards and their respective suits.
            print('______________________________________________')
            print('\nPlayer', i + 1, 'Cards :')
            print('-----------------------')
            for j in range(9):
                print("{:<1}) {:>5} of {:<9} |".format(j + 1, self.arr[i][j][0], self.arr[i][j][1]))


def main():
    dk = DeckOfCards()
    print("Enter To Distribute Cards to each Player.")
    input()
    dk.distribution()


if __name__ == '__main__':
    main()