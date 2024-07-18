

def calculate_balance(transactions):
    total_income = 0
    total_expense = 0

    for transaction in transactions:
        if transaction['type'] == 'income':
            total_income += transaction['amount']
        elif transaction['type'] == 'expense':
            total_expense += transaction['amount']

    balance = total_income - total_expense
    return balance
