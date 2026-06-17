import json

FILE_NAME = "accounts.json"

class BankAccount:
    def __init__(self,acc_number,acc_holder,balance):
        self.acc_number = acc_number
        self.acc_holder = acc_holder
        self.balance = balance
    
    def to_dict(self):
        return{
            "acc_number":self.acc_number,
            "acc_holder":self.acc_holder,
            "balance":self.balance 
        }

    
def load_accounts():
    try:
        with open(FILE_NAME,"r") as file:
            json.load(file)
    except:
        return[]

def save_accounts(accounts):
    with open(FILE_NAME,"w") as file:
        json.dump(accounts,file,indent=4)

def find_acc(accounts,acc_number):
    for account in accounts:
        if account["acc_number"] == acc_number:
            return account
    return None

def create_account(accounts):

    acc_number = input("Enter Account Number: ").strip()

    if find_acc(accounts,acc_number):
        print("Account already exist")
        return 
    
    acc_holder = input("Enter Account Holder Name: ").strip()

    try:
        balance = float(input("Enter Initial Balance: "))
        if balance <= 0:
            print("Balance must be greater than 0.")
            return
    except ValueError:
        print("Invalid Balance.")
        return
    
    account = BankAccount(acc_number,acc_holder,balance)
    accounts.append(account.to_dict())
    save_accounts(accounts)
    print("Account Created Successfully.")

def deposit_money(accounts):
    acc_number = input("Enter Account Number: ").strip()
    account = find_acc(accounts,acc_number)

    if not account:
        print("Account Not Found")
        return
    
    try:
        amount = float(input("Enter Deposit Amount: "))
        if amount <= 0:
            raise ValueError("Amount must be greater than 0.")
        
        account["balance"] += amount
        save_accounts(accounts)
        print(f"₹{amount} deposited successfully.")
    except ValueError as e:
        print(e)

def main():

    accounts = load_accounts()

    while True:
        print("\n===== BANK MANAGEMENT SYSTEM =====")
        print("1. Create Account")
        print("2. Deposit Account")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. View Account Details")
        print("6. View All Accounts")
        print("7. Delete Account")
        print("8. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            create_account(accounts)
        elif choice == "2":
            deposit_money(accounts)
        elif choice == "3":
            withdraw_money(accounts)
        elif choice == "4":
            check_balance(accounts)
        elif choice == "5":
            view_accounts_details(accounts)
        elif choice == "6":
            view_all_accounts(accounts)
        elif choice == "7":
            delete_accounts(accounts)
        elif choice == "8":
            print("Thank you for using Bank Management System.")
            break
        else:
            print("Invalid Choice! Please enter 1-8.")
        