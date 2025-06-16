import sys
from bank_account import BankAccount

def main():
    """
    Main function to handle command line interactions with BankAccount.
    """
    # Create account with initial balance of $100
    account = BankAccount(100)
    
    # Check if sufficient command line arguments are provided
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        print("Examples:")
        print("  python main-0.py deposit:50")
        print("  python main-0.py withdraw:20")
        print("  python main-0.py display")
        sys.exit(1)

    # Parse command and parameters
    command_parts = sys.argv[1].split(':')
    command = command_parts[0]
    
    # Extract amount if provided
    try:
        amount = float(command_parts[1]) if len(command_parts) > 1 else None
    except (ValueError, IndexError):
        amount = None

    # Execute commands based on user input
    if command == "deposit":
        if amount is not None and amount > 0:
            account.deposit(amount)
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Invalid deposit amount. Please provide a positive number.")
            
    elif command == "withdraw":
        if amount is not None and amount > 0:
            if account.withdraw(amount):
                print(f"Withdrew: ${amount:.2f}")
            else:
                print("Insufficient funds.")
        else:
            print("Invalid withdrawal amount. Please provide a positive number.")
            
    elif command == "display":
        account.display_balance()
        
    else:
        print("Invalid command.")
        print("Available commands: deposit:<amount>, withdraw:<amount>, display")

if __name__ == "__main__":
    main()