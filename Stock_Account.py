# *********************************************************************************************
# Purpose: To write a program to create Stock Account Management.
# Author:  Damodhar D. Nirgude.
# *********************************************************************************************

import json
from Stock_Report import Stock


class StockAccount:

    def __init__(self, fn=None):
        self.lst = {'stocks': []}
        self.fileName = fn

    def create(self):  # method to create a json file
        try:
            with open(self.fileName + '.json', 'w') as f1:
                json.dump(self.lst, f1, indent=2)
        except FileExistsError as e:
            print(e)
        else:
            print("Account Created successfully.")
            f1.close()

    def open(self):  # method to open a json file
        try:
            with open(self.fileName + '.json', 'r') as f1:
                self.lst = json.load(f1)
        except FileNotFoundError as e:
            print(e)
            return False
        else:
            return True

    def add_stk(self, shares, stock_name):  # method to add stock data to the file
        add_new = {}
        try:
            stock_price = int(input('Enter the price per stock: '))
        except ValueError:
            print('You entered Wrong data!')
            self.add_stk(shares, stock_name)
        else:
            add_new['StockName'] = stock_name
            add_new['StockPrice'] = stock_price
            add_new['Shares'] = shares
            self.lst['stocks'].append(add_new)
            self.save()
            print('Stock {} bought successfully !'.format(stock_name))
            self.print_rep()

    def save(self):  # method to save the data to the json file.
        with open(self.fileName + '.json', 'w') as f1:
            json.dump(self.lst, f1, indent=2)
            f1.close()

    def print_rep(self):  # method to print the json data.
        try:
            with open(self.fileName + '.json', 'r') as f2:  # loading json data to a variable
                stock_data = json.load(f2)
        except FileExistsError as e:
            print(e)
        else:
            f2.close()
            total = 0
            print('\n')
            print('\t\t\t\t*****  STOCK REPORT  *****')  # printing table for stock report

            print('----|-----------------|-----------------|-----------------|----------------------|')
            print('{:<4}'.format('NO. |'), end=' ')
            for i in stock_data['stocks'][0]:
                print('{:<16}|'.format(i), end=' ')
            print("Total Value / Stock  |")
            print('____|_________________|_________________|_________________|______________________|')
            for i in range(len(stock_data['stocks'])):
                total += stock_data['stocks'][i]['StockPrice'] * stock_data['stocks'][i]['Shares']
                print('{:<4}| {:<16s}| {:<16d}| {:<16d}| {:>16d} Rs. |'
                      .format(i+1, stock_data['stocks'][i]['StockName']
                              , stock_data['stocks'][i]['StockPrice'], stock_data['stocks'][i]['Shares']
                              , stock_data['stocks'][i]['StockPrice'] * stock_data['stocks'][i]['Shares']))
            print('____|_________________|_________________|_________________|______________________|')
            print("YOUR PORTFOLIO:\nTotal Value of all the Stocks: ", total, 'Rs.')
            print('__________________________________________________________________________________')

    def acc_val(self):
        try:
            with open(self.fileName + '.json', 'r') as f2:  # loading json data to a variable
                stock_data = json.load(f2)
        except FileExistsError as e:
            print(e)
        else:
            f2.close()
            total = 0
            for i in range(len(stock_data['stocks'])):
                total += stock_data['stocks'][i]['StockPrice'] * stock_data['stocks'][i]['Shares']
            return total

    def buy_stock(self):
        if self.open() is True:
            print('file opened successfully!')
            try:
                name = input("Enter name of stock you wanted to buy")
                qty = int(input("Enter amount of stocks you wanted to buy"))
            except ValueError as e:
                print(e)
            else:
                for i in range(len(self.lst['stocks'])):  # Check stock in the account using stock name.
                    if str(self.lst['stocks'][i]['StockName']).casefold() == name.casefold():  # If stock found
                        self.lst['stocks'][i]['Shares'] += qty  # add stocks
                        print('{} Shares of {} bought successfully !'.format(qty, name))
                        self.save()
                        self.print_rep()
                        return
                self.add_stk(qty, name)  # If file opened but stock is not there in the account then add stock into acc.
        else:  # If file is failed to open, print message.
            print('{} Account not found !'.format(self.fileName))
            print("Please Create an Account before buying stocks. or Enter correct details.")

    def sell_stock(self):
        if self.open() is True:
            print('file opened successfully!')
            try:
                name = input("Enter name of stock you wanted to Sell")
                qty = int(input("Enter a No. of stocks you wanted to Sell"))
            except ValueError as e:
                print(e)
            else:
                for i in range(len(self.lst['stocks'])):  # Check stock in the account using stock name.
                    if str(self.lst['stocks'][i]['StockName']).casefold() == name.casefold():  # If stock found
                        if self.lst['stocks'][i]['Shares'] >= qty:
                            self.lst['stocks'][i]['Shares'] -= qty  # remove qty no. of stocks
                            print('{} Shares of {} Sold successfully !'.format(qty, name))
                            if self.lst['stocks'][i]['Shares'] == 0:
                                del self.lst['stocks'][i]
                            self.save()
                            self.print_rep()
                            return
                        else:
                            print('You don\'t have {} shares of {} stocks in Your account.'.format(qty, name))
                            return
                print('No stock named {} found in your Account'.format(name))
                print('plz.. Enter a correct details.')
        else:
            print('Fail to Sell stock. No Account named {} found.'.format(self.fileName))


