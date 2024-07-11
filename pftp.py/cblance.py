def calculate_balance():
    total_income = sum(transaction['amount'] for transaction in  transactions if transaction['type'] == 'income')
    total_expense = sum(transaction['amount'] for transaction in transactions if transaction['type'] == 'expense')
    balance = total_income - total_expense
    return balance