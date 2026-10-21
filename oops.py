class Account:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def widrawmoney(self,amount):
        self.amount = amount
        print(a1.name, a1.balance)
        if self.balance > amount:
            self.balance =  self.balance - self.amount
        else:
            print("widraw money")


a1 = Account("riya", 1000)
a2 = Account("meena", 500)
a1.widrawmoney(200)


print(a1.balance)
