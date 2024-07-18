
def add_income(amount, category,transactions):
    transaction = {'type': 'income', 'amount': amount, 'category': category}
    transactions.append(transaction)
    print(f"Income of ${amount} added successfully.")
