from incomeadd import *
from  expence import *
from  cblance import *
from  view import *
transactions = []
def main():
    while True:
        print("\nPersonal Finance Tracker")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Balance")
        print("4. View All Transactions")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            amount = float(input("Enter income amount: "))
            category = input("Enter income category: ")
            add_income(amount, category,transactions)
        elif choice == '2':
            amount = float(input("Enter expense amount: "))
            category = input("Enter expense category: ")
            add_expense(amount, category,transactions)
        elif choice == '3':
            balance=calculate_balance(transactions)
            print(f"Current Balance: ${balance}")
        elif choice == '4':
            view_transactions(transactions)
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

main()