import json
import hashlib

# Dictionary to store account credentials
password_dict = {}
# Set to store unique passwords
password_set = set()

def add_password(account, password):
    """
    Adds an account and password to the dictionary.
    Also checks for duplicate passwords using a set.
    """
    if password in password_set:
        print(f"⚠️  Warning: The password '{password}' is already used for another account.")
    else:
        # Hash the password before storing it
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        password_dict[account] = hashed_password
        password_set.add(password)
        print(f"✅ Account '{account}' added successfully!")

def get_password(account):
    """
    Retrieves the password for a given account.
    """
    if account in password_dict:
        print(f"🔑 Password for '{account}': {password_dict[account]}")
    else:
        print(f"❌ Account '{account}' not found.")

def delete_password(account):
    """
    Removes an account from the password manager.
    """
    if account in password_dict:
        password_set.discard(password_dict[account])  # Remove password from set
        del password_dict[account]
        print(f"🗑️  Account '{account}' deleted successfully!")
    else:
        print(f"❌ Account '{account}' not found.")

def check_duplicate(password):
    """
    Checks if a password already exists in the set.
    """
    if password in password_set:
        print(f"⚠️  The password '{password}' is already used.")
    else:
        print(f"✅ The password '{password}' is unique.")

def save_to_file():
    """
    Saves the password dictionary to a JSON file.
    """
    with open("passwords.json", "w") as file:
        json.dump(password_dict, file)
    print("💾 Passwords saved to 'passwords.json'.")

def load_from_file():
    """
    Loads the password dictionary from a JSON file.
    """
    global password_dict, password_set
    try:
        with open("passwords.json", "r") as file:
            password_dict = json.load(file)
            password_set = set(password_dict.values())
        print("📂 Passwords loaded from 'passwords.json'.")
    except FileNotFoundError:
        print("❌ No saved passwords found.")

def menu():
    """
    Displays the menu and handles user input with recursion.
    """
    print("\n🔒 Password Manager 🔒")
    print("1. Add Password")
    print("2. Retrieve Password")
    print("3. Delete Password")
    print("4. Check for Duplicate Password")
    print("5. Save Passwords to File")
    print("6. Load Passwords from File")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        account = input("Enter account name: ")
        password = input("Enter password: ")
        add_password(account, password)
        menu()  # Recursion to show the menu again

    elif choice == "2":
        account = input("Enter account name: ")
        get_password(account)
        menu()

    elif choice == "3":
        account = input("Enter account name: ")
        delete_password(account)
        menu()

    elif choice == "4":
        password = input("Enter password to check: ")
        check_duplicate(password)
        menu()

    elif choice == "5":
        save_to_file()
        menu()

    elif choice == "6":
        load_from_file()
        menu()

    elif choice == "7":
        print("👋 Exiting Password Manager. Goodbye!")
        return  # Exit the recursion

    else:
        print("❌ Invalid choice. Please try again.")
        menu()  # Recursion to retry

# Start the program
if __name__ == "__main__":
    menu()
