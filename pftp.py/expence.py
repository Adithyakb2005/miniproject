def add_expense(amount, category):
    transaction = {'type': 'expense', 'amount': amount, 'category': category}
    transaction.append(transaction)
    print(f"Expense of ${amount} added successfully.")