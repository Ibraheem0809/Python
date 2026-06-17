class BankAccount:
    def __init__(self,ac_number,balance,ac_holder):
        self.ac_number = ac_number
        self.balance = balance
        self.ac_holder = ac_holder

    def deposit(self,amount):
        if amount <= 0:
            raise ValueError("Amount cannot be negative or zero.")
        self.balance += amount
        print(f"₹{amount} deposited successfully.")

    def withdraw(self,amount):
        if amount > self.balance:
            raise ValueError("Insufficient Balance")
        if amount <= 0:
            raise ValueError("Amount cannot be negative or zero.")
        self.balance -= amount
        print(f"₹{amount} withdrawn successfully.")

    def check(self):
        print("A/c Holder:",self.ac_holder)
        print("Balance: ₹",self.balance)

    def details(self):
        print("A/c Holder:",self.ac_holder)
        print("Balance: ₹",self.balance)
        print("A/c Number:",self.ac_number)

    def to_dict(self):
        return {
            "ac_holder": self.ac_holder,
            "balance": self.balance,
            "ac_number": self.ac_number
        }

import json

FILE_NAME = "bankAcc.json"
accounts = []

def load_acc():
    try:
        with open(FILE_NAME,"r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
    
def save_acc(accounts):
    with open(FILE_NAME,"w") as file:
        json.dump(accounts, file, indent=4)

def createAcc():
    acc_number = int(input("Enter Account Number:"))
    for account in accounts:
        if acc_number == account["ac_number"]:
            print("Account Already Ecixt for this A/C Number")
            return
    acc_holder = input("Enter A/C Holder Name:")
    balance = int(input("Initial Balance:"))
    if balance <= 0:
        print("Balance should be greater than 0")
    account1 = BankAccount(acc_number,balance,acc_holder)
    accounts.append(account1.to_dict())
    save_acc()


def main():
    accounts = load_acc()

    while True:
        print("\n===== BANK MANAGEMENT SYSTEM =====")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. View Account Details")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            pass

        elif choice == "2":
            amt = int(input("Enter amount to be deposited:"))
            
            Deposit(amt)
            save_acc()


        elif choice == "3":
            amt = int(input("Enter amount to be deposited:"))
            Withdraw(amt)
            save_acc()

        elif choice == "4":
            Check()

        elif choice == "5":
            Details()

        elif choice == "6":
            print("Thank you for using Student Management System.")
            break