def stock_manager(choice):
    if choice == 1:
        cnt2 = 0
        while cnt2 < 3:
            print("Do u have an account ?\nEnter Y/N:", end=' ')  # Ask weather user has an account or not.
            ch = input()
            if ch.upper() == 'N' or ch.upper() == 'NO':  # If don't have acc ask to create.
                print("please Create an Account before buying stocks.")
                cnt = 0
                while cnt < 3:
                    print('Do You Want to Create an Account ?\nEnter Y/N')
                    usr = input()
                    if usr.upper() == 'Y' or usr.upper() == 'YES':  # If yes only then create an acc n buy stock.
                        filename = input("Enter a File Name to be created:")
                        st = StockAccount(filename)  # assigning object to Stock class
                        st.create()
                        st.buy_stock()
                        cnt2 = 4
                        break
                    elif usr.upper() == 'N' or usr.upper() == 'NO':  # else don't buy stock
                        print("sorry !! You can't buy stocks without having an Account.")
                        cnt2 = 4
                        break
                    else:
                        if cnt == 1:
                            print('last chance.. plz enter correct choice')
                        elif cnt == 2:
                            print('You have exceeded the limit of attempts')
                        else:
                            print('Wrong entry')
                        cnt += 1
            elif ch.upper() == 'Y' or ch.upper() == 'YES':  # If user already has an acc then ask for filename
                filename = input("Enter a File Name to be opened:")  # n buy stock
                st = StockAccount(filename)  # assigning object to Stock class
                st.buy_stock()
                break
            else:
                if cnt2 == 1:
                    print('last chance.. plz enter correct choice')
                elif cnt2 == 2:
                    print('You have exceeded the limit of attempts')
                else:
                    print('Wrong entry')
                cnt2 += 1
    elif choice == 2:
        filename = input("Enter a Account Name to be Opened (eg. st2):")
        st = StockAccount(filename)  # assigning object to Stock class
        st.sell_stock()
    elif choice == 3:
        filename = input("Enter a Account Name to be Opened (eg. st2):")
        st = StockAccount(filename)  # assigning object to Stock class
        st.print_rep()
    elif choice == 4:
        quit()
    else:
        print('Wrong Entry')


def main():
    try:
        print('\n\t\t\tWelcome to Stock Account Management Office.')
        print('Enter:\n1: To buy stocks.\n2: To Sell stocks'
              '\n3: To print acc Portfolio Report\n4: To quit.')
        choice = int(input('Enter a value: '))  # Ask for user input.
    except ValueError as e:
        print(e)
    else:
        stock_manager(choice)


if __name__ == '__main__':
    main()