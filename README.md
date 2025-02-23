DESCRIPTION
Dictionary (accounts):
The program uses a dictionary to store account information. The key is the account number (a unique identifier for each account). The value is the account balance (a floating-point number representing the amount of money in the account).
Constants
MAX_DEPOSIT_AMOUNT:
A constant that defines the maximum amount of money that can be deposited in a single transaction. Set to 50,000,000 to a deposit limit.
Functions
display_menu():
Displays the main menu options to the user. Prints a list of available operations (e.g., create account, deposit money, withdraw money, etc.).
create_account():
Allows the user to create a new account. Prompts the user to enter an account number and an initial balance. Ensures the initial balance does not exceed the maximum deposit limit (MAX_DEPOSIT_AMOUNT).
deposit_money():
Allows the user to deposit money into an existing account. Prompts the user to enter the account number and the amount to deposit.
withdraw_money():
Allows the user to withdraw money from an existing account. Prompts the user to enter the account number and the amount to withdraw.
check_balance():
Displays the balance of an existing account. Prompts the user to enter the account number. Checks if the account exists in the accounts dictionary. Displays the current balance of the account.
transfer_money():
Allows the user to transfer money from one account to another. Prompts the user to enter the source account number, recipient account number, and amount to transfer. Checks if both accounts exist in the accounts dictionary. Ensures the source account has sufficient funds before transferring the amount. Updates the balances of both accounts (deducts from the source account and adds to the recipient account).
get_valid_amount(prompt):
Validates the input amount to ensure it is a positive number. Uses a while loop to repeatedly prompt the user until a valid amount is entered. Ensures the amount is a positive number and handles invalid inputs (e.g., non-numeric values).
 Main Loop (while True):
 Keeps the program running until the user chooses to exit. Displays the main menu using the display_menu() function. Prompts the user to enter a choice (1-6). Calls the appropriate function based on the user's choice. Continues running until the user selects the "Exit" option (choice == '6').
 Input Validation Loop (while True in get_valid_amount):
 Ensures the user enters a valid amount (a positive number). Repeatedly prompts the user until a valid input is provided. Handles invalid inputs (e.g., negative numbers or non-numeric values).
