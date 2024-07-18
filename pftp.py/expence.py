
def add_expense(amount, category,transactions):
    transaction = {'type': 'expense', 'amount': amount, 'category': category}
    transactions.append(transaction)
    print(f"Expense of ${amount} added successfully.")