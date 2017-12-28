def make_withdraw(balance):
    """Return a withdraw function that draws down balance with each call."""
    def withdraw(amount):
        nonlocal balance                 # Declare the name "balance" nonlocal
        if amount > balance:
            return 'Insufficient funds'
        balance = balance - amount       # Re-bind the existing balance name
        return balance
    return withdraw

withdraw = make_withdraw(100)

print(withdraw(25))
print(withdraw(25))
print(withdraw(60))
print(withdraw(15))