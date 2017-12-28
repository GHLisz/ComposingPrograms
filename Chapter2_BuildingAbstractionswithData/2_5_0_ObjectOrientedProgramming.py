class Account:
    """A bank account that has a non-negative balance."""
    interest = 0.02            # A class attribute

    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder

    def deposit(self, amount):
        """Increase the account balance by amount and return the new balance."""
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        """Decrease the account balance by amount and return the new balance."""
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        return self.balance

spock_account = Account('Spock')
print(spock_account.deposit(100))
print(spock_account.withdraw(90))
print(spock_account.withdraw(90))
print(spock_account.holder)

spock_account = Account('Spock')
kirk_account = Account('Kirk')
print(spock_account.interest)
print(kirk_account.interest)

# a single assignment statement to a class attribute
# changes the value of the attribute for all instances of the class.
Account.interest = 0.04
print(spock_account.interest)
print(kirk_account.interest)

# If we assign to the named attribute interest of an account instance,
# we create a new instance attribute that has the same name as the existing class attribute.
kirk_account.interest = 0.08
print(kirk_account.interest)
print(spock_account.interest)

# Changes to the class attribute interest will affect spock_account,
# but the instance attribute for kirk_account will be unaffected.
Account.interest = 0.05
print(spock_account.interest)
print(kirk_account.interest)


class CheckingAccount(Account):
    """A bank account that charges for withdrawals."""
    withdraw_charge = 1
    interest = 0.01

    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_charge)

checking = CheckingAccount('Sam')
print(checking.deposit(10))
print(checking.withdraw(5))
print(checking.interest)


class SavingsAccount(Account):
    deposit_charge = 2

    def deposit(self, amount):
        return Account.deposit(self, amount - self.deposit_charge)


class AsSeenOnTVAccount(CheckingAccount, SavingsAccount):
    # ambiguous reference order: AsSeenOnTVAccount, CheckingAccount, SavingsAccount, Account, object
    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 1           # A free dollar!
