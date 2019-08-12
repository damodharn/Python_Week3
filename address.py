import json
import sys


class Address:

    def __init__(self):
        self.lst = {}
        self.filename = None

    def create(self):
        self.lst = {'data':[]}
        filename = input('Create a file name')
        with open(filename+'.json','w') as f1:
            json.dump(self.lst,f1,indent=2)
            f1.close()
            print(filename, 'File created')

    def open(self):
        filename = input('Enter the file name')
        with open(filename+'.json', 'r') as f1:
            self.lst = json.load(f1)

    def sort(self):
        for i in range(len(self.lst['data'])):
            for j in range(len(self.lst['data'])):
                if int(self.lst['data'][i]['zipcode']) < int(self.lst['data'][j]['zipcode']):
                    (self.lst['data'][i],self.lst['data'][j]) = (self.lst['data'][j],self.lst['data'][i])
        print(self.lst['data'])
        self.save()
        self.print()

    def sort_name(self):
        for i in range(len(self.lst['data'])):
            for j in range(len(self.lst['data'])):
                if self.lst['data'][i]['firstname'] < self.lst['data'][j]['firstname']:
                    (self.lst['data'][i],self.lst['data'][j]) = (self.lst['data'][j],self.lst['data'][i])
        print(self.lst['data'])
        self.save()
        self.print()

    def add(self):
        add_new = {}
        try:
            first_name = input('Enter your first name: ')
            last_name = input('Enter your last name: ')
            mobile = input('Enter the mobile number: ')
            address = input('Enter the address: ')
            zip_code = input('Enter your pin code: ')
            city = input('Enter your city name: ')
            state = input('Enter your state name: ')
            if (first_name.isalpha() and last_name.isalpha() and mobile.isnumeric() and
                    address.isalpha()and zip_code.isnumeric()and city.isalpha()and state.isalpha()):
                add_new['firstname'] = first_name
                add_new['lastname'] = last_name
                add_new['mobile'] = mobile
                add_new['address'] = address
                add_new['zipcode'] = zip_code
                add_new['city'] = city
                add_new['state'] = state
                self.lst['data'].append(add_new)
                print('tttt')
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
                first_name = input('Enter the firstname: ')
                last_name = input('Enter  the lastname: ')
                for i in range(len(self.lst['data'])):
                    if (str(self.lst['data'][i]['firstname']).casefold() == first_name.casefold()
                            and str(self.lst['data'][i]['lastname']).casefold() == last_name.casefold()):
                        print('ttt')
                        flag = True
                    if flag is True:
                        print('Enter 1 to update city')
                        print('Enter 2 to update Address')
                        print('Enter 3 to update State')
                        print('Enter 4 to update mobile')
                        print('Enter 5 to update zipcode')
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
                            self.lst['data'][i]['state'] =state
                            update = True
                        elif user == 4:
                            mobile = input('Enter New mobile number: ')
                            self.lst['data'][i]['mobile'] = mobile
                            update = True
                        elif user == 5:
                            zipcode = input('Enter the new zipcode:')
                            self.lst['data'][i]['zipcode'] = zipcode
                            update = True
                        else:
                            print('Invalid input')
                            update = False
                            self.print()
                    else:
                        print('Invalid details')
                        self.update()
        except Exception as e:
            print(e)
        else:
            if update is True:
                self.save()
                self.print()

    def save(self):
        filename = input('Enter the file name: ')
        with open(filename+'.json', 'w') as j1:
            json.dump(self.lst, j1, indent=2)
            j1.close()

    def print(self):
        try:
            if len(self.lst['data']) >= 1:
                print('\n----------------------------------------------------- ADDRESS BOOK ------'
                      '--------------------------------------------------------\n')
                print('First Name\t\t\tLast Name\t\t\t  Mobile number\t\t\t  Address\t\t\t '
                      'City\t\t\tState\t\t\t\tZipcode')
                print('-----------------------------------------------------'
                      '--------------------------------------------------------------------')
                for i in range(len(self.lst['data'])):
                    print(self.lst['data'][i]['firstname'],'\t\t  ',self.lst['data'][i]['lastname'],
                          '\t\t\t    ',self.lst['data'][i]['mobile'],'\t\t\t    ',
                          self.lst['data'][i]['address'],'\t\t\t  ',
                          self.lst['data'][i]['city'],'  \t\t\t    ',self.lst['data'][i]['state'],'\t\t\t\t',
                          self.lst['data'][i]['zipcode'])
            else:
                print('No record found')
                ch = input('Do you want to Add new record? : Enter = y/n ')
                if ch.upper() == 'Y':
                    self.add()
                else:
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
