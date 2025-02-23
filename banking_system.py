# Dictionary to store accounts and balances
accounts = {}

# Constants
MAX_DEPOSIT_AMOUNT = 50000000  # Maximum deposit limit

# Function to display the main menu
def display_menu():
    """
    Displays the main menu options to the user.
    """
    print("\nWelcome to the Simple Banking System")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Transfer Money")
    print("6. Exit")

# Function to create a new account
def create_account():
    """
    Creates a new account with an initial balance.
    Prompts the user for an account number and initial balance.
    Stores the account in the 'accounts' dictionary.
    """
    account_number = input("Enter account number: ")
    if account_number in accounts:
        print("Account already exists.")
    else:
        initial_balance = get_valid_amount("Enter initial balance: ")
        if initial_balance > MAX_DEPOSIT_AMOUNT:
            print(f"Initial balance cannot exceed {MAX_DEPOSIT_AMOUNT}.")
        else:
            accounts[account_number] = initial_balance
            print(f"Account {account_number} created with balance {initial_balance}.")

# Function to deposit money
def deposit_money():
    """
    Deposits money into an existing account.
    Ensures the deposit amount does not exceed the maximum limit.
    """
    account_number = input("Enter account number: ")
    if account_number in accounts:
        amount = get_valid_amount("Enter amount to deposit: ")
        if amount > MAX_DEPOSIT_AMOUNT:
            print(f"Deposit amount cannot exceed {MAX_DEPOSIT_AMOUNT}.")
        else:
            accounts[account_number] += amount
            print(f"Deposited {amount}. New balance: {accounts[account_number]}")
    else:
        print("Account does not exist.")

# Function to withdraw money
def withdraw_money():
    """
    Withdraws money from an existing account.
    Ensures the account has sufficient funds before deducting the amount.
    """
    account_number = input("Enter account number: ")
    if account_number in accounts:
        amount = get_valid_amount("Enter amount to withdraw: ")
        if amount > accounts[account_number]:
            print("Insufficient funds.")
        else:
            accounts[account_number] -= amount
            print(f"Withdrew {amount}. New balance: {accounts[account_number]}")
    else:
        print("Account does not exist.")

# Function to check balance
def check_balance():
    """
    Displays the balance of an existing account.
    """
    account_number = input("Enter account number: ")
    if account_number in accounts:
        print(f"Account {account_number} balance: {accounts[account_number]}")
    else:
        print("Account does not exist.")

# Function to transfer money
def transfer_money():
    """
    Transfers money from one account to another.
    Ensures both accounts exist and the source account has sufficient funds.
    """
    from_account = input("Enter your account number: ")
    to_account = input("Enter recipient's account number: ")
    if from_account in accounts and to_account in accounts:
        amount = get_valid_amount("Enter amount to transfer: ")
        if amount > accounts[from_account]:
            print("Insufficient funds.")
        else:
            accounts[from_account] -= amount
            accounts[to_account] += amount
            print(f"Transferred {amount} to {to_account}. Your new balance: {accounts[from_account]}")
    else:
        print("One or both accounts do not exist.")

# Function to validate input amount
def get_valid_amount(prompt):
    """
    Validates the input amount to ensure it is a positive number.
    """
    while True:
        try:
            amount = float(input(prompt))
            if amount >= 0:
                return amount
            else:
                print("Amount must be positive.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Main program loop
def main():
    """
    Main loop to run the banking system.
    Displays the menu and processes user choices.
    """
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            create_account()
        elif choice == '2':
            deposit_money()
        elif choice == '3':
            withdraw_money()
        elif choice == '4':
            check_balance()
        elif choice == '5':
            transfer_money()
        elif choice == '6':
            print("Thank you for using the Simple Banking System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
