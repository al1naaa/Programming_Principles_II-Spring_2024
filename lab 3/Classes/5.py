class Account:
    def __init__(self, owner, balance):
        self.owner=owner
        self.balance=balance
    def deposit(self, months, percent):
        for i in range(months):
            self.balance+=self.balance*(percent/100)
        print("Your current balance is equal to", self.balance)
    def withdraw(self, wtdr):
        if wtdr<0:
            print("You haven't withdrawn the money")
        elif wtdr>self.balance:
            print("Your balance does not have such a withdraw")
        else:
            print("You took it off", wtdr, " and your current balance is exactly ", self.balance-wtdr)
            self.balance=self.balance-wtdr
x=Account("Alina", 50000)
x.deposit(24, 15)
x.withdraw(25000)