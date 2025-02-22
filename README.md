# Dictionary to store all accounts
accounts = {}

# Function to generate account numbers
def generate_account_number():
    return len(accounts) + 1

# Function to create a new account
def create_account():
    name = input("Enter your name: ")

    # Set initial balance to 1,000,000
    initial_deposit = 1000000

    account_number = generate_account_number()
    accounts[account_number] = {"name": name, "balance": initial_deposit}
    print(f"Account created successfully! Your account number is: {account_number}")
    print(f"Initial balance: {initial_deposit}")

# Function to deposit money
def deposit_money():
    account_number = int(input("Enter your account number: "))
    amount = float(input("Enter the amount to deposit: "))

    if account_number in accounts:
        if amount > 0:
            accounts[account_number]["balance"] += amount
            print(f"Deposit successful! New balance: {accounts[account_number]['balance']}")
        else:
            print("Invalid amount. Deposit amount must be positive.")
    else:
        print("Account not found.")

# Function to withdraw money
def withdraw_money():
    account_number = int(input("Enter your account number: "))
    amount = float(input("Enter the amount to withdraw: "))

    if account_number in accounts:
        if amount > 0 and amount <= accounts[account_number]["balance"]:
            accounts[account_number]["balance"] -= amount
            print(f"Withdrawal successful! New balance: {accounts[account_number]['balance']}")
        else:
            print("Insufficient funds or invalid amount.")
    else:
        print("Account not found.")

# Function to check balance
def check_balance():
    account_number = int(input("Enter your account number: "))

    if account_number in accounts:
        print(f"Your current balance is: {accounts[account_number]['balance']}")
    else:
        print("Account not found.")

# Function to transfer money
def transfer_money():
    from_account = int(input("Enter your account number: "))
    to_account = int(input("Enter the recipient's account number: "))
    amount = float(input("Enter the amount to transfer: "))

    if from_account in accounts and to_account in accounts:
        if amount > 0 and amount <= accounts[from_account]["balance"]:
            accounts[from_account]["balance"] -= amount
            accounts[to_account]["balance"] += amount
            print(f"Transfer successful! Your new balance: {accounts[from_account]['balance']}")
        else:
            print("Insufficient funds or invalid amount.")
    else:
        print("One or both accounts not found.")

# Function to display the menu
def display_menu():
    print("\nWelcome to the Simple Banking System!")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Transfer Money")
    print("6. Exit")

# Main program loop
def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            create_account()
        elif choice == "2":
            deposit_money()
        elif choice == "3":
            withdraw_money()
        elif choice == "4":
            check_balance()
        elif choice == "5":
            transfer_money()
        elif choice == "6":
            print("Thank you for using the Simple Banking System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
