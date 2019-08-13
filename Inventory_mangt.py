
import json                                           # importing json module


class Inventory:

    def __init__(self):                                 # method to create a json file
        self.lst = {'Rice': [], 'Pulses': [], 'Wheat': []}

    def create_json(self):  # Method to create new json file.
        filename = input('Enter file name: ')
        with open(filename + '.json', 'a') as f1:
            json.dump(self.lst, f1, indent=2)
            f1.close()

    def open_json(self):                               # method to open already present json file
        filename = input('Enter the filename: ')      # and printing it's data.
        try:
            with open(filename+'.json', 'r') as f1:
                str1 = json.load(f1)
                print('file opened successfully!\n')
                for j in str1:
                    for k in str1[j]:
                        print(j, ':', k)
        except Exception as e:
            print("File not Found\n", e)

    def add_inv(self):  # method to add inventory items to file and then saving them in json file.
        dix = {}
        try:
            for i in self.lst:  # Traversing in dictionary to get different items from user.
                print("Enter how many items of {} you wanted to add".format(i))
                item = int(input())
                if item > 0:
                    for j in range(item):
                        name = input('Enter the name of item: ')
                        weight = int(input('Enter the weight: '))
                        price = int(input('Enter the price: '))
                        dix['Name'] = name
                        dix['weight'] = weight
                        dix['price'] = price
                        self.lst[i].append(dix.copy())  # Adding each item into the dictionary dix.
            self.save()  # To save file in json file.
            self.print_i()  # Printing In inventories added by user.
        except ValueError:
            print('Enter valid details!')

    def print_i(self):  # method to print the Inventory file
        if len(self.lst) >= 1:
            print('\n-------------- INVENTORY------------------------')
            for i in self.lst:
                print("________________________________________________")
                print('No.\t\t{} \t\t\tWeight\t\t\tPrice/Kg\n\t\t(Type)'.format(i))
                print('------------------------------------------------')
                for j in range(len(self.lst[i])):
                    print(j+1, '\t\t', self.lst[i][j]['Name'], '\t\t\t', self.lst[i][j]['weight'], '\t\t\t',
                          self.lst[i][j]['price'])
        else:
            print('No items in Inventory')
            ch = input('Do you want to add items: Y/N')
            if ch.upper() == 'Y':
                self.add_inv()
            else:
                quit()

    def save(self):  # method to save the data to the json file
        print("To Save File in Json format.")
        filename = input('Enter the file name')
        with open(filename + '.json', 'w') as f1:
            json.dump(self.lst, f1, indent=2)
            print("{} .json file saved Successfully..".format(filename))
            f1.close()

