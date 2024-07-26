# Define all the classes in one script

# Account Class
class Account:
    def __init__(self, account_number, account_holder, initial_balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew {amount}. New balance is {self.balance}.")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account({self.account_number}): {self.account_holder} with balance ${self.balance}"


# User Class
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password  # In a real application, passwords should be hashed

    def check_password(self, password):
        return self.password == password


# Transaction Class
class Transaction:
    def __init__(self, transaction_id, account, amount, transaction_type):
        self.transaction_id = transaction_id
        self.account = account
        self.amount = amount
        self.transaction_type = transaction_type
        self.process_transaction()

    def process_transaction(self):
        if self.transaction_type == "deposit":
            self.account.deposit(self.amount)
        elif self.transaction_type == "withdrawal":
            self.account.withdraw(self.amount)
        else:
            print("Invalid transaction type.")


# Bank Class
class Bank:
    def __init__(self):
        self.accounts = {}
        self.users = {}
        self.logged_in_user = None

    def register_user(self, username, password):
        if username in self.users:
            print("User already exists.")
        else:
            self.users[username] = User(username, password)
            print(f"User {username} registered successfully.")

    def login_user(self, username, password):
        user = self.users.get(username)
        if user and user.check_password(password):
            self.logged_in_user = username
            print(f"User {username} logged in successfully.")
        else:
            print("Invalid username or password.")

    def logout_user(self):
        self.logged_in_user = None
        print("Logged out successfully.")

    def add_account(self, account):
        if self.logged_in_user is None:
            print("Please log in first.")
            return
        
        if account.account_number in self.accounts:
            print("Account already exists.")
        else:
            self.accounts[account.account_number] = account
            print(f"Account {account.account_number} added.")

    def remove_account(self, account_number):
        if self.logged_in_user is None:
            print("Please log in first.")
            return

        if account_number in self.accounts:
            del self.accounts[account_number]
            print(f"Account {account_number} removed.")
        else:
            print("Account not found.")

    def get_account(self, account_number):
        if self.logged_in_user is None:
            print("Please log in first.")
            return None

        return self.accounts.get(account_number, "Account not found.")

    def __str__(self):
        if self.logged_in_user is None:
            return "Please log in to view accounts."
        return "\n".join(str(account) for account in self.accounts.values())


# Main Program
def main():
    bank = Bank()

    while True:
        print("\n--- Bank System ---")
        print("1. Register")
        print("2. Login")
        print("3. Logout")
        print("4. Create Account")
        print("5. Remove Account")
        print("6. View Accounts")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            bank.register_user(username, password)

        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            bank.login_user(username, password)

        elif choice == "3":
            bank.logout_user()

        elif choice == "4":
            if bank.logged_in_user is None:
                print("You must be logged in to create an account.")
                continue
            
            account_number = input("Enter account number: ")
            account_holder = input("Enter account holder name: ")
            initial_balance = float(input("Enter initial balance: "))
            account = Account(account_number, account_holder, initial_balance)
            bank.add_account(account)

        elif choice == "5":
            if bank.logged_in_user is None:
                print("You must be logged in to remove an account.")
                continue
            
            account_number = input("Enter account number to remove: ")
            bank.remove_account(account_number)

        elif choice == "6":
            print("\nCurrent bank accounts:")
            print(bank)

        elif choice == "7":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
