def add_income(amount, category):
    transaction = {'type': 'income', 'amount': amount, 'category': category}
    transaction.append(transaction)
    print(f"Income of ${amount} added successfully.")

