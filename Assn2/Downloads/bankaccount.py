INTEREST = 0.015

class BankAccount:
    """Represents a customer's bank account with the ability to calculate interest on their account."""

    def __init__(self, account_num, first, last, balance):
        """Class contructor

        Args:
            account_num (_int_): the account's unique identifier
            first (_str_): customer first name
            last (_str_): customer last name
            balance (_float_): the account balance
        """
        self.account_num = int(account_num)
        self.first = first
        self.last = last
        self.balance = float(balance)
    
    def __str__(self):
        """Dunder method to provide a string representation of a BankAccount object

        Returns:
            str: the formatted string containing account num, last name, first name, and balance
        """
        return f"{self.account_num}: {self.first} {self.last}, ${self.balance:.2f}"
    
    def __repr__(self):
        """Dunder method to provide a printable representation of the object. Used in debugging and exceptions.

        Returns:
            str: Returns a string of the form BankAccount(account_num, first, last, balance)
        """
        return f"BankAccount({self.account_num}, {self.first}, {self.last}, {self.balance})"
    
    def calculate_interest(self):
        """Computes the 1.5% interest using the formula `balance * 0.015`

        Returns:
            float: the interest computed on the account balance.
        """
        return self.balance * INTEREST
