import sqlite3
conn = sqlite3.connect('stock.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS stock (
        id INTEGER PRIMARY KEY,
        name TEXT,
        quantity INTEGER,
        price REAL
    )
''')


def add_stock():
    name = input('Enter stock name: ')
    quantity = int(input('Enter quantity: '))
    price = float(input('Enter price: '))
    cursor.execute('INSERT INTO stock (name, quantity, price) VALUES (?, ?, ?)', (name, quantity, price))
    conn.commit()


def update_stock():
    id = int(input('Enter stock ID: '))
    name = input('Enter new name: ')
    quantity = int(input('Enter new quantity: '))
    price = float(input('Enter new price: '))
    cursor.execute('UPDATE stock SET name = ?, quantity = ?, price = ? WHERE id = ?', (name, quantity, price, id))
    conn.commit()


def delete_stock():
    id = int(input('Enter stock ID: '))
    cursor.execute('DELETE FROM stock WHERE id = ?', (id,))
    conn.commit()


def view_stock():
    cursor.execute('SELECT * FROM stock')
    rows = cursor.fetchall()
    for row in rows:
        print(f'ID: {row[0]}, Name: {row[1]}, Quantity: {row[2]}, Price: {row[3]}')

while True:
    print('1. Add Stock')
    print('2. Update Stock')
    print('3. Delete Stock')
    print('4. View Stock')
    print('5. Quit')
    choice = input('Enter choice: ')
    if choice == '1':
        add_stock()
    elif choice == '2':
        update_stock()
    elif choice == '3':
        delete_stock()
    elif choice == '4':
        view_stock()
    elif choice == '5':
        break
    else:
        print('Invalid choice')

