# *********************************************************************************************
# Purpose: To write a program to create STOCK Portfolio system.
# Author:  Damodhar D. Nirgude.
# *********************************************************************************************

import json                                           # importing json module


class Stock:                                          # class Stock created

    def __init__(self, fn=None):
        self.lst = {'stocks': []}
        self.fileName = fn

    def create(self):                                 # method to create a json file
        try:
            with open(self.fileName+'.json', 'w') as f1:
                json.dump(self.lst, f1, indent=2)
        except FileNotFoundError as e:
            print(e)
        else:
            print("File Created successfully.")
            f1.close()

    def open(self):                                    # method to open a json file
        try:
            with open(self.fileName+'.json', 'r') as f1:
                self.lst = json.load(f1)
        except FileNotFoundError as e:
            print(e)
            return False
        else:
            print('file opened successfully!')
            return True

    def add_st(self):                                   # method to add stock data to the file
        add_new = {}
        try:
            stock_name = input('Enter the Stock Name: ')
            stock_price = int(input('Enter the price per stock: '))
            shares = int(input('Enter the shares you want: '))
        except ValueError:
            print('You entered Wrong data!')
            self.add_st()
        else:
            add_new['StockName'] = stock_name
            add_new['StockPrice'] = stock_price
            add_new['Shares'] = shares
            self.lst['stocks'].append(add_new)
            self.save()
            self.print()

    def delete(self):             # method to delete json data from the file.
        self.open()
        stock_name = input('Enter the name of the stock u wanted to delete: ')
        for i in range(len(self.lst['stocks'])):
            if str(self.lst['stocks'][i]['StockName']).casefold() == stock_name.casefold():
                del self.lst['stocks'][i]
                print("Stock Deleted from File")
                self.save()
                self.print()
                break
            else:
                print(f"No stock named {stock_name} found in the file {self.fileName}.\n"
                      f"please check the stock name carefully.")

    def print(self):                     # method to print the json data.
        self.open()
        if len(self.lst['stocks']) >= 1:
            print('-------------------Inventory Management-------------------')
            print('___________________________________________________________')
            print('StockName\t\t\tStockPrice\t\t\tShares')
            print('___________________________________________________________')
            for i in range(len(self.lst['stocks'])):
                print(self.lst['stocks'][i]['StockName'], '\t\t\t', self.lst['stocks'][i]['StockPrice'], '\t\t\t',
                      self.lst['stocks'][i]['Shares'])
        else:
            print('No record found')
            ch = input('Do you want to add new Stock Value: Y/N')
            if ch.upper() == 'Y':
                self.add_st()
            else:
                quit()

    def save(self):                                   # method to save the data to the json file.
        with open(self.fileName+'.json', 'w') as f1:
            json.dump(self.lst, f1, indent=2)
            f1.close()

    def stock_cal(self):  # Function to calculate Total Stack Value.
        try:
            with open(self.fileName + '.json', 'r') as f2:  # loading json data to a variable
                stock_data = json.load(f2)
        except FileExistsError as e:
            print(e)
        else:
            total = 0
            print('\n')
            print('\t\t\t*****STOCK REPORT*****')  # printing table for stock report

            print('___---___---___---___---___---___---___---___---___---___---___')
            print('StockName\t StockPrice\t Shares\t Stock Value. |')
            print('_______________________________________________________________')
            for i in range(len(stock_data['stocks'])):
                total += stock_data['stocks'][i]['StockPrice'] * stock_data['stocks'][i]['Shares']
                print(stock_data['stocks'][i]['StockName'], '\t\t\t', stock_data['stocks'][i]['StockPrice'], '\t\t\t',
                      stock_data['stocks'][i]['Shares'], '\t\t\t'
                      , stock_data['stocks'][i]['StockPrice'] * stock_data['stocks'][i]['Shares'], 'Rs.\t\t|')
            print("_______________________________________________________________")
            print("Total Value of Stocks: ", total, 'Rs.\n___________________________________'
                                                    '___________________________')

#  *****************************  Main Method  *********************************


def main():
    try:
        filename = input("Enter a File Name to be created or opened.")
        st = Stock(filename)  # assigning object to Stock class
        print('Enter:\n1: To add stocks into new file.\n2: To add stocks into existing file.\n'
              '3: To print the inventory.\n4: To remove items.\n5: To DISPLAY PORTFOLIO.\n6: To quit.')
        choice = int(input('Enter a value: '))  # Ask for user input.
        if choice == 1:  # for adding stock items to the New file.
            st.create()
            st.add_st()
        elif choice == 2:  # To  Add stock details into already created file.
            chk = st.open()
            if chk:
                st.add_st()
            else:
                print("plz..Give correct details.\nCan't save Stock details.")
        elif choice == 3:  # to print the inventory.
            st.print()
        elif choice == 4:  # for removing stock items from the object.
            st.delete()
        elif choice == 5:  # for Displaying Portfolio.
            st.stock_cal()
        elif choice == 6:  # To exit.
            quit()
        else:
            print("Wrong Entry.")
    except ValueError as e:  # exception handling.
        print(e)
    except FileNotFoundError as e:
        print(e)


if __name__ == '__main__':
    main()