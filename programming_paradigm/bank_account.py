class BankAccount:
    """
    A class to represent a bank account with basic banking operations.
    
    Attributes:
        account_balance (float): The current balance of the account
    """
    
    def __init__(self, initial_balance=0):
        """
        Initialize a BankAccount instance.
        
        Args:
            initial_balance (float): The starting balance for the account (default: 0)
        """
        self.account_balance = initial_balance
    
    def deposit(self, amount):
        """
        Deposit money into the account.
        
        Args:
            amount (float): The amount to deposit
        """
        if amount > 0:
            self.account_balance += amount
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        """
        Withdraw money from the account if sufficient funds are available.
        
        Args:
            amount (float): The amount to withdraw
            
        Returns:
            bool: True if withdrawal was successful, False if insufficient funds
        """
        if amount > 0:
            if self.account_balance >= amount:
                self.account_balance -= amount
                return True
            else:
                return False
        else:
            print("Withdrawal amount must be positive.")
            return False
    
    def display_balance(self):
        """
        Display the current account balance in a user-friendly format.
        """
        print(f"Current Balance: ${self.account_balance:.2f}")
    
    def get_balance(self):
        """
        Get the current account balance.
        
        Returns:
            float: The current account balance
        """
        return self.account_balance