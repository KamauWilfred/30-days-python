print("=============BANK TRANSFER SIMULATOR=================")

import sqlite3
connection = sqlite3.connect("bank.db")
cursor = connection.cursor()

try:
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS accounts(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    balance INTEGER NOT NULL
    )
    """)

    connection.commit()

    account_info = []
    sender_name = input("\nEnter sender's name: ").strip().lower()
    reciever_name = input("Enter reciever's name: ").strip().lower()

    for person in [sender_name, reciever_name]:
        while True:
            try:
                balance = int(input("Enter {person}'s balance: "))
                if balance >= 0:
                    account_info.append((person, balance))
                    break
                print("Balance cannot be negative!")
            except ValueError:
                print("Enter an integer value!")

    cursor.executemany(
        "INSERT INTO accounts(name, balance) VALUES(?, ?)",
        account_info
    )
    connection.commit()

    cursor.execute(
        "SELECT id, name, balance FROM accounts"
    )
    accounts = cursor.fetchall()

    print("\nAccounts")
    for account in accounts:
        print(f"ID: {account[0]} | Name: {account[1]} | Balance: {account[2]}")

    sender_id = accounts[-2][0]
    reciever_id = accounts[-1][0]

    while True:
        try:
            transfer_amount = int(input("\nEnter amount to transfer: "))
            if transfer_amount > 0:
                break
            print("Amount must be greater than zero!")
        except ValueError:
            print("Enter an integer value!")

    cursor.execute(
        "SELECT balance FROM accounts WHERE id = ?",
        (sender_id,)
    )
    sender = cursor.fetchone()

    if sender == None:
        print("Sender account not found!")

    elif sender[0] < transfer_amount:
        print("Insufficient funds. Transfer cancelled!")

    else:
        try:
            cursor.execute("Begin")

            cursor.execute(
                "UPDATE accounts SET balance = balance - ? WHERE id = ?",
                (transfer_amount, sender_id)
            )

            cursor.execute(
                "UPDATE accounts SET balance = balance + ? WHERE id = ?",
                (transfer_amount, reciever_id)
            )

            if cursor.rowcount == 0:
                raise ValueError("Reciever account not found!")
            connection.commit()
            print("Transfer successful!")

        except(sqlite3.Error, ValueError)as error:
            connection.rollback()
            print("Transfer failed. changes rolled back!")
            print("Reason: ",error)

    cursor.execute(
        "SELECT id, name, balance FROM accounts"
    )

    print("\nFinal Account Balances")
    for account in cursor.fetchall():
        print(f"ID: {account[0]} | Name: {account[1]} | Balance: {account[2]}")

except sqlite3.Error as error:
    connection.rollback()
    print("Database error: ", error)

finally:
    connection.close()

print("================================================================")



    