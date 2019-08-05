# *********************************************************************************************
# Purpose: To write a program to create Inventory Management system.
# Author:  Damodhar D. Nirgude.
# *********************************************************************************************
from Inventory_mangt import *                            # importing temp2 module


# def inventory():                                     # function to calculate the value for item
#     try:
#         with open('Inventory_management.json', 'r') as f1:         # opening json file in read mode
#             my_data = json.load(f1)
#         print('\n*************************************************************\n')
#
#         print('Name', '\t|\t', 'Price * Weight')
#         print('----------------------------')
#         for j in my_data:
#             for i in range(len(my_data[j])):  # for loop used to calculate the json price and weight
#                 a = my_data[j][i]["Name"]
#                 b = my_data[j][i]["price"] * my_data["data"][i]["weight"]
#                 print(f"{a}\t\t\t{b}\t$")
#
#     except IOError:                                           # exception handling for json file
#         print('File not present')


def main():
    i = Inventory()  # Assigning object to the Inventory class
    try:
        while True:
            print('Enter ur choice:\n1: To add items in json file \n2: To Print the Inventory\n3: To quit'
                  '\n4: To Open already created json File and O/p it in String format')
            ch = int(input('Enter the value'))  # ask User for input
            if ch == 1:  # if 1 then print the inventory
                i.add_inv()
                print("Items added..")
            elif ch == 2:  # if 2 then add items to the inventory
                i.print_i()
            elif ch == 3:  # else quit
                break
            elif ch == 4:
                i.open_json()
    except FileExistsError:  # exception handling for file
        print('Inventory management fails')

    # inventory()


if __name__ == '__main__':
    main()

