class BalanceException(Exception):
    pass


class BankAccount:
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName
        print(f"\nAccount '{self.name}' created.\nBalance = ₹{
              self.balance:.2f}")

    def getBalance(self):
        print(f"\nAccount '{self.name}' balance = ₹{self.balance:.2f}")

    def deposit(self, amount):
        self.balance += amount
        print(f"\nDeposit complete.")
        self.getBalance()

    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"\nSorry, account '{
                self.name}' only has a balance of ₹{self.balance:.2f}")

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance -= amount
            print(f"\n Withdraw complete.")
            self.getBalance()
        except BalanceException as error:
            print(f'\nWithdraw intrupted: {error}')

    def transfer(self, amount, account):
        try:
            print('\n**************\n\nBeginning Transfer..🚀')
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print(f'\nTransfer complete! ✅\n\n**************')
        except BalanceException as error:
            print(f'\n Transfer interrupted. ❌{error}')


class InterestRewardAccount(BankAccount):
    def deposit(self, amount):
        self.balance += (amount * 1.05)
        print('\nDeposit complete.')
        self.getBalance()


class SavingAccount(InterestRewardAccount):
    def __init__(self, initialAmount, accountName):
        super().__init__(initialAmount, accountName)
        self.fee = 100

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance -= amount + self.fee
            print('\nWithdraw complete.')
            self.getBalance()
        except BalanceException as error:
            print(f'\nWithdraw interrupted: {error}')
