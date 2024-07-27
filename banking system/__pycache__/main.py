# Account Class
class Account:
    def __init__(self, account_number, account_holder, initial_balance=0):
        self._account_number = account_number
        self._account_holder = account_holder
        self._balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited ${amount}. New balance is ${self._balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self._balance:
                self._balance -= amount
                print(f"Withdrew ${amount}. New balance is ${self._balance}.")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        return self._balance

    def __str__(self):
        return f"Account({self._account_number}): {self._account_holder} with balance ${self._balance}"


# User Class
class User:
    def __init__(self, username, password):
        self._username = username
        self._password = password  # Note: In real applications, use hashed passwords

    def check_password(self, password):
        return self._password == password


# Transaction Class
class Transaction:
    def __init__(self, transaction_id, account, amount, transaction_type):
        self._transaction_id = transaction_id
        self._account = account
        self._amount = amount
        self._transaction_type = transaction_type
        self.process_transaction()

    def process_transaction(self):
        if self._transaction_type == "deposit":
            self._account.deposit(self._amount)
        elif self._transaction_type == "withdrawal":
            self._account.withdraw(self._amount)
        else:
            print("Invalid transaction type.")


# Bank Class
class Bank:
    def __init__(self):
        self._accounts = {}
        self._users = {}
        self._logged_in_user = None

    def register_user(self, username, password):
        if username in self._users:
            print("User already exists.")
        else:
            self._users[username] = User(username, password)
            print(f"User {username} registered successfully.")

    def login_user(self, username, password):
        user = self._users.get(username)
        if user and user.check_password(password):
            self._logged_in_user = username
            print(f"User {username} logged in successfully.")
        else:
            print("Invalid username or password.")

    def logout_user(self):
        if self._logged_in_user is None:
            print("No user is currently logged in.")
        else:
            self._logged_in_user = None
            print("Logged out successfully.")

    def add_account(self, account):
        if self._logged_in_user is None:
            print("Please log in first.")
            return
        
        if account._account_number in self._accounts:
            print("Account already exists.")
        else:
            self._accounts[account._account_number] = account
            print(f"Account {account._account_number} added.")

    def remove_account(self, account_number):
        if self._logged_in_user is None:
            print("Please log in first.")
            return

        if account_number in self._accounts:
            del self._accounts[account_number]
            print(f"Account {account_number} removed.")
        else:
            print("Account not found.")

    def get_account(self, account_number):
        if self._logged_in_user is None:
            print("Please log in first.")
            return None

        return self._accounts.get(account_number)

    def __str__(self):
        if self._logged_in_user is None:
            return "Please log in to view accounts."
        
        accounts_str = ""
        for account in self._accounts.values():
            accounts_str += str(account) + "\n"
        return accounts_str.strip()  # Remove the trailing newline

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
        print("7. Withdraw Money")
        print("8. Exit")

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
            if bank._logged_in_user is None:
                print("You must be logged in to create an account.")
                continue
            
            account_number = input("Enter account number: ")
            account_holder = input("Enter account holder name: ")
            try:
                initial_balance = float(input("Enter initial balance: "))
                account = Account(account_number, account_holder, initial_balance)
                bank.add_account(account)
            except ValueError:
                print("Invalid balance amount. Please enter a numeric value.")

        elif choice == "5":
            if bank._logged_in_user is None:
                print("You must be logged in to remove an account.")
                continue
            
            account_number = input("Enter account number to remove: ")
            bank.remove_account(account_number)

        elif choice == "6":
            print("\nCurrent bank accounts:")
            print(bank)

        elif choice == "7":
            if bank._logged_in_user is None:
                print("You must be logged in to withdraw money.")
                continue

            account_number = input("Enter account number to withdraw from: ")
            account = bank.get_account(account_number)
            if account is None:
                print("Account not found.")
                continue
            
            try:
                amount = float(input("Enter amount to withdraw: "))
                if amount <= 0:
                    print("Amount must be positive.")
                    continue
                account.withdraw(amount)
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")

        elif choice == "8":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
