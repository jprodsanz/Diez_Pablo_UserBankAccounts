class User:

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = {}
        
    def create_account(self,with_amount=0,int_rate=0.04,account_type="checking"):
        self.accounts[account_type] = BankAccount(with_amount,int_rate,account_type)
        return self

    def deposit(self, amount,account_type="checking"):
        self.accounts[account_type].deposit(amount)
        return self
    
    def withdraw(self, amount, account_type="checking"):
        self.accounts[account_type].withdraw(amount)
        return self
    
    def display_balance(self):
        print(self.name)
        for account_name in self.accounts:
            self.accounts[account_name].display_account_info()
        return self

class  BankAccount:
    accounts = []

    def __init__(self, int_rate, balance,account_type="checking"):
        self.int_rate = int_rate
        self.balance = balance
        self.account_type = account_type
        BankAccount.accounts.append(self)
    
    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print('negative funds: $100 Fee')
            self.balance -= 100
        return self

    def display_account_info(self):
        print('account:', self.account_type)
        print('account_balance $',str(self.balance))
        print('int_rate',self.int_rate)
        return self
    
    def yield_interest(self):
        if self.balance > 0: 
            self.balance +=(self.balance * self.int_rate)
        return self

    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

savings =  BankAccount(0.5,2000)
checking = BankAccount(0.7,750)

savings.deposit(30).deposit(50).withdraw(10).yield_interest().display_account_info()
savings.deposit(300).deposit(500).withdraw(100).yield_interest().display_account_info()

BankAccount.print_all_accounts() 