from address import Address
import sys                                          # imorting sys module

try:
    a1 = Address()                                  # Assigning the object to address class
    a1.open()                                       # opening the json file
    choice = int(input('Enter 1 to Add new contact\nEnter 2 to delete\nEnter 3 to Update address book\n'
                       'Enter 4 to print Address book\nEnter 5 to sort by zipcode\nEnter 6 to sort by name\n'
                       'Enter 7 to Quit\n: '))       # Asks user for input
    if choice == 1:
        a1.add()                                     # if user input is 1 the add a data
    elif choice == 2:
        a1.delete()                                  # if user input is 2 then delete a data
    elif choice == 3:
        a1.update()                                  # user input is 3 to update the data
    elif choice == 4:
        a1.print()                                   # user input is 4 to print the AddressBook
    elif choice == 5:
        a1.sort()                                    # user input is 5 to sort by zipcode
    elif choice == 6:
        a1.sort_name()                                # if user input is 6 to sort by name
    elif choice == 7:
        sys.exit()                                   # system exit
except FileExistsError:                              # exception handling for json  file error
    print('Error')