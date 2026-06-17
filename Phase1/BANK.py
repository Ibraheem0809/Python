import json

FILE_NAME = "bankAcc.json"


class BankAccount:
    def __init__(self, ac_number, balance, ac_holder):
        self.ac_number = ac_number
        self.balance = balance
        self.ac_holder = ac_holder

    def details(self):
        print(f"A/C Number : {self.ac_number}")
        print(f"A/C Holder : {self.ac_holder}")
        print(f"Balance    : ₹{self.balance}")

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


def create_account(accounts):

    ac_number = input("Enter Account Number: ").strip()

    # Check duplicate account number
    for account in accounts:
        if account["ac_number"] == ac_number:
            print("❌ Account already exists with this account number.")
            return

    ac_holder = input("Enter Account Holder Name: ").strip()

    try:
        balance = float(input("Enter Initial Balance: "))

        if balance <= 0:
            print("❌ Balance must be greater than 0.")
            return

    except ValueError:
        print("❌ Please enter a valid amount.")
        return

    new_account = BankAccount(
        ac_number,
        balance,
        ac_holder
    )

    accounts.append(new_account.to_dict())
    save_accounts(accounts)

    print("✅ Account created successfully!")


def view_all_accounts(accounts):

    if len(accounts) == 0:
        print("No accounts available.")
        return

    print("\n===== ALL ACCOUNTS =====")

    for account in accounts:
        print("------------------------")
        print("A/C Number :", account["ac_number"])
        print("A/C Holder :", account["ac_holder"])
        print("Balance    : ₹", account["balance"])

    print("------------------------")
    print("Total Accounts:", len(accounts))


def main():

    accounts = load_accounts()

    while True:

        print("\n===== BANK MANAGEMENT SYSTEM =====")
        print("1. Create Account")
        print("2. View All Accounts")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            create_account(accounts)

        elif choice == "2":
            view_all_accounts(accounts)

        elif choice == "3":
            print("Thank you for using Bank Management System.")
            break

        else:
            print("❌ Invalid Choice. Please try again.")


if __name__ == "__main__":
    main()