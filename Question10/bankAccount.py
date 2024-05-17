class BankAccount:
    def __init__(self, balance, accountNumber, accountHolder):
        self.balance = balance
        self.accountNumber = accountNumber
        self.accountHolder = accountHolder

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def getBalance(self):
        return self.balance

    def displayInfo(self):
        print(f"Account Number: {self.accountNumber}, Account Holder: {self.accountHolder}, Balance: {self.balance}")


if __name__ == '__main__':
    ba1 = BankAccount(2000, 1111, 'Aayush Soni')
    ba2 = BankAccount(3000, 1112, 'Bhinsar')

    ba1.deposit(1000)
    ba1.withdraw(500)
    ba1.displayInfo()

    ba2.deposit(2000)
    ba2.withdraw(5000)
    ba2.displayInfo()
