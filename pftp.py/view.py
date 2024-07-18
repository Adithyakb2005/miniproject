
def view_transactions(transactions):
    print("Transactions:")
    for transaction in transactions:
        print(f"- {transaction['type']}: ${transaction['amount']} (Category: {transaction['category']})")

