"""This module contains functions and classes to support processing bank account information"""
from bankaccount import BankAccount

ACCOUNT_NUM_COL = 0
FIRST_NAME_COL = 2 # was 1
LAST_NAME_COL = 4 # was 2
BALANCE_COL = 5 # was 3

class BankDataError(Exception):
    pass

def search_for_accounts(accounts,acct_num):
    for acct in accounts:
        if acct.account_num == acct_num:
            return acct
    else:
        raise ValueError("Cannot find account with that number.")
    
def load_from_file(filename):
    accounts = []
    
    try:
        with open(filename, encoding='utf-8') as infile:
            next(infile)
            for line in infile:
                line = line.strip().split(',')
                new_account = BankAccount(line[ACCOUNT_NUM_COL],line[FIRST_NAME_COL],line[LAST_NAME_COL],line[BALANCE_COL])
                accounts.append(new_account)
    except FileNotFoundError:
        raise BankDataError("Error: Cannot find that file")
    except (ValueError, IndexError):
        raise BankDataError("Error: Bad data in the file. Make sure it file is in proper format")

def main():
    """Main method that loads data and responds to user commands"""
    
    load_from_file(input("Enter a filename: "))
            
    while True:
        print("Make a selection:")
        print("1) Display account")
        print("0) Exit")

        choice = input()
        if choice == '1':
            acct_num = int(input("Enter an account number: "))
            for acct in accounts:
                if acct.account_num == acct_num:
                    print(acct)
                    break
            else:
                print("Account not found!")
        elif choice == '0':
            print("Goodbye!")
            exit(0)
        else:
            print("I don't understand that option. Try again.")
                    

if __name__ == "__main__":
    main()
