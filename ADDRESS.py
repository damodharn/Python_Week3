# *********************************************************************************************
# Purpose: To write a program to create Address Book Management.
# Author:  Damodhar D. Nirgude.
# *********************************************************************************************

from address import Address
import sys                                          # imorting sys module


def main():
    try:
        a1 = Address()                                  # Assigning the object to address class
        print("Do you want to create New Address Book. Y/N")
        ch = input()
        if ch.upper() == 'Y' or ch.upper() == 'YES':
            f_name = input('Enter File Name to be created.')
            a1.create(f_name)
        choice = int(input('Enter\n1: To Add new contact'
                           '\n2: To delete\n3: To Update address '
                           'book Data\n4: To print Address book\n5: To sort by zip code\n6: To sort by name'
                           '\n7: To Quit: '))       # Asks user for input
        if choice == 1:
            f_name = input('Enter File Name.')
            a1.open(f_name)
            a1.add()                                     # if user input is 1 the add a data
        elif choice == 2:
            a1.delete()                                  # if user input is 2 then delete a data
        elif choice == 3:
            f_name = input('Enter File Name.')
            a1.open(f_name)
            a1.update()                                  # user input is 3 to update the data
        elif choice == 4:
            f_name = input('Enter File Name.')
            a1.open(f_name)
            a1.print()                                   # user input is 4 to print the AddressBook
        elif choice == 5:
            f_name = input('Enter File Name.')
            a1.open(f_name)
            a1.sort_zip()                                    # user input is 5 to sort by zipcode
        elif choice == 6:
            f_name = input('Enter File Name.')
            a1.open(f_name)
            a1.sort_name()                                # if user input is 6 to sort by name
        elif choice == 7:
            sys.exit()                                   # system exit
    except ValueError as e:                              # exception handling for json  file error
        print('Error:', e)


if __name__ == '__main__':
    main()