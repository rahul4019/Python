from bank_accounts import *

Rahul = BankAccount(50000, "Rahul")
Sara = BankAccount(10000, "Sara")

# Rahul.getBalance()
# Sara.getBalance()

Rahul.deposit(19591)
Sara.deposit(9131)

# Rahul.withdraw(571059105)
Rahul.withdraw(10)
# Rahul.transfer(15701705,Sara)
Rahul.transfer(1000, Sara)

Jim = InterestRewardAccount(1000, "Jim")

Jim.getBalance()
Jim.deposit(100)

Jim.transfer(100, Rahul)

Blaze = SavingAccount(70000, "Blaze")

Blaze.getBalance()

Blaze.deposit(10000)

# Blaze.transfer(100000, Sara)
Blaze.transfer(10000, Sara)
