

class Currency:
    def __init__(self, name, symbol, exchange_rate):
        self.name = name
        self.symbol = symbol
        self.excange_rate = 1.0

    def convert(self, amount):
        return amount * self.excange_rate
    
class Wallet:
    def __init__(self, currency, balance):
        self.currency = currency
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        else:
            self.balance -= amount
        
    def check_balance(self):
        return self.balance
    
class User:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = Wallet(Currency("USD", "$", 1.0), 0.0)

    def deposit(self, amount):
        self.wallet.deposit(amount)

    def withdraw(self, amount):
        self.wallet.withdraw(amount)

    def check_balance(self):
        return self.wallet.check_balance()
