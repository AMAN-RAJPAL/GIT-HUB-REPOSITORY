import pymysql

# Connect to the MySQL server
db = pymysql.connect(host="localhost", user="root", password="manager", port=3306)
cur = db.cursor()

# Create the database
try:
    cur.execute("CREATE DATABASE Bank")
    print("Database created")
except:
    print("Database already created")

# Use the database
cur.execute("USE Bank")

# Create the table
try:
    cur.execute("""
        CREATE TABLE accounts (
            id INT PRIMARY KEY, 
            account_number VARCHAR(25) NOT NULL UNIQUE, 
            account_holder VARCHAR(25) NOT NULL, 
            balance INT
        );
    """)
    print("Table created")
except:
    print("Table already exists")

# Function to create a new account
def create_account():
    _id_ = int(input("Enter id: "))
    an = input("Enter account number: ")
    ah = input("Enter account holder's name: ")
    bal = int(input("Enter balance: "))
    sql = "INSERT INTO accounts (id, account_number, account_holder, balance) VALUES (%s, %s, %s, %s)"
    cur.execute(sql, (_id_, an, ah, bal))
    db.commit()
    print("Record inserted")

# Function to view all accounts
def view_accounts():
    sql = "SELECT * FROM accounts"
    cur.execute(sql)
    records = cur.fetchall()
    for rec in records:
        print(rec)

# Function to deposit amount
def deposit(an, amt):
    sql = "UPDATE accounts SET balance = balance + %s WHERE account_number = %s"
    cur.execute(sql, (amt, an))
    db.commit()
    print('Amount deposited')

# Function to withdraw amount
def withdraw(an, am):
    sql = "UPDATE accounts SET balance = balance - %s WHERE account_number = %s"
    cur.execute(sql, (am, an))
    db.commit()
    print('Amount withdrawn')

# Function to check balance
def check_balance(an):
    sql = "SELECT balance FROM accounts WHERE account_number = %s"
    cur.execute(sql, (an,))
    balance = cur.fetchone()
    if balance:
        print("Balance:", balance[0])
    else:
        print("Account not found")

# Main function to interact with the bank system
def main():
    while True:
        print("\nBank Management System")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. View Accounts")
        print("6. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            create_account()
        elif choice == 2:
            an = input('Enter your account number: ')
            am = int(input('Enter amount to be deposited: '))
            deposit(an, am)
        elif choice == 3:
            an = input('Enter your account number: ')
            am = int(input('Enter amount to be withdrawn: '))
            withdraw(an, am)
        elif choice == 4:
            an = input('Enter your account number: ')
            check_balance(an)
        elif choice == 5:
            view_accounts()
        elif choice == 6:
            break
        else:
            print("Invalid choice. Please try again.")

main()
