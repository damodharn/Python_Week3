# *********************************************************************************************
# Purpose: To write a program to create Stock Account Management Using LinkList.
# Author:  Damodhar D. Nirgude.
# *********************************************************************************************
import json
import pathlib
from datetime import*
from Stock_Account import*
from tets22 import LinkList


class CompanyShares:

    def __init__(self):
        self.ll = LinkList()

    def buy_share(self):
        # lst = {'stocks': []}
        new = {}

        dt, tm = self.ll.date_time()
        name = input('Enter the Name of Share.')
        share = int(input('Enter quantity of Shares.'))
        price = int(input('Enter price of a share'))
        new['StockName'] = name
        new['StockPrice'] = price
        new['Shares'] = share
        new['Date'] = dt
        new['Time'] = tm
        # lst['stocks'].append(new)
        self.ll.insert(new)
        self.ll.push(new)

    def sell_share(self):
        name = input('Enter name of share you wanted to sell.')
        if self.ll.search(name) is True:
            new = self.ll.get_item()
            self.ll.push(new)
            self.ll.delete(name)
        else:
            print('Stock not found in the List.')

    def display(self):
        self.ll.print_rep()


def main():
    cs = CompanyShares()
    while True:
        print("Enter your Choice:\n1: To Buy Company Shares.\n2: To sell Company Shares.\n3: To Print Previous "
              "Transactions.\n4: To print previous Transaction Time\n5: To quit.")
        choice = int(input())
        if choice == 1:
            cs.buy_share()
        elif choice == 2:
            cs.sell_share()
        elif choice == 3:
            cs.display()
        elif choice == 5:
            break


if __name__ == '__main__':
    main()