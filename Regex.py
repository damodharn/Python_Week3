# *********************************************************************************************
# Purpose: To write a program to print modified message using regex.
# Author:  Damodhar D. Nirgude.
# *********************************************************************************************
import re                                     # importing REGULAR EXPRESSION
from datetime import date                     # importing datetime module
import sys                                    # importing sys module


def regularExp(my_string):                             # Function to replace the text using REGULAR EXPRESSION

    today = date.today()
    d = today.strftime('%d/%m/%Y')
    try:
        first_name = input('Enter your first name: ')       # asks user for input first name
        if not re.match("^[a-zA-Z]*$", first_name):        # regex if invalid data
            print("Error! in Name Only letters a-z allowed!")
            sys.exit()

        last_name = input('Enter your Last name')          # asks user for last name
        if not re.match("^[a-zA-Z]*$", last_name):        # Checking the input using regex
            print("Error! in Last Name Only letters a-z allowed!")
            sys.exit()

        mobile = input('\n Enter your 10 digit mobile number '+'\n eg: 91-xxxxxxxxxx')  # input mobile number
        if len(str(mobile)) != 10:
            print("Invalid No. 10 digits are required")
            sys.exit()
        if not re.match("^[0-9]*$", mobile):                               # regex to check number
            print("Error! Only numericals 0-9 allowed!")
            sys.exit()

        if first_name.isalpha() and last_name.isalpha() and mobile.isdigit():
            full_name = first_name + " " + last_name
            mobile = '91-' + mobile
            data = [first_name, full_name, mobile, d]
            pattern = ['<<name>>', '<<full name>>', '91-xxxxxxxxxx', ' 01/01/2016']
            print("Printing Modified Message..\n")
            for i in range(4):
                my_string = re.sub(pattern[i], data[i], my_string)  # regular expression to replace pattern by User data
            print(my_string)
        else:
            raise ValueError
    except ValueError as e:                                                      # exception handling for value error
        print(e)


def main():
    my_string = '''Hello <<name>>, We have your full name as <<full name>> in our system.",
                    your contact number is 91-xxxxxxxxxx.",
                    Please,let us know in case of any clarification 
                    Thank you BridgeLabz 01/01/2016. '''
    regularExp(my_string)


if __name__ == '__main__':
    main()
