# *********************************************************************************************
# Purpose: To write a program to create Deck Of Cards to shuffle 9 cards to four players and print cards of each player
#  using Queue.
# Author:  Damodhar D. Nirgude.
# *********************************************************************************************
import itertools                             # importing itertools module
import random                                # importing random module
from Queue import Queue                      # importing Queue class from Queue file.


class DeckOfCards:
    def __init__(self):
        self.arr = []
        self.cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        self.name = ['Ace', 'Jack', 'Queen', 'King']
        # '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace'
        self.suits = ['Spades', 'Clubs', 'Hearts', 'Diamonds']
        self.deck = list(itertools.product(self.cards, self.suits))  # it's a List of Tuples containing card
        # and suits combination.
        self.qq = Queue()

    def distribution(self):                              # Function to randomly distribute the cards to 4 players
        for i in range(4):  # Using for loop for inserting cards into 2D array.
            random.shuffle(self.deck)  # random shuffle to deck cards.
            ls = list()
            for j in range(9):
                ls.append(self.deck[j])
            self.arr.append(ls)
            self.qq.en_queue(ls)  # En-Queuing each player cards into Queue.

    def display(self):  # Method to display cards of each player.
        for i in range(4):  # Printing cards and their respective suits.
            print('______________________________________________')
            print('\nPlayer', i+1, 'Cards :')
            print('-----------------------')
            if self.qq.is_empty() is False:
                arr = self.qq.de_queue()  # De-Queuing each player's cards from Queue,
                for j in range(len(arr)):
                    if int(arr[j][0]) == 1:  # If card found to be of rank 1 then print 'Ace' instead of 1.
                        name = 'Ace'
                    elif (int(arr[j][0]) != 1) and (int(arr[j][0]) < 11):
                        print("{:<1}) {:>5} of {:<9} |".format(j+1, arr[j][0], arr[j][1]))
                        continue
                    else:  # If card found to be greater than rank 10 then print proper name for that rank.
                        name = self.name[int(arr[j][0])-11]
                    print("{:<1}) {:>5} of {:<9} |".format(j + 1, name, arr[j][1]))
            else:
                print("Queue is Empty.")

    @staticmethod
    def insertion_sort(arr):  # Using insertion sort method for sorting cards by their Ranks.
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j = j - 1
                arr[j + 1] = key
        return arr

    def sort(self):
        for i in range(4):
            self.qq.en_queue(self.arr[i])  # Taking each player's card and En-Queuing them into Queue.
        for i in range(4):
            if self.qq.is_empty() is False:
                arr = self.qq.de_queue()   # De-Queuing each player's cards from Queue.
                arr = self.insertion_sort(arr)  # Sorting cards by their Ranks.
                print('______________________________________________')
                print('\nPlayer', i + 1, 'Cards :')
                print('-----------------------')
                for j in range(9):
                    if int(arr[j][0]) == 1:  # If card found to be of rank 1 then print 'Ace' instead of 1.
                        name = 'Ace'
                    elif int(arr[j][0]) < 11:
                        print("{:<1}) {:>5} of {:<9} |".format(j + 1, arr[j][0], arr[j][1]))
                        continue
                    else:
                        name = self.name[int(arr[j][0]) - 10]
                    print("{:<1}) {:>5} of {:<9} |".format(j + 1, name, arr[j][1]))
            else:  # If card found to be greater than rank 10 then print proper name for that rank.
                print("Queue is Empty.")
                break


def main():
    dk = DeckOfCards()
    print("Enter To Distribute Cards to each Player.")
    input()
    dk.distribution()
    dk.display()
    try:
        i = input('Do you want to SORT cards (by Rank).\nEnter Y/N: ')
    except ValueError as e:
        print(e)
    else:
        if i.upper() == 'Y' or i.upper() == 'YES':
            print("Sorted Cards of Each players: ")
            dk.sort()


if __name__ == '__main__':
    main()