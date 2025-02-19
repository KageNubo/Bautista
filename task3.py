class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self):
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            self.balance += amount
            print(f"Deposited PHP{amount}. New balance: PHP{self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self):
        amount = float(input("Enter amount to withdraw: "))
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew PHP{amount}. New balance: PHP{self.balance}")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            print("Invalid withdrawal amount.")

    def display_balance(self):
        print(f"Account {self.account_number} - {self.owner} Balance: PHP{self.balance}")


account1 = BankAccount("\n111-222-234", "\nJohn Rophi Bautista\n", 1000)


account1.display_balance()
account1.deposit()
account1.withdraw()
account1.display_balance()
