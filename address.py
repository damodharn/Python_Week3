import json
import sys


class Address:

    def __init__(self):  # Initializing class Address.
        self.lst = {'data': []}

    def create(self, f_name):  # Method to create New address book.
        # filename = input('Enter a file name.:')
        with open(f_name+'.json', 'w') as f1:
            json.dump(self.lst, f1, indent=2)
            f1.close()
            print(f_name, 'New Address Book created.\nAddress book is Empty.')
            print("Add data into it.")

    def open(self, f_name):  # Method to open file already created.
        # filename = input('Enter the file name.')
        try:
            with open(f_name+'.json', 'r') as f1:
                self.lst = json.load(f1)
        except FileNotFoundError as e:
            print(e)
        else:
            print("file opened Successfully.")

    def sort_zip(self):
        for i in range(len(self.lst['data'])):
            for j in range(len(self.lst['data'])):
                if int(self.lst['data'][i]['zip_code']) < int(self.lst['data'][j]['zip_code']):
                    (self.lst['data'][i], self.lst['data'][j]) = (self.lst['data'][j], self.lst['data'][i])
        print(self.lst['data'])
        self.save()
        self.print()

    def sort_name(self):  # Sorting the file data according to the Name.
        for i in range(len(self.lst['data'])):
            for j in range(len(self.lst['data'])):
                if self.lst['data'][i]['first_name'] < self.lst['data'][j]['first_name']:
                    (self.lst['data'][i], self.lst['data'][j]) = (self.lst['data'][j], self.lst['data'][i])
        print(self.lst['data'])
        self.save()
        self.print()

    def add(self):
        add_new = {}
        try:
            first_name = input('Enter your first name: ')
            last_name = input('Enter your last name: ')
            while True:
                mobile = input('Enter 10 Digit mobile number: ')
                if len(mobile) != 10:
                    print('check your No.\nEnter 10 digit no.')
                else:
                    break
            address = input('Enter the address: ')
            zip_code = input('Enter your pin code: ')
            city = input('Enter your city name: ')
            state = input('Enter your state name: ')
            if (first_name.isalpha() and last_name.isalpha() and mobile.isnumeric() and
                    address.isalpha()and zip_code.isnumeric()and city.isalpha()and state.isalpha()):
                add_new['first_name'] = first_name
                add_new['last_name'] = last_name
                add_new['mobile'] = mobile
                add_new['address'] = address
                add_new['zip_code'] = zip_code
                add_new['city'] = city
                add_new['state'] = state
                self.lst['data'].append(add_new)
                self.save()
                self.print()
        except ValueError:
            print('You entered wrong data!')
            self.add()
            return

    def update(self):
        try:
            flag = update = False
            if len(self.lst['data']) >= 1:
                first_name = input('Enter the First Name: ')
                last_name = input('Enter  the Last Name: ')
                for i in range(len(self.lst['data'])):
                    if (str(self.lst['data'][i]['first_name']).casefold() == first_name.casefold()
                            and str(self.lst['data'][i]['last_name']).casefold() == last_name.casefold()):
                        flag = True
                    if flag is True:
                        print('Enter 1 to update city')
                        print('Enter 2 to update Address')
                        print('Enter 3 to update State')
                        print('Enter 4 to update mobile')
                        print('Enter 5 to update zip_code')
                        user = int(input('Enter your choice: '))
                        if user == 1:
                            city = input('Enter New City name: ')
                            self.lst['data'][i]['city'] = city
                            update = True
                        elif user == 2:
                            address = input('Enter New address: ')
                            self.lst['data'][i]['address'] = address
                            update = True
                        elif user == 3:
                            state = input('Enter New state name: ')
                            self.lst['data'][i]['state'] = state
                            update = True
                        elif user == 4:
                            mobile = input('Enter New mobile number: ')
                            self.lst['data'][i]['mobile'] = mobile
                            update = True
                        elif user == 5:
                            zip_code = input('Enter the new zip code:')
                            self.lst['data'][i]['zip_code'] = zip_code
                            update = True
                        else:
                            print('Invalid input')
                            update = False
                            self.print()
                    else:
                        print('Invalid details')
                        # self.update()
        except Exception as e:
            print(e)
        else:
            if update is True:
                self.save()
                # self.print()

    def save(self):
        filename = input('Enter the file name: ')
        with open(filename+'.json', 'w') as j1:
            json.dump(self.lst, j1, indent=2)
            j1.close()

    def print(self):
        try:
            if len(self.lst['data']) >= 1:
                print('\n____________________________  ADDRESS BOOK  ______________________________________\n')
                print('-----------|------------|------------|----------------|------'
                      '----|--------------|---------|')
                print('{:<11}| {:<11}| {:<11}| {:<15}| {:<9}| {:<13}|{:<8} |'.format('First Name',
                                                'Last Name', 'Mob. No.', 'Address', 'City', 'State', 'Zip-Code'))
                print('-----------|------------|------------|----------------|------'
                      '----|--------------|---------|')
                for i in range(len(self.lst['data'])):
                    print('{:<11}| {:<11}| {:<11}| {:<15}| {:<9}| {:<13}| {:<8}|'.format(self.lst['data'][i]['first_name'],
                                 self.lst['data'][i]['last_name'], self.lst['data'][i]['mobile'],
                                 self.lst['data'][i]['address'], self.lst['data'][i]['city'],
                                 self.lst['data'][i]['state'], self.lst['data'][i]['zip_code']))
            else:
                print('No record found')
                # ch = input('Do you want to Add new record? : Enter = y/n ')
                # if ch.upper() == 'Y':
                #     self.add()
                # else:
                sys.exit()
        except Exception as e:
            print('File is empty', e)

    def delete(self):
        first_name = input('Enter the first name: ')
        last_name = input('Enter  the last name: ')
        for i in range(len(self.lst['data'])):
            if (str(self.lst['data'][i]['firstname']).casefold() == first_name.casefold()
                    and str(self.lst['data'][i]['lastname']).casefold() == last_name.casefold()):
                del self.lst['data'][i]
                print('deleted successfully')
                self.save()
                self.print()
                return
            else:
                print('No data found')
