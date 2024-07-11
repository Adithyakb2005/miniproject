def view_transactions():
    print("All Transactions:")
    for transaction in transaction:
        print(f"{transaction['type'].title()} of ${transaction['amount']} in '{transaction['category']}' category")
