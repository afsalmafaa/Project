from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        pass

    def withdraw(self,amount):
        pass

    def get_balance(self):
        return self.balance
    
class CheckingAccount(Account):
    def __init__(self, account_number, balance):
        super().__init__(account_number,balance)

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient Funds")

class SavingsAccount(Account):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient Funds")

class BusinessAccount(Account):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient Funds")

def main():
    checking_account = CheckingAccount("12345", 1000.0)
    savings_account = SavingsAccount("67890", 5000.0)
    business_account = BusinessAccount("54321", 20000.0)

    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            account_type = input("Enter account type (C for Checking, S for Savings, B for Business): ")
            if account_type == "C":
                print(f"Checking Account Balance: ${checking_account.get_balance()}")
            elif account_type == "S":
                print(f"Savings Account Balance: ${savings_account.get_balance()}")
            elif account_type == "B":
                print(f"Business Account Balance: ${business_account.get_balance()}")
            else:
                print("Invalid account type")

        elif choice == "2":
            account_type = input("Enter account type (C for Checking, S for Savings, B for Business): ")
            amount = float(input("Enter the deposit amount: "))
            if account_type == "C":
                checking_account.deposit(amount)
                print("Your amount has been Deposited")
            elif account_type == "S":
                savings_account.deposit(amount)
                print("Your amount has been Deposited")
            elif account_type == "B":
                business_account.deposit(amount)
                print("Your amount has been Deposited")
            else:
                print("Invalid account type")

        elif choice == "3":
            account_type = input("Enter account type (C for Checking, S for Savings, B for Business): ")
            amount = float(input("Enter the withdrawal amount: "))
            if account_type == "C":
                checking_account.withdraw(amount)
                print("Your withdrawal is complete. Don't spend it all in one place!")
            elif account_type == "S":
                savings_account.withdraw(amount)
                print("Your withdrawal is complete. Don't spend it all in one place!")
            elif account_type == "B":
                business_account.withdraw(amount)
                print("Your withdrawal is complete. Don't spend it all in one place!")
            else:
                print("Invalid account type")
            
        elif choice == "4":
            print("Exiting the ATM program. Have a nice day!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
