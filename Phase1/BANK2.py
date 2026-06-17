import json

FILE_NAME = "bankAcc.json"


class BankAccount:
    def __init__(self, ac_number, balance, ac_holder):
        self.ac_number = ac_number
        self.balance = balance
        self.ac_holder = ac_holder

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be greater than 0.")

        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be greater than 0.")

        if amount > self.balance:
            raise ValueError("Insufficient Balance.")

        self.balance -= amount

    def to_dict(self):
        return {
            "ac_number": self.ac_number,
            "balance": self.balance,
            "ac_holder": self.ac_holder
        }


def load_accounts():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        return []


def save_accounts(accounts):
    with open(FILE_NAME, "w") as file:
        json.dump(accounts, file, indent=4)


def find_account(accounts, account_number):
    for account in accounts:
        if account["ac_number"] == account_number:
            return account
    return None


def create_account(accounts):

    account_number = input("Enter Account Number: ").strip()

    if find_account(accounts, account_number):
        print("Account already exists.")
        return

    account_holder = input("Enter Account Holder Name: ").strip()

    try:
        balance = float(input("Enter Initial Balance: "))

        if balance <= 0:
            print("Balance must be greater than 0.")
            return

    except ValueError:
        print("Invalid balance.")
        return

    account = BankAccount(
        account_number,
        balance,
        account_holder
    )

    accounts.append(account.to_dict())

    save_accounts(accounts)

    print("Account created successfully.")


def deposit_money(accounts):

    account_number = input("Enter Account Number: ").strip()

    account = find_account(accounts, account_number)

    if not account:
        print("Account not found.")
        return

    try:
        amount = float(input("Enter Deposit Amount: "))

        if amount <= 0:
            raise ValueError("Amount must be greater than 0.")

        account["balance"] += amount

        save_accounts(accounts)

        print(f"₹{amount} deposited successfully.")

    except ValueError as e:
        print("", e)


def withdraw_money(accounts):

    account_number = input("Enter Account Number: ").strip()

    account = find_account(accounts, account_number)

    if not account:
        print("Account not found.")
        return

    try:
        amount = float(input("Enter Withdrawal Amount: "))

        if amount <= 0:
            raise ValueError("Amount must be greater than 0.")

        if amount > account["balance"]:
            raise ValueError("Insufficient Balance.")

        account["balance"] -= amount

        save_accounts(accounts)

        print(f"₹{amount} withdrawn successfully.")

    except ValueError as e:
        print("", e)


def check_balance(accounts):

    account_number = input("Enter Account Number: ").strip()

    account = find_account(accounts, account_number)

    if not account:
        print("Account not found.")
        return

    print(f"\nCurrent Balance: ₹{account['balance']}")


def view_account_details(accounts):

    account_number = input("Enter Account Number: ").strip()

    account = find_account(accounts, account_number)

    if not account:
        print("Account not found.")
        return

    print("\n===== ACCOUNT DETAILS =====")
    print("Account Holder :", account["ac_holder"])
    print("Account Number :", account["ac_number"])
    print("Balance        : ₹", account["balance"])


def view_all_accounts(accounts):

    if len(accounts) == 0:
        print("No accounts available.")
        return

    print("\n===== ALL ACCOUNTS =====")

    for account in accounts:
        print("-" * 30)
        print("Account Holder :", account["ac_holder"])
        print("Account Number :", account["ac_number"])
        print("Balance        : ₹", account["balance"])

    print("-" * 30)
    print("Total Accounts:", len(accounts))


def delete_account(accounts):

    account_number = input("Enter Account Number to Delete: ").strip()

    account = find_account(accounts, account_number)

    if not account:
        print("Account not found.")
        return

    accounts.remove(account)

    save_accounts(accounts)

    print("Account deleted successfully.")


def main():

    accounts = load_accounts()

    while True:

        print("\n===== BANK MANAGEMENT SYSTEM =====")
        print("1. Create Account")
        print("2. Deposit Money")
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
            view_account_details(accounts)

        elif choice == "6":
            view_all_accounts(accounts)

        elif choice == "7":
            delete_account(accounts)

        elif choice == "8":
            print("Thank you for using Bank Management System.")
            break

        else:
            print("Invalid Choice. Please enter 1-8.")


if __name__ == "__main__":
    main